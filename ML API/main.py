from fastapi import FastAPI
import pickle
from pydantic import BaseModel


app = FastAPI()
# For runnning the pickle file to load the ML model you need to install scikit-learn because help unpickel the ML model in its background so before loading pickle model import this package otherwise you will get error 
with open('finalized_model.pkl', 'rb') as f:
  myModel = pickle.load(f)


# Defining the model using pydantics
class Details(BaseModel):
    sepal_length : float
    sepal_width : float
    petal_length : float
    petal_width : float



@app.get('/')
def home_route():
    return {
        "hello": "world"
    }

@app.post("/predict")
async def predict(flowerData : Details):
    p = myModel.predict([[flowerData.sepal_length, flowerData.sepal_width, flowerData.petal_length, flowerData.petal_width]])[0]
    # Here the type of the p is numpy.int32 so we need to convert it to int before parsing this to json
    plantType = ""
    if (int(p) == 0):
        plantType = "setosa"
    elif (int(p) == 1):
        plantType = "versicolor"
    elif (int(p) == 2):
        plantType = "virginica"
    return {"predictions" : plantType}

