from enum import Enum
from pydantic import SecretStr
from pydantic_settings import BaseSettings

class LoggingRenderer(str, Enum):
    JSON = "json"
    CONSOLE = "console"

class LoggingSettings(BaseSettings):
    level: str = "INFO"
    format: str = "%Y-%m-%d %H:%M:%S"
    is_utc: bool = False
    renderer: LoggingRenderer = LoggingRenderer.JSON
    log_unhandled: bool = False

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        env_prefix = "LOGGING_"

class BotSettings(BaseSettings):
    BOT_TOKEN: SecretStr
    BOT_DATABASE_HOST: str
    BOT_DATABASE_PORT: int
    BOT_DATABASE_NAME: str
    BOT_DATABASE_USER: str
    BOT_DATABASE_PASSWORD: SecretStr

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'

config = BotSettings()
log_config = LoggingSettings()