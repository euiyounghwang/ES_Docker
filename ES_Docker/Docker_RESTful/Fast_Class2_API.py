
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    return item


if __name__ == "__main__":
    """
    # Python Main
    uvicorn.run(app="main:app", 
                host="0.0.0.0",
                port=80,
                reload=True,
                workers=4) 

    # Command                
    uvicorn main:app --reload --host=0.0.0.0 --port=80 --workers=4
    """
    uvicorn.run("Fast_Class2_API:app", host="127.0.0.1", port=1237, log_level="info")