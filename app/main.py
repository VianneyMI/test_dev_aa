"""API Entry Point"""

from fastapi import FastAPI
from .routers import pricing, matching

app = FastAPI(
    title = "Aramis Auto Mock API",
    description = "Mock API supporting technical test",
    version="0.1.0",
    port=8000
)

app.include_router(pricing.router)
app.include_router(matching.endpoints.router)

# Root
# ------------------------------------------------------
@app.get("/")
async def root()->dict:
    """Returns a welcome message"""

    return {"message":"Welcome to this mock server"}
