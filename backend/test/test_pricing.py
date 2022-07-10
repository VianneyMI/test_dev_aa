"""Script containing unit test for pricing endpoints"""

from fastapi.testclient import TestClient
from hypothesis import given, strategies as st

from backend.app.main import app
from backend.app.models.matching import InputMatchingAll

client = TestClient(app)

@given(st.builds(InputMatchingAll))
def test_pricing_endpoint(body:InputMatchingAll)->None:
    """Testes the pricing endpoints"""

    response = client.post("/pricing/fuzzy-price/linear-reg", json=body.dict())
    assert response.status_code == 200
