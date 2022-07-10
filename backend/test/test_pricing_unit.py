"""Script containing unit test for pricing endpoints"""

from fastapi.testclient import TestClient
from hypothesis import given, strategies as st

from ..app.main import app
from ..app.models.matching import InputMatchingAll

client = TestClient(app)

@given(st.builds(InputMatchingAll))
def test_pricing_endpoint(body:InputMatchingAll):
    """Testes the pricing endpoints"""

    response = client.post("/fuzzy-price/linear-reg", json=body.json())
    assert response.status_code == 200
