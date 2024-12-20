from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    initial_database_url: str = "mysql+mysqlconnector://root:sarasara@localhost"
    database_url: str = "mysql+mysqlconnector://root:sarasara@localhost/Fanni_3lbab"
    secret_key: str = "sarasara"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    class Config:
        env_file = ".env"
        extra = "allow"

settings = Settings()