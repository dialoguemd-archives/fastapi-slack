# fastapi-slack

[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-brightgreen.svg)](https://conventionalcommits.org)
[![CircleCI](https://circleci.com/gh/dialoguemd/fastapi-slack.svg?style=svg&circle-token=d5088d3188d29980a98d21136927b0693ea7d90e)](https://circleci.com/gh/dialoguemd/fastapi-slack)
[![codecov](https://codecov.io/gh/dialoguemd/fastapi-slack/branch/master/graph/badge.svg?token=CVU9WOYOEG)](https://codecov.io/gh/dialoguemd/fastapi-slack)

Slack extension for FastAPI.

## Configuration - Environment Variables

### `slack_access_token`

Bot User OAuth Access Token as defined in OAuth & Permissions menu of the slack app.

### `slack_signing_secret`

App signing secret as shown in Basic Information menu of the slack app in the App
Credentials section.

## Setup

* Include fastapi-slack router:

```python
import fastapi_slack
from fastapi import FastAPI


app = FastAPI()
app.include_router(fastapi_slack.router)
```

## [Slash Commands]

* Depending on `fastapi_slack.SlashCommand` automatically validates Slack request
  signature and extract the info needed to process it:

```python
from fastapi import Depends, FastAPI
from fastapi_slack import SlashCommand, router

app = FastAPI()
app.include_router(router)


@app.post("/slash-commands")
def process_commands(slash_command: SlashCommand = Depends()):
    pass
```


[Slash Commands]: https://api.slack.com/interactivity/slash-commands
