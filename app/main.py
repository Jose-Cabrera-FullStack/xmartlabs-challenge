from fastapi import FastAPI

from app.database.config import database
from app.routers import restful_endpoints, rest_endpoints

API_VERSION = "v1"

app = FastAPI(
    title="API Name",
    description="API description",
    version=API_VERSION,
    docs_url="/",
)

app.include_router(restful_endpoints.router)
app.include_router(rest_endpoints.router)

@app.on_event("startup")
async def startup():
    if not database.is_connected:
        await database.connect()

@app.on_event("shutdown")
async def shutdown():
    if database.is_connected:
        await database.disconnect()
