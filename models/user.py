#!/usr/bin/python3
"""Module for the User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class representing a User"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
