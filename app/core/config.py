from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "OrderFlow"
    app_version: str = "0.1.0"
    app_description: str = "Order management system for small businesses"

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
    }


settings = Settings()
