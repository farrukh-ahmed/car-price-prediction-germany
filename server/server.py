import json
import pickle
import numpy as np
__models  = None
__make = None
__fuel = None
__gear = None


def seperate_make(make_values):
    return np.array([make.split('_')[1] for make in make_values])
def seperate_models(model_values):
    return np.array([model.split('_')[1] for model in model_values])

def seperate_fuel(fuel_values):
    return np.array([fuel.split('_')[1] for fuel in fuel_values])

def seperate_gear(gear_values):
    gearList = np.array([gear.split('_')[1] for gear in gear_values])
    print(gearList)
    return gearList


def load_saved_artifacts():
    global __data_columns
    global __models
    global __make
    global __fuel
    global __gear

    with open("./artifacts/columns.json",'r') as f:
        __data_columns = json.load(f)['data_columns']
        __make = seperate_make(__data_columns[2:72])
        __models = seperate_models(__data_columns[72:900])
        __fuel = seperate_fuel(__data_columns[900:909])
        __gear = seperate_gear(__data_columns[909:911])


if __name__ == '__main__':
    load_saved_artifacts()