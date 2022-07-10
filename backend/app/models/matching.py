"""Matching related schemas"""

from typing import Optional
from pydantic import BaseModel

class InputMatchingAll(BaseModel):
    """Data class for fuzzy matching."""

    brand : str
    model : str
    releaseYear : int
    fuel : str
    gearbox : str
    mileage : int
    # Using Optional automatically makes the attribute default to None
    doors : Optional[str]
    version : Optional[str]
    carFinishing : Optional[str ]
    horsepower : Optional[str]
    motorization : Optional[str]

    class Config:
        """Config class to change default behavior inherited from BaseModel."""

        anystr_lower = True # Coerces string to lowercase
                            # https://pydantic-docs.helpmanual.io/usage/model_config/

class MockFilters(BaseModel):
    """
    Mock filters model
    (Defined for testing purposes)

    """
    car : dict

DUMMY_CAR = {
    "brand" : "peugeot",
    "model" : "401",
    "releaseYear" : 1934,
    "fuel" : "diesel",
    "gearbox" : "manual",
    "mileage" : 350000
}