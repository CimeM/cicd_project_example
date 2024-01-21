import uuid
from typing import Optional
from pydantic import BaseModel, Field
from decimal import Decimal

class Landmark(BaseModel):
    id:     str = Field(default_factory=uuid.uuid4, alias="_id")
    name:   str = Field(...)
    type:   str = Field(...)
    tags:   str = Field(...)
    published:      bool    = Field(...)
    
    descriptions:   str     = Field(...)
    images:         str     = Field(...)
    landmarks:      str     = Field(...)
    
    position_lng:   str = Field(...)
    position_lat:   str = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "",
                "name": "Tour eiffel",
                "type": "landmark",
                "tags": "view,tower",
                "published": False,
                "descriptions": "",
                "images": "",
                "landmarks": "", #["_id","_id"]
                "position_lng": "3.14",
                "position_lat": "3.14" 
            }
        }


class LandmarkUpdate(BaseModel):
    name: Optional[str]
    type: Optional[str]
    tags: Optional[str]
    published: Optional[str]
    descriptions: Optional[str]
    images: Optional[str]
    landmarks: Optional[str]
    position_lng: Optional[str]
    position_lat: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "name": "Tour eiffel",
                "type": "landmark",
                "tags": "view,tower",
                "published": False,
                "descriptions": "",
                "images": "",
                "landmarks": "",
                "position_lng": "3.14",
                "position_lat": "2.71" 
            }
        }