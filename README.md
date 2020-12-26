# fastapi-slack

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
