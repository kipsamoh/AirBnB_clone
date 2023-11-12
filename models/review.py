#!/usr/bin/python3
"""
Defines review class as an attribute
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Reviews by users about a cetain specific place"""
    place_id = ""
    user_id = ""
    text = ""
