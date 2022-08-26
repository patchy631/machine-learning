import json
import joblib
from azureml.core import Model


def init():
    global model
    model_name = "irisclassifier"
    path = Model.get_model_path(model_name)
    model = joblib.load(path)


def run(data):
    try:
        data = json.loads(data)
        result = model.predict(data["data"])
        return {"data": result.tolist(), "message": "Prediction successful"}
    except Exception as e:
        return {"data": e, "message": "Failed to predict"}
