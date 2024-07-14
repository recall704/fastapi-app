from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from api.endpoints import auth, user, menus

app = FastAPI()

app.include_router(auth.router, prefix="/api/v1/auth")
app.include_router(user.router, prefix="/api/v1/users")
app.include_router(menus.router, prefix="/api/v1/menus")

register_tortoise(
    app,
    db_url="sqlite://db.sqlite3",
    modules={"models": ["db.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
