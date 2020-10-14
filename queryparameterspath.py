from fastapi import FastAPI
from typing import Optional

app = FastAPI()

itens_falsos_db = [{"item_name":"item 1"}, {"item_name":"item 2"}, {"item_name":"item 3"}]

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return itens_falsos_db[skip: skip+limit]

@app.get("/item/{item_id}")
async def read_item_one(item_id: str, q: Optional[str] = None, short: bool = False):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id":item_id}

@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
        user_id: int, item_id: str, q: Optional[str] = None, short: bool = False
):
    item = {"item_id":item_id, "usuario_id":user_id}
    if q:
        item.update({"q":q})
    if not short:
        item.update(
            {"descricao":"essa é uma descricao enorme de um item topissimo"}
        )
    return item

@app.get("/items/{item_id}")
async def read_user_item_two(item_id: str, needy: str):
    item = {"item_id":item_id, "needy":needy}
    return item

@app.get("/itemsoptional/{item_id}")
async def read_user_item(
        item_id: str, needy: str, skip: int = 0, limit: Optional[int] = None
):
    item = {"item_id": item_id, "needy": needy, "skip":skip, "limit":limit}
    return item