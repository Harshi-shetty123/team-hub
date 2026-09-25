from pydantic_settings import BaseSettings, SettingsConfigDict
class Settings(BaseSettings):
    app_name: str = "Team Calendar"
    database_url: str  # no default: the app must fail fast if it's missing

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
