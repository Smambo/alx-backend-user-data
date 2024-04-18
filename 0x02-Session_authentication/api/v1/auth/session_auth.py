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

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Returns a User ID based on a session ID"""
        if type(session_id) is str:
            return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None) -> User:
        """Returns a User instance based on cookie value"""
        user_id = self.user_id_for_session_id(self.session_cookie(request))
        return User.get(user_id)

    def destroy_session(self, request=None) -> bool:
        """Deletes user session on logout"""
        sesh_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(sesh_id)

        if (request is None or sesh_id is None) or user_is is None:
            return False
        if sesh_id in self.user_id_by_session_id:
            del self.user_id_by_session_id[sesh_id]
        return True
