from unittest.mock import AsyncMock

from fastapi import Request
from pytest import mark

pytestmark = mark.asyncio


async def test_with_body():
    from fastapi_slack import with_body

    request = AsyncMock(spec=Request)
    request.body.return_value = b"b o d y"

    assert await with_body(request) == b"b o d y"
