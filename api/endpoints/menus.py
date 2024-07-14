from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from db.models import User
from schemas.user import JwtToken
from .auth import get_current_user

router = APIRouter()


@router.get("/routes")
async def menus_routes(current_user: Annotated[User, Depends(get_current_user)]):
    return {
        "code": "00000",
        "data": [
            {
                "path": "/doc",
                "component": "Layout",
                "redirect": "https://juejin.cn/post/7228990409909108793",
                "name": "/doc",
                "meta": {
                    "title": "平台文档",
                    "icon": "document",
                    "hidden": False,
                    "alwaysShow": False,
                    "params": None,
                },
                "children": [
                    {
                        "path": "internal-doc",
                        "component": "demo/internal-doc",
                        "name": "InternalDoc",
                        "meta": {
                            "title": "平台文档(内嵌)",
                            "icon": "document",
                            "hidden": False,
                            "alwaysShow": False,
                            "params": None,
                        },
                    },
                    {
                        "path": "https://juejin.cn/post/7228990409909108793",
                        "name": "Https://juejin.cn/post/7228990409909108793",
                        "meta": {
                            "title": "平台文档(外链)",
                            "icon": "link",
                            "hidden": False,
                            "alwaysShow": False,
                            "params": None,
                        },
                    },
                ],
            },
            {
                "path": "/multi-level",
                "component": "Layout",
                "name": "/multiLevel",
                "meta": {
                    "title": "多级菜单",
                    "icon": "cascader",
                    "hidden": False,
                    "alwaysShow": True,
                    "params": None,
                },
                "children": [
                    {
                        "path": "multi-level1",
                        "component": "demo/multi-level/level1",
                        "name": "MultiLevel1",
                        "meta": {
                            "title": "菜单一级",
                            "icon": "",
                            "hidden": False,
                            "alwaysShow": True,
                            "params": None,
                        },
                        "children": [
                            {
                                "path": "multi-level2",
                                "component": "demo/multi-level/children/level2",
                                "name": "MultiLevel2",
                                "meta": {
                                    "title": "菜单二级",
                                    "icon": "",
                                    "hidden": False,
                                    "alwaysShow": False,
                                    "params": None,
                                },
                                "children": [
                                    {
                                        "path": "multi-level3-1",
                                        "component": "demo/multi-level/children/children/level3-1",
                                        "name": "MultiLevel31",
                                        "meta": {
                                            "title": "菜单三级-1",
                                            "icon": "",
                                            "hidden": False,
                                            "keepAlive": True,
                                            "alwaysShow": False,
                                            "params": None,
                                        },
                                    },
                                    {
                                        "path": "multi-level3-2",
                                        "component": "demo/multi-level/children/children/level3-2",
                                        "name": "MultiLevel32",
                                        "meta": {
                                            "title": "菜单三级-2",
                                            "icon": "",
                                            "hidden": False,
                                            "keepAlive": True,
                                            "alwaysShow": False,
                                            "params": None,
                                        },
                                    },
                                ],
                            },
                        ],
                    },
                ],
            },
        ],
        "msg": "一切ok",
    }
