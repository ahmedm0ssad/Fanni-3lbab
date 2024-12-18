from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str = "mysql+mysqlconnector://Rana:Rana-555@localhost/Fanni_3lbab"
    secret_key: str = "Rana-555"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    class Config:
        env_file = ".env"
        extra="allow"

settings = Settings()