from fastapi import FastAPI
from routes.index import trends


app = FastAPI(
    title="Trends APIs",
    description="This apis will return trending data related to Green Hydrogen",
)
app.include_router(trends)
