from fastapi import Depends, FastAPI

from fastapi_slack import SlashCommand, router, with_slash_command

app = FastAPI(title="demo")
app.include_router(router)


@app.post("/slack-commands")
def commands(command: SlashCommand = Depends(with_slash_command)):
    pass
