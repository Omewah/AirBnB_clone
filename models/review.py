#!/usr/bin/python3
"""Review module: subclass of BaseModel"""

from models.base_model import BaseModel


class Review(BaseModel):
    """The Review model"""
    place_id = ""
    user_id = ""
    text = ""
