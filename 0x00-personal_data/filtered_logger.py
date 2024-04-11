#!/usr/bin/env python3
"""Below module filters logs"""
import os
import re
from typing import List


patterns = {
    'extract': lambda x, y: r'(?P<field>{})=[^{}]*'.format('|'.join(x), y),
    'replace': lambda x: r'\g<field>={}'.format(x),
}
PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(
        fields: List[str],
        redaction: str, message: str, separator: str) -> str:
    """Function returns obfuscated log message"""
    extract, replace = (patterns['extract'], patterns['replace'])
    return (re.sub(extract(fields, separator), replace(redaction), message))
