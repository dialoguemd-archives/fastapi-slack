from pytest import fixture


@fixture
def form_data() -> dict:
    # https://api.slack.com/interactivity/slash-commands#app_command_handling
    return {
        "token": "gIkuvaNzQIHg97ATvDxqgjtO",
        "team_id": "T0001",
        "team_domain": "example",
        "enterprise_id": "E0001",
        "enterprise_name": "Globular Construct Inc",
        "channel_id": "C2147483705",
        "channel_name": "test",
        "user_id": "U2147483697",
        "user_name": "Steve",
        "command": "/weather",
        "text": "94070",
        "response_url": "https://hooks.slack.com/commands/1234/5678",
        "trigger_id": "13345224609.738474920.8088930838d88f008e0",
        "api_app_id": "A123456",
    }


def test_slash_commands(settings, form_data):
    from fastapi_slack import with_slash_command

    slash_command = with_slash_command(form_data, "signature")

    assert slash_command.dict() == form_data
