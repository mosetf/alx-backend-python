#!/usr/bin/env python3
"""Module containing function safely_get_value"""
from typing import Mapping, Any, Union, TypeVar, Optional

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Optional[T] = None) -> Union[Any, T]:
    """
    Safely gets value from dictionary.
    Args:
        dct (dict): Dictionary to get value from.
        key (str): Key to get value from.
        default (any): Default value to return if key is not found.
    Returns:
        Value from dictionary.
    """
    if key in dct:
        return dct[key]
    else:
        return default
