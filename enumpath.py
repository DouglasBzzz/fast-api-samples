from enum import Enum

from fastapi import FastAPI

class ModelName(str, Enum):
    pedro = "pedro"
    douglas = "douglas"
    carlos = "carlos"

app = FastAPI()

@app.get("/model/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.pedro:
        return {"model_name": model_name, "message":"esse é o pedro"}

    if model_name.value == "douglas":
        return {"model_name": model_name, "message":"esse é o douglas"}

    return {"model_name":model_name, "message":"sobrou alguém..."}