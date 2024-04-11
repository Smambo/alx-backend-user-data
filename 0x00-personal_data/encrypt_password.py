#!/usr/bin/env python3
"""Module for password encryption"""

import bcrypt


def hash_password(password: str) -> bytes:
    """Function hashes a password"""
    return (bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()))


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Function checks if given password is hashed"""
    return (bcrypt.checkpw(password.encode('utf-8'), hashed_password))
