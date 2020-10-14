from fastapi import FastAPI

app = FastAPI()

@app.get('/item/{item_id}')
async def read_item(item_id: int): #mudar primeiro para sem a definicao de tipo. tentar passar valores que nao sejam inteiros.
    return {"item_id":item_id}