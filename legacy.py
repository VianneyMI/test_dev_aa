"""Pricing back-end, pricing endpoints."""

# pylint: disable=C0103 # Replacing the code (C0103) of the check by its name (invalid-name) would ease the readability of the codebase

import datetime
from pydantic import BaseModel

from fastapi import APIRouter, HTTPException, Response, Request, status # As reported by pylint, the unusued import should be removed
from typing import Dict, List, Optional # As reported by pylint, this import should be on top
from routers import matching

router = APIRouter(
    prefix="/pricing",
    tags=["Pricing"],
    responses={404: {"description": "Not found"}},
)

# It is usually recommended to separate the model from the logic and from the boilerplate code.
# That is, in this case to move the two classes (InputMatchingAll, OutputPricing) definitions below to another module.

class InputMatchingAll(BaseModel):
    """Data class for fuzzy matching."""

    brand : str
    model : str
    releaseYear : int
    fuel : str
    gearbox : str
    mileage : int

    # The definition of the below attributes is not consistent.
    # They are all optional strings, but some default to None others to empty strings.
    # There might be a valid reason to do so, in this case, it would be nice to add a comment to explain the rationale.

    doors : Optional[str] = None
    version : Optional[str] = ""
    carFinishing : Optional[str ] = ""
    horsepower : Optional[str] = None
    motorization : Optional[str] = ""

    class Config: # We should add a docstring for this class or silence the linter
        anystr_lower = True

class OutputPricing(BaseModel):
    """Data class containing output pricing infos"""

    price : float
    # it would be nice to return more information about the prediction
    # for example, the confidence level, and/or a price range


@router.post(
    "./fuzzy-price/linear-reg",
    response_description="Estimate market price",
    response_model=OutputPricing
)
async def estimate_market_price_from_fuzzy_input(
    carMetadata : InputMatchingAll,
    request : Request,
    estimationDate : datetime.date = datetime.datetime.today().date(),
)-> float: # As reported by Pylint, the function is missing a docstring.
            # Unlike the previous example Config class, this docstring is critical to understand the code.
            # The output typehint is a bit misleading as the function actually returns a dictionary

    matching_output = await matching.endpoints.match_all(
        inputMapping=carMetadata,
        request=request,
        matchingDate=estimationDate
    )
    filterCar = matching_output["filters"].car # Do we always have a match ? If not this will break
                                               # It would also break if the outpute does not have a filters key
    output_pricing = {
        "price": filterCar['mileage']*0.8 + (2022-filterCar['releaseYear'])*1.5 + 105000, # it would be better to externalize this statement into a dedicated function
    }
    return output_pricing
