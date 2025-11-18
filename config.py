import os
from typing import Literal
import dotenv
import pydantic_settings

# Загружаем общие переменные окружения сначала
dotenv.load_dotenv()


class Config(pydantic_settings.BaseSettings):
    context: Literal['local_emulator', 'local_real', 'bstack'] = 'bstack'  # по дефолту запускает на bstack

    # Общие параметры
    deviceName: str = 'Pixel'
    udid: str = ''
    app: str = './app-alpha-universal-release.apk'
    timeout: float = 10.0

    # BrowserStack параметры
    BROWSERSTACK_USERNAME: str = ''
    BROWSERSTACK_ACCESS_KEY: str = ''
    BROWSERSTACK_PROJECT_NAME: str = 'default_name'
    BROWSERSTACK_BUILD_NAME: str = 'default_build'
    BROWSERSTACK_SESSION_NAME: str = 'default_session'
    remote_url: str = ''

    # Настройка загрузки переменных окружения
    model_config = pydantic_settings.SettingsConfigDict(
        env_file=('.env', f'.env.{os.getenv("CONTEXT", "bstack")}')
    )

    # Создаем экземпляр конфига


config = Config()
