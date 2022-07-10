"""Pricing back-end, pricing endpoints."""

from datetime import datetime, date

from fastapi import APIRouter, Request

from . import matching
from ..logic.pricing import get_price
from ..models.matching import InputMatchingAll
from ..models.pricing import OutputPricing

router = APIRouter(
    prefix="/pricing",
    tags=["Pricing"],
    responses={404: {"description": "Not found"}},
)


@router.post(
    "./fuzzy-price/linear-reg",
    response_description="Estimate market price",
    response_model=OutputPricing
)
async def estimate_market_price_from_fuzzy_input(
    carMetadata : InputMatchingAll,
    request : Request,
    estimationDate : date = datetime.today().date(),
)->dict:
    """Estimates market price from fuzzy input."""

    matching_output = await matching.endpoints.match_all(
        inputMapping=carMetadata,
        request=request,
        matchingDate=estimationDate
    )
    filterCar = matching_output["filters"].car
    output_pricing = {
        "price": get_price(filterCar)
    }

    return output_pricing
