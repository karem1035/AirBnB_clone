#!/usr/bin/python3
"""Defines the aminity class."""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity of user"""

    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
