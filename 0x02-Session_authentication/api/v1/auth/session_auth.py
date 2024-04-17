#!/usr/bin/env python3
"""Session Auth module for the API"""
from .auth import Auth
from flask import request
from models.user import User
from uuid import uuid4


class SessionAuth(Auth):
    """Session Authentication module"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates a Session ID for a user_id"""
        if type(user_id) is str:
            session_id = str(uuid4())
            self.user_id_by_session_id[session_id] = user_id
            return session_id
