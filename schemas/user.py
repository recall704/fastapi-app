from pydantic import BaseModel


class UserLogin(BaseModel):
    username: str
    password: str


class TokenData(BaseModel):
    accessToken: str = None
    tokenType: str = "Bearer"
    expires: int = 3600
    refreshToken: str = None


class JwtToken(BaseModel):
    code: str
    data: TokenData
    msg: str
