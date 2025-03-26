import re
from functools import partial
from typing import Annotated

from pydantic import BeforeValidator


def _validator(value: str) -> str:
    regex = r"^\d{11}$"
    if not re.match(regex, value):
        raise ValueError("Phone number must consist of 11 digits")
    return value

def is_phone(value: str) -> bool:
    try:
        _validator(value)
        return True
    except ValueError:
        return False

Phone = Annotated[
    str,
    BeforeValidator(partial(_validator)),
]
