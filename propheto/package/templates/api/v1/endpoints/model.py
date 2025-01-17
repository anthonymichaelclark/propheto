import pickle
import boto3
from fastapi import APIRouter
from typing import Optional, List
from pydantic import BaseModel
from datetime import datetime
from time import time
import json
from .logs import create_log

router = APIRouter()


class ModelsResponse(BaseModel):
    Key: str
    LastModified: datetime
    ETag: str
    Size: int
    StorageClass: str
    Owner: dict


class Response(BaseModel):
    code: int
    message: str
    result: dict


def get_deserialize_model():
    model = object
    # %{model_serializer}%
    return model


@router.get("/models/", response_model=List[ModelsResponse])
def get_models(model_name: Optional[str] = "current"):
    s3client = boto3.client("s3")
    delimiter = f"{model_name}*" if model_name != "current" else "*"
    response = s3client.list_objects(Bucket="%{bucket_name}%", Delimiter=delimiter)
    return response["Contents"]


async def log_prediction(data):
    js_data = {}
    created_at = datetime.fromtimestamp(time()).isoformat()
    js_data["created_at"] = created_at
    js_data["data"] = data
    filename = f"predictions/predict-{created_at}.json"
    await create_log(filename=filename, filedata=json.dumps(js_data))


@router.post("/models/predict", response_model=Response)
async def get_prediction(data: List):
    pred = [0]
    model = get_deserialize_model()
    print("Deserialized model")
    print(model)
    print("Data is")
    print(data)
    # preprocess data
    # %{model_preprocessor}%
    # predict from model
    # %{model_predictor}%
    # postprocessor for data
    # %{model_postprocessor}%
    response = {"prediction": pred}
    log_response = {"prediction": pred, "data": data}
    await log_prediction(log_response)
    return Response(code=200, message="Success", result=response)


@router.post("/models/{model_name}", response_model=Response)
def set_model_api(model_name: str):
    s3client = boto3.client("s3")
    return Response(code=200, message="Success", result="test")

