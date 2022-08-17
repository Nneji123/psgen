from fastapi import FastAPI
from passgen.passgen import generate_password
from pydantic import BaseModel


class Password(BaseModel):
    password: int


app = FastAPI()


@app.get('/')
def home():
    return "API is running"


@app.post('/genpass')
async def genpass(data: Password) -> dict:
    text = generate_password(data.password)
    return {"Generated Password": text}
