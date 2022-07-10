"""Module containing the business logic for the pricing"""

from datetime import datetime

MILEAGE_COEFF = 0.8
AGE_COEFF = 1.5
ORIGIN = 10500
CURRENT_YEAR = datetime.today().year

def get_price(car:dict)->float:
    """Makes a price estimation of car based on its 'mileage' and its 'age'."""

    return car['mileage']*MILEAGE_COEFF + (CURRENT_YEAR-car['releaseYear'])*AGE_COEFF + ORIGIN
