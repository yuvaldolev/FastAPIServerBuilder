import uvicorn
from typing import Union

from fastapi import FastAPI


class ServerBuilder:
    def __init__(self) -> None:
        self._app = FastAPI()

    def build(self) -> FastAPI:
        return self._app

    def root(self) -> "ServerBuilder":
        @self._app.get("/")
        def root():
            return {"Hello": "World"}

        return self

    def hello(self) -> "ServerBuilder":
        @self._app.get("/hello/{name}")
        def hello(name: str) -> str:
            return f"Hello, {name}"

        return self


def main() -> None:
    server = ServerBuilder().root().hello().build()
    uvicorn.run(server, host="0.0.0.0", port=5000)


if "__main__" == __name__:
    main()
