#!/usr/bin/python3
"""
Defines city attribute
"""
from models.base_model import BaseModel


class City(BaseModel):
    """defines the city to pick from"""
    state_id = ""
    name = ""
