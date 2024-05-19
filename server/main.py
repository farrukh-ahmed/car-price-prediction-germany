import numpy as np
from fastapi import FastAPI
from server import util
from server.do.DataModel import DataModel
app = FastAPI()
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