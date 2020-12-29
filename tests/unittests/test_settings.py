from fastapi import HTTPException
from pytest import fixture, mark, raises

pytestmark = mark.asyncio


@fixture
def missing_variables(monkeypatch):
    monkeypatch.delenv("slack_access_token")
    monkeypatch.delenv("slack_signing_secret")


async def test_on_startup_fails_with_invalid_settings(missing_variables):
    from fastapi_slack import on_startup

    with raises(Exception):
        await on_startup()


async def test_on_startup():
    from fastapi_slack import on_startup

    await on_startup()


async def test_with_settings(settings):
    from fastapi_slack import with_settings

    assert with_settings() == settings


async def test_with_settings_raises_500_with_missing_variables(missing_variables):
    from fastapi_slack import with_settings

    with raises(HTTPException) as raise_info:
        with_settings()

    assert raise_info.value.status_code == 500
