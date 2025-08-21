# Arquivo principal da aplicação 
#FastAPI

from fastapi import FastAPI 
from app.core.config import Settings
from app.routers import health 

app = FastAPI(
    title=Settings.app_name, 
    version=Settings.app_version
)

app.include_router(health.router)
