#!/usr/bin/python3
"""Define the stateclass"""
from models.base_model import BaseModel


class State(BaseModel):
    """state of the user"""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
