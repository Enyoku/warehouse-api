from fastapi import FastAPI

from routers import router
from db.database import engine
from user import models

app = FastAPI()

app.include_router(router)

models.Base.metadata.create_all(engine)
