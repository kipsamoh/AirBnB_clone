#!/usr/bin/python3
"""
 class that creates the user
"""
from models.base_model import BaseModel


class User(BaseModel):
    """Defines attributes for the user class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
