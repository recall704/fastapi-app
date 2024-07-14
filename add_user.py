import asyncio
from tortoise import Tortoise
from db.models import User
from core.jwt import get_password_hash


async def add_user(username: str, password: str):
    await Tortoise.init(
        db_url="sqlite://db.sqlite3",
        modules={"models": ["db.models"]},
    )
    await Tortoise.generate_schemas()

    # 检查用户是否已存在
    existing_user = await User.filter(username=username).first()
    if existing_user:
        print(f"User {username} already exists.")
        return

    # 创建新用户
    hashed_password = get_password_hash(password)
    user = await User.create(username=username, password_hash=hashed_password)
    print(f"User {username} created successfully.")

    await Tortoise.close_connections()


if __name__ == "__main__":
    username = input("Enter username: ")
    password = input("Enter password: ")
    asyncio.run(add_user(username, password))
