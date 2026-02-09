import logging
import os
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv
from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict
from appium.options.android import UiAutomator2Options

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)



class AppiumSettings(BaseSettings):
    """Конфигурация Appium на Pydantic Settings."""

    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        extra='ignore',
    )

    context: str = Field(..., alias='CONTEXT', description='Контекст окружения')
    remote_url: str = Field('', alias='REMOTE_URL')
    device_name: Optional[str] = Field(None, alias='DEVICE_NAME')
    platform_name: str = Field('Android', alias='PLATFORM_NAME')
    platform_version: str = Field('13.0', alias='PLATFORM_VERSION')
    automation_name: str = Field('UiAutomator2', alias='AUTOMATION_NAME')
    app_wait_activity: str = Field('org.wikipedia.*')
    app: str = Field('apps/app-alpha-universal-release.apk', alias='app')

    @field_validator('remote_url')
    @classmethod
    def clean_remote_url(cls, v: str) -> str:
        return v.rstrip('/') if v else v

    @field_validator('app')
    @classmethod
    def resolve_app_path(cls, v: str) -> str:
        if v.startswith(('http://', 'https://')):
            return v
        path = Path(v)
        if not path.is_absolute():
            path = Path.cwd() / path
        return str(path)

    def to_driver_options(self) -> UiAutomator2Options:
        """Собирает UiAutomator2Options из текущих настроек."""
        return to_driver_options(self)


def load_config() -> AppiumSettings:
    """Загружает конфигурацию из .env и .env.{context}."""
    load_dotenv()
    context = os.getenv("CONTEXT")
    if not context:
        raise RuntimeError("CONTEXT is not set")
    load_dotenv(f".env.{context}")
    return AppiumSettings()


def to_driver_options(config: Optional[AppiumSettings] = None) -> UiAutomator2Options:
    """Собирает UiAutomator2Options из конфига. Если config не передан — загружается через load_config()."""
    if config is None:
        config = load_config()
    options = UiAutomator2Options()
    logger.info(config.context)
    logger.info(config.remote_url)
    if config.device_name:
        options.set_capability('deviceName', config.device_name)
    logger.info(config.device_name)
    if config.app_wait_activity:
        options.set_capability('appWaitActivity', config.app_wait_activity)
    options.set_capability('appium:appPackage', 'org.wikipedia.alpha')
    options.set_capability('appium:appActivity', 'org.wikipedia.main.MainActivity')
    options.set_capability('app', config.app)
    return options
