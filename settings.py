"""File with settings and configs for the project"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_DB: str
    POSTGRES_PASSWORD: int
    DB_PORT: int
    DB_HOST: str
    EXPIRE_MINUTES: int
    HOST_GRPC: str
    USER_PORT_GRPC: int
    SESSION_PORT_GRPC: int

    @property
    def DATABASE_URL_async(self):
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.POSTGRES_DB}"

    model_config = SettingsConfigDict(
        validate_default=False, env_file=".env", extra="allow"
    )


settings = Settings()
