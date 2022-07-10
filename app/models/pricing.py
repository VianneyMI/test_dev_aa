"""Pricing related schemas"""

from pydantic import BaseModel

class OutputPricing(BaseModel):
    """Data class containing output pricing infos"""

    price : float
