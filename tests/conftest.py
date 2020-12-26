from unittest.mock import patch

from pytest import fixture


@fixture(autouse=True)
def environ():
    environ = {
        "slack_access_token": "slack-access-token",
        "slack_signing_secret": "slack-signing-secret",
    }
    with patch.dict("os.environ", environ, clear=True):
        yield environ
