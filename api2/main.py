from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import dotenv_values
from pymongo import MongoClient
from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder

import os
from typing import List

from models import Landmark, LandmarkUpdate
# from router_landmark import router as landmark_router

# config = dotenv_values(".env")

router = APIRouter()

app = FastAPI()

origins = [
    "http://localhost:8100",
    "http://app.localhost",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_origin_regex='https://.*\.localhost',
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def main():
    return {"message": "Hello World"}

@app.get("/landmark", response_description="List all landmarks", response_model=List[Landmark])
def list_landmarks(request: Request):
    landmarks = list(request.app.database["landmarks"].find(limit=100))
    return landmarks

@app.post("/landmark", response_description="Create a new landmark", status_code=status.HTTP_201_CREATED, response_model=Landmark)
def create_landmark(request: Request, landmark: Landmark = Body(...)):
    landmark = jsonable_encoder(landmark)
    new_landmark = request.app.database["landmarks"].insert_one(landmark)
    created_landmark = request.app.database["landmarks"].find_one(
        {"_id": new_landmark.inserted_id}
    )

    return created_landmark

@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(os.environ["ATLAS_URI"])
    app.database = app.mongodb_client[os.environ["DB_NAME"]]

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()