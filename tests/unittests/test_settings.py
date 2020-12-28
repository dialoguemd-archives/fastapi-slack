from pytest import mark, raises

pytestmark = mark.asyncio


async def test_on_startup_fails_with_invalid_settings(monkeypatch):
    from fastapi_slack import on_startup

    monkeypatch.delenv("slack_access_token")
    monkeypatch.delenv("slack_signing_secret")
    with raises(Exception):
        await on_startup()


async def test_on_startup():
    from fastapi_slack import on_startup

    await on_startup()


async def test_with_settings(settings):
    from fastapi_slack import with_settings

    assert with_settings() == settings
