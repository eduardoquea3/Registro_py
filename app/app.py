from fastapi import FastAPI
from .routes import User
app = FastAPI()

app.include_router(User.app)


@app.get("/", tags=["root"])
def read_root():
    return {"Bienvenido": "a nuestra API"}
