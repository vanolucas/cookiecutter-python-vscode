from fastapi import FastAPI

app = FastAPI()


@app.get("/echo")
def echo(msg: str) -> str:
    return msg
