from fastapi import APIRouter
from pkg_resources import get_distribution
from pydantic import BaseSettings, SecretStr, ValidationError

__all__ = ["router"]
__version__ = get_distribution("fastapi-slack").version
router = APIRouter()


class Settings(BaseSettings):
    access_token: SecretStr
    signing_secret: SecretStr

    class Config:
        env_prefix = "slack_"


@router.on_event("startup")
async def on_startup():
    try:
        Settings()
    except ValidationError as error:
        raise Exception("Missing environment variable(s)") from error
