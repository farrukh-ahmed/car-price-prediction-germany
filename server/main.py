import numpy as np
from fastapi import FastAPI
from server import util
from server.do.DataModel import DataModel, PricePredictionModel
from typing import Dict, List
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/models", response_model= DataModel)
async def get_models():
    util.load_saved_artifacts()
    list = util.get_model_names()
    return DataModel(data=list)



@app.get("/fuel", response_model=DataModel)
async def get_fuel_types():
    util.load_saved_artifacts()
    list = util.get_fuel_type_names()
    return DataModel(data=list)


@app.get("/transmission_type", response_model=DataModel)
async def get_transmission_type():
    util.load_saved_artifacts()
    list = util.get_gear_names()
    return DataModel(data=np.append(list, 'Automatic'))


@app.get("/offerType", response_model=DataModel)
async def get_offerType():
    util.load_saved_artifacts()
    list = util.get_offerType_names()
    return DataModel(data=list)

@app.get("/make",response_model=DataModel)
async def get_makers():
    util.load_saved_artifacts()
    list = util.get_make_names()
    return DataModel(data=list)

@app.post("/predict")
async def predict_price(model : PricePredictionModel):
    util.load_saved_artifacts()
    price = util.get_estimated_price_for_car(model.mileage,model.year,model.make,
                                                   model.model,model.fuel,model.gear,model.offerType)
    data = {
        "data" : {
            "price" : price
        }
    }
    return data

@app.get("/get_all")
async def get_all_data():
    util.load_saved_artifacts()
    model_list = util.get_model_names()
    make_list = util.get_make_names()
    offerType_list = util.get_offerType_names()
    transmission_list = util.get_gear_names()
    fuel_list = util.get_fuel_type_names()
    response : Dict[str, List] = {
        "models": model_list.tolist(),
        "makers": make_list.tolist(),
        "offerTypes": offerType_list.tolist(),
        "transmissions": np.append(transmission_list, 'automatic').tolist(),
        "fuelTypes": fuel_list.tolist()

    }

    return { "data" : response }