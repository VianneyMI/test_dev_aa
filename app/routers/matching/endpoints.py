"""Matching back-end, matching endpoints."""

# pylint: disable=unused-import

from datetime import datetime, date

from fastapi import Request

from ...models.matching import InputMatchingAll

async def match_all(
    inputMapping : InputMatchingAll,
    request : Request,
    matchingDate : date
) -> dict:
    """Returns the closest matching car in the database ?"""

    raise NotImplementedError
