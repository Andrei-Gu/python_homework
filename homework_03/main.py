import json
import os

from fastapi import FastAPI, Response, status, HTTPException
from views.users import router as users_router


app = FastAPI()
app.include_router(users_router)


@app.get("/")
def read_root():
    return Response(
        content=json.dumps({"hello": "root"}),
        media_type="application/json"
    )


@app.get("/hello")
def hello(name: str | None = None):
    if name is None:
        name = "Lord"
    return {
        "message": f"Hello {name}!"
    }


@app.get("/sensitive")
def get_sensitive(parameter: str | None = None):
    if parameter is None:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT
        )
    return {
        parameter: os.getenv(parameter, f"Parameter '{parameter}' not found!")
    }


@app.get("/ping", status_code=status.HTTP_200_OK)
def ping_pong():
    return Response(
        content=json.dumps({"message": "pong"}),
        media_type="application/json"
    )
