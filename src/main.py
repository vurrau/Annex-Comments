from fastapi import FastAPI

from src.api.comments.router import comment
from src.api.user.router import user

app = FastAPI()

routers = [user, comment]

for router in routers:
    app.include_router(router)



