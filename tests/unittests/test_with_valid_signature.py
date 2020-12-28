from unittest.mock import patch

from fastapi import HTTPException
from pytest import fixture, raises


@fixture
def check_signature():
    with patch("fastapi_slack.check_signature") as check_signature:
        check_signature.return_value = True
        yield check_signature


def test_with_valid_signature(check_signature, settings):
    from fastapi_slack import with_valid_signature

    with_valid_signature(b"b o d y", settings, 12345, "signature")


def test_with_valid_signature_raises_403_when_signature_is_invalid(
    check_signature, settings
):
    from fastapi_slack import with_valid_signature

    check_signature.return_value = False
    with raises(HTTPException) as raise_info:
        with_valid_signature(b"b o d y", settings, 12345, "signature")

    assert raise_info.value.status_code == 403
