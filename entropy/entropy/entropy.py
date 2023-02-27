"""
Implements the entropy algorithm for a probability distribution.

Functions:
entropy: calculates the entropy of a probability distribution.
"""


import numbers

import numpy as np

    
def entropy(probabilities):
    """
    Calculates the entropy of a probability distribution.

    Parameters:
    probabilities (list of numbers): the probability distribution to
    find the entropy of.

    Returns:
    number: the entropy of the list of numbers

    Raises:
    ValueError if any of the values in the probability list are not
    numbers, are negative, or if the probabilities in the list do not
    sum to 1 (ie are not a real probability distribution).
    """
    if any(not isinstance(p_i, numbers.Number) for p_i in probabilities):
        raise ValueError("At least one input is not a number")
    if any((p_i < 0.0) or (p_i > 1.0) for p_i in probabilities):
        raise ValueError("At least one input is out of range [0...1]")
    if not np.isclose(1, np.sum(probabilities), atol=1e-08):
        raise ValueError("The list of input probabilities does not sum to 1")

    items = []
    for p_i in probabilities:
        if p_i > 0:
            interm = p_i * np.log2(p_i)
            items.append(interm)
    return np.abs(-np.sum(items))
