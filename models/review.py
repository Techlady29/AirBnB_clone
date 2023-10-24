#!/usr/bin/python3
"""This defines the Review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """The class for managing review objects"""
    place_id = ""
    user_id = ""
    text = ""
