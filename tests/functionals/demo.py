from fastapi import Depends, FastAPI

from fastapi_slack import SlashCommand, router

app = FastAPI(title="demo")
app.include_router(router)


@app.post("/slack-commands")
def commands(command: SlashCommand = Depends()):
    pass
