#!/usr/bin/env python3
"""Module for auth-related routines"""
import bcrypt
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4

from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """Hashes a password"""
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


def _generate_uuid() -> str:
    """generates a uuid"""
    return str(uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """Initialises new class instance"""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Registers new users to the database"""
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))
        raise ValueError("User {} already exists".format(email))

    def valid_login(self, email: str, password: str) -> bool:
        """Checks if login credentials are valid"""
        user = None
        try:
            user = self._db.find_user_by(email=email)
            if user is not None:
                return bcrypt.checkpw(
                    password.encode("utf-8"),
                    user.hashed_password,
                )
        except NoResultFound:
            return False
        return False
