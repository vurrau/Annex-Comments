from fastapi import FastAPI

from src.api.user.router import user

app = FastAPI()

routers = [user]

for router in routers:
    app.include_router(router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


