from httpx import ASGITransport, AsyncClient
from asgi_lifespan import LifespanManager
from pytest import fixture


@fixture
async def app():
    from fastapi_slack import with_valid_signature
    from demo import app

    async with LifespanManager(app):
        app.dependency_overrides[with_valid_signature] = lambda: "signature"
        yield app


@fixture
async def client(app):
    async with LifespanManager(app):
        transport = ASGITransport(app=app)
        async with AsyncClient(
            transport=transport, base_url="http://example.local"
        ) as client:
            yield client
