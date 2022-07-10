"""Module containing the business logic for the pricing"""

from typing import Dict
from datetime import datetime

MILEAGE_COEFF = 0.8
AGE_COEFF = 1.5
ORIGIN = 10500
CURRENT_YEAR = datetime.today().year

DIFFERENTIATION_FACTOR : Dict[str, Dict[str, float]] ={
    "PEUGEOT":{
        "ESSENCE":125.0/100,
        "DIESEL":100.0/100 # guess as the value was not provided
    },
    "RENAULT":{
        "DIESEL":80.0/100,
        "ESSENCE":100.0/100
    },
    "OTHER":{
        "ESSENCE":80.0/100,
        "DIESEL":100.0/100
    }
}

def get_price(car:dict)->float:
    """Makes a price estimation of car based on its 'mileage' and its 'age'."""

    return (car['mileage']*MILEAGE_COEFF + (CURRENT_YEAR-car['releaseYear'])*AGE_COEFF + ORIGIN)*DIFFERENTIATION_FACTOR[_get_brand_df(car)][_get_fuel_df(car)]

def _get_brand_df(car:dict)->str:
    """Returns the brand name of a car mapped to the options available in DIFFERENTIATION_FACTOR"""

    brand:str = car.get("brand", "").upper() # Given InputMatchingAll, I assume the brand info is always available
                                         # however, using get is safer
                                         # Using "" as a default helps mypy understands that the output will be a string

    # To prevent KeyErrors (and also to map all other brands to OTHER)
    if brand not in DIFFERENTIATION_FACTOR:
        brand = "OTHER"

    return brand

def _get_fuel_df(car:dict)->str:
    """Returns the fuel type of car mapped to the options available in DIFFERENTIATION_FACTOR"""

    fuel:str = car.get("fuel", "").upper()

    # To prevent KeyErrors
    if fuel not in ["ESSENCE", "DIESEL"]:
        raise ValueError(f"Expected ESSENCE or DIESEL for fuel type. Received {fuel}")

    return fuel
