#!/usr/bin/env python3
"""Module for password encryption"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Function hashes a password"""
    return (bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()))
