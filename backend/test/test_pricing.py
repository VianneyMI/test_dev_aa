"""Script containing unit test for pricing endpoints"""

import pytest
from fastapi.testclient import TestClient
from hypothesis import given, strategies as st

from backend.app.main import app
from backend.app.models.matching import InputMatchingAll
from backend.app.logic.pricing import DIFFERENTIATION_FACTOR, get_differentiation_factor, get_price

client = TestClient(app)

@pytest.mark.unit
@given(st.builds(InputMatchingAll))
def test_pricing_endpoint(body:InputMatchingAll)->None:
    """Testes the pricing endpoints"""

    response = client.post("/pricing/fuzzy-price/linear-reg", json=body.dict())
    assert response.status_code == 200

@pytest.mark.unit
def test_differentiation_factor()->None:
    """
    Testes that the correct differentiation factor is returned for various test cases

    First and second assertions, ensure a correct value is return for good brand and fuel parameters
    Third and Fourth assertion ensures the brand mapping works as expected
    Fifth assertion ensures an Exception is raised as expected when a bad fuel parameter is received

    """


    other_brand_car = {
        "brand" : "Toyota",
        "fuel" : "essence"
    }

    no_brand_car = {
        "fuel" : "diesel"
    }

    wrong_fuel_car = {
        "brand" : "peugeot",
        "fuel" : "SP"
    }

    assert DIFFERENTIATION_FACTOR["PEUGEOT"]["ESSENCE"] == 1.25
    assert DIFFERENTIATION_FACTOR["RENAULT"]["DIESEL"] == 0.8
    assert get_differentiation_factor(other_brand_car) == 0.8
    assert get_differentiation_factor(no_brand_car) == 1.0

    with pytest.raises(ValueError):
        get_differentiation_factor(wrong_fuel_car)

@pytest.mark.functional
@pytest.mark.latest
def test_pricing_value()->None:
    """Testes that the get_price function returns the correct value"""

    dummy_car = {
        "mileage" : 1,
        "releaseYear" : 2012,
        "brand" : "Unknown",
        "fuel" :"Essence"
    }

    assert get_price(dummy_car) == 8412.64 # Computed manually ....
    # TODO : Create more test cases
