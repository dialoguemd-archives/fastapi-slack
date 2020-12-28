from time import time

from pytest import raises


def test_with_valid_timestamp():
    from fastapi_slack import with_valid_timestamp

    with_valid_timestamp(int(time()))


def test_with_valid_timestamp_raises_400_when_more_than_30_seconds():
    from fastapi_slack import with_valid_timestamp

    with raises(Exception):
        with_valid_timestamp(int(time() - 40))
