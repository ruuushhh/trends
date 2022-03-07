from fastapi import APIRouter
from api.index import all_data_to_csv


trends = APIRouter()


@trends.get("/get_trend", tags=["Trends Data"])
async def get_trend():
    response = all_data_to_csv()
    response.headers["Content-Disposition"] = "attachment; filename=data.csv"
    return response
