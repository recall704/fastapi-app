from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from db.models import User
from schemas.user import JwtToken
from core.jwt import (
    verify_password,
    create_access_token,
    create_refresh_token,
    decode_user,
)
from utils.captcha import generate_captcha

router = APIRouter()


# 4. get current user
# 输入：access token
# 输出：user
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
    )
    username = decode_user(token, exception=credentials_exception)
    # check if user exists in db
    user = await User.get_or_none(username=username)
    if user is None:
        raise credentials_exception
    return user


# 1. login
# 输入：username, password
# 输出：access token
@router.post("/login", response_model=JwtToken)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await User.get_or_none(username=form_data.username)
    if not user or not verify_password(form_data.password, user.password_hash):
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    access_token = create_access_token(data={"sub": user.username})
    refresh_token = create_refresh_token(data={"sub": user.username})
    return {
        "code": "00000",
        "data": {
            "accessToken": access_token,
            "tokenType": "Bearer",
            "expires": 3600,
            "refreshToken": refresh_token,
        },
        "msg": "ok",
    }


# 2. logout
# 输入：access token
# 输出：无
@router.delete("/logout")
async def logout(user: str = Depends(get_current_user)):
    return {
        "msg": "ok",
        "code": "00000",
        "data": None,
    }


# 3. refresh token
# 输入：refresh token
# 输出：access token
@router.post("/refresh")
async def refresh_token(refresh_token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
    )
    user = decode_user(refresh_token, credentials_exception)
    access_token = create_access_token(data={"sub": user.username})
    return {
        "code": "00000",
        "data": {
            "accessToken": access_token,
            "tokenType": "Bearer",
            "expires": 3600,
            "refreshToekn": refresh_token,
        },
        "msg": "ok",
    }


# 5. get captcha
# 输入：无
# 输出：captcha base64
@router.get("/captcha")
async def captcha():
    # TODO 生成一个 id，将 id 和验证码值存在 db 中
    # 在 login 时，获取用户输入，根据 id 获取验证码值，进行比对
    key, bs64img = generate_captcha()
    return {
        "code": "00000",
        "msg": "ok",
        "data": {
            "captchaKey": key,
            "captchaBase64": bs64img,
        },
    }
