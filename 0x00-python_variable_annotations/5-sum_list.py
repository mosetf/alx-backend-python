#!/usr/bin/env python3
"""
sums a list of floats and returns their sum as a float
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Sums a list of floats
    Args:
        input_list (list): A list of floats
    Returns:
        float: The sum of the floats in the list
    """
    if input_list is None:
        return 0
    else:
        return sum(input_list)
