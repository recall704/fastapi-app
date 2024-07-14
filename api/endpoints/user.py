from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from db.models import User
from schemas.user import JwtToken
from .auth import get_current_user

router = APIRouter()


@router.get("/me")
async def read_users_me(current_user: Annotated[User, Depends(get_current_user)]):
    user = await User.get_or_none(username=current_user.username)
    if user is None:
        return {
            "code": "B0001",
            "msg": "User not found",
            "data": None,
        }
    return {
        "code": "00000",
        "data": {
            "userId": user.id,
            "nickname": "系统管理员",
            "avatar": "https://oss.youlai.tech/youlai-boot/2023/05/16/811270ef31f548af9cffc026dfc3777b.gif",
            "roles": ["admin"],
            "perms": [
                "sys:menu:delete",
                "sys:dept:edit",
                "sys:dict_type:add",
                "sys:dict:edit",
                "sys:dict:delete",
                "sys:dict_type:edit",
                "sys:menu:add",
                "sys:user:add",
                "sys:role:edit",
                "sys:dept:delete",
                "sys:user:edit",
                "sys:user:delete",
                "sys:user:password:reset",
                "sys:dept:add",
                "sys:role:delete",
                "sys:dict_type:delete",
                "sys:menu:edit",
                "sys:dict:add",
                "sys:role:add",
                "sys:user:query",
                "sys:user:export",
                "sys:user:import",
            ],
        },
        "msg": "ok",
    }
