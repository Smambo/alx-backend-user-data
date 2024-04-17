#!/usr/bin/env python3
"""Session Auth module for the API"""
from .auth import Auth
from flask import request
from models.user import User
from uuid import uuid4


class SessionAuth(Auth):
    """Session Authentication module"""
    pass
