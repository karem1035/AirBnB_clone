#!/usr/bin/python3
"""Defines the city class"""
from models.base_model import BaseModel


class City(BaseModel):
    """user city"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
