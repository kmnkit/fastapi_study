import uvicorn
from datetime import datetime
from fastapi import FastAPI
from typing import Optional, List
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    id: int
    name = "John Doe"
    signup_ts: Optional[datetime] = None
    friends: List[int] = []


external_data = {
    "id": 123,
    "signup_ts": "2019-06-01 12:22",
    "friends": [1, 2, "3"],
}
user = User(**external_data)
print(user.id)
print(repr(user.signup_ts))
print(user.friends)
print(user.dict())


@app.get("/")
def hello():
    return "Hello, World!"


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
