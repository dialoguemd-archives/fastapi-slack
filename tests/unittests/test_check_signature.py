from pytest import fixture


@fixture
def secret():
    """Valid slack signing secret."""
    return "e33f1fb286333652295f920c461de67d"


@fixture
def timestamp():
    """Valid timestamp."""
    return 1602970682


@fixture
def signature():
    """Valid signature."""
    return "v0=9f214e30377799cf44e680e22991f04147a32bf2434954247728d60304180dc2"


@fixture
def body() -> bytes:
    """Valid slack command body."""
    return (
        b"token=zLKyq9QNyqgGQ3weXwtSov90&team_id=T129F61FC&team_domain=dialoguemd&channe"
        b"l_id=D1V7CLUH3&channel_name=directmessage&user_id=U1V5RS49Z&user_name=hadrien&"
        b"command=%2Fdev-ohs&text=&api_app_id=A01D64BPMTK&response_url=https%3A%2F%2Fhoo"
        b"ks.slack.com%2Fcommands%2FT129F61FC%2F1435644863042%2FgV9qwUtCPGS3AQry7kNLiVsX"
        b"&trigger_id=1428914092678.36321205522.18053fc39d1f89c8bab43fd18ee47ed8"
    )


def test_check_signature(secret, timestamp, signature, body):
    from fastapi_slack import check_signature

    assert check_signature(secret, timestamp, signature, body) is True


def test_check_signature_return_false_on_invalid_signature():
    from fastapi_slack import check_signature

    assert check_signature("secret", 12345, "signature", b"body") is False
