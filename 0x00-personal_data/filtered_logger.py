#!/usr/bin/env python3
"""Below module filters logs"""
import logging
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


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    FORMAT_FIELDS = ("name", "levelname", "asctime", "message")
    SEPARATOR = ";"

    def __init__(self, fields: List[str]) -> None:
        """Initialises class"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Formats the log record."""
        message = super(RedactingFormatter, self).format(record)
        text = filter_datum(
            self.fields,
            self.REDACTION,
            message,
            self.SEPARATOR,
        )
        return (text)
