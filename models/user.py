#!/usr/bin/python3
"""Class user: subclass of BaseModel"""

from models.base_model import BaseModel


class User(BaseModel):
    """The Class User"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
