from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

#@app.get("/items/{item_id}")
#async def root(item_id):
#    return {"item_id": item_id}

#@app.get("/items/{item_id}")
#async def root(item_id:int):
#    return {"item_id": item_id}

#query parameters

#fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

#@app.get("/items/")
#async def read_item(skip: int = 0, limit: int = 10):
#    return fake_items_db[skip : skip + limit]


#optional parameters
#@app.get("/items/{item_id}")
#async def read_item(item_id: str, q: str | None = None):
#    if q:
#        return {"item_id": item_id, "q": q}
#    return {"item_id": item_id}


""" @app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item
#test http://127.0.0.1:8000/items/foo?q=testq """

@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: str | None = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item