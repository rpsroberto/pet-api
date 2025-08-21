# Configs Globais da app 
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "Pet API"
    app_version: str = "1.0.0"

    model_config = SettingsConfigDict(
        env_file = ".env", env_file_encoding = "utf-8"
    )
    
Settings = Settings()
    
    
    
    