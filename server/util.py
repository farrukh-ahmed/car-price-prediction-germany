import json
import pickle
import numpy as np
__models  = None
__make = None
__fuel = None
__gear = None
__model = None
__offer_type = None


def seperate_make(make_values):
    return np.array([make.split('_')[1] for make in make_values])
def seperate_models(model_values):
    return np.array([model.split('_')[1] for model in model_values])

def seperate_fuel(fuel_values):
    return np.array([fuel.split('_')[1] for fuel in fuel_values])

def seperate_gear(gear_values):
    return np.array([gear.split('_')[1] for gear in gear_values])

def seperate_offer_type(offerType_values):
    return np.array([offerType.split('_')[1] for offerType in offerType_values])

def get_estimated_price_for_car(mileage,year,make,model,fuel, gear,offerType):
    make_index = get_the_index_value('make', make)
    model_index = get_the_index_value( 'model', model)
    fuel_index = get_the_index_value( 'fuel', fuel)
    gear_index = get_the_index_value( 'gear', gear)
    offerType_index = get_the_index_value( 'offerType', offerType)
    x = np.zeros(len(__data_columns))
    x[0] = mileage
    x[1] = year
    if make_index >= 0:
        x[make_index] = 1
    if model_index >= 0:
        x[model_index] = 1
    if fuel_index >= 0:
        x[fuel_index] = 1
    if gear_index >= 0:
        x[gear_index] = 1
    if offerType_index >= 0:
        x[offerType_index] = 1

    #return x
    return round(__model.predict([x])[0],2)
def get_the_index_value(col_name, col_value):
    index =  0
    try:
        str = col_name + '_' + col_value
        index = __data_columns.index(str.lower())
    except:
        index = -1
    return index

def load_saved_artifacts():
    global __data_columns
    global __models
    global __make
    global __fuel
    global __gear
    global __model
    global __offer_type

    with open("./artifacts/columns.json",'r') as f:
        __data_columns = json.load(f)['data_columns']
        __make = seperate_make(__data_columns[2:72])
        __models = seperate_models(__data_columns[72:900])
        __fuel = seperate_fuel(__data_columns[900:909])
        __gear = seperate_gear(__data_columns[909:911])
        __offer_type = seperate_offer_type(__data_columns[910:914])

    with open("./artifacts/car_price_prediction.pickle",'rb') as f:
        __model = pickle.load(f)

def get_model_names():
    return __models
def get_gear_names():
    return __gear
def get_fuel_type_names():
    return __fuel
def get_make_names():
    return __make
def get_offerType_names():
    return __offer_type

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_estimated_price_for_car(50000, 2020,'BMW','M5','Gasoline','Manual','Used'))
