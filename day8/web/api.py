from typing import Union, Optional, List, Any, Dict
from fastapi import FastAPI
from pydantic import BaseModel
import json


# Serializador de saída
class PersonOut(BaseModel):
    id: int
    name: str
    picture: str
    age: int
    email: str
    about: Optional[str] = ""
    is_active: bool


app = FastAPI()


@app.get("/", response_model=List[PersonOut])
async def read_root(is_active: Optional[str] = None):
    if is_active is not None:
        is_active = is_active.lower() == "true"

    return get_pessoas(is_active=is_active)


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


def get_pessoas(is_active=None) -> List[Dict[str, Any]]:
    with open("data.json") as datafile:
        data = json.loads(datafile.read())

    if is_active is not None:
        return [
            pessoa for pessoa in data
            if pessoa["is_active"] == is_active
        ]

    return data
