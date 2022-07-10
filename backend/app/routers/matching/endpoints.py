"""Matching back-end, matching endpoints."""

# pylint: disable=unused-import

from datetime import datetime, date

from fastapi import Request, APIRouter

from ...models.matching import InputMatchingAll, MockFilters, DUMMY_CAR

router = APIRouter(tags=["matchiing"])
@router.post("/matching")
async def match_all(
    inputMapping : InputMatchingAll,
    request : Request,
    matchingDate : date
) -> dict:
    """Returns the closest matching car in the database ?"""

    return {
        "filters": MockFilters(car=DUMMY_CAR)
    }
