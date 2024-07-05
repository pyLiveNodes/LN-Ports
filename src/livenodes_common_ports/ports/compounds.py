import numpy as np

from livenodes.components.port import Port
from .primitives import Port_Any

# === Compounds ========================================================

# TODO: consider if it really makes sense to mix lists and arrays...
class Port_List(Port):
    example_values = []
    compound_type = Port_Any

    @classmethod
    def example_compound_construction(cls, compounding_value):
        return [compounding_value]

    @classmethod
    def check_value(cls, value):
        if not (type(value) == list or isinstance(value, np.ndarray)):
            return False, f"Should be list; got {type(value)}, val: {value}."
        if len(value) > 0:
            return cls.compound_type.check_value(value[-1])
        return True, None


def has_duplicates(iterable):
    # origianlly used set(), but that prohibits unhashable items, which can still be compared via reference (ie nested lists)
    seen = []
    for x in iterable:
        if x in seen:
            return True
        seen.append(x)
    return False

class Port_ListUnique(Port):
    example_values = [
        ["EMG1", "EMG2"],
        [0, 1],
        [20, .1]
    ]
    compound_type = Port_Any

    @classmethod
    def example_compound_construction(cls, compounding_value):
        return [compounding_value]

    @classmethod
    def check_value(cls, value):
        if (type(value) != list):
            return False, f"Should be list; got {type(value)}, val: {value}."
        if has_duplicates(value):
            return False, "There should not be any duplicates;"
        if len(value) > 0:
            return cls.compound_type.check_value(value[-1])
        return True, None


class Port_Dict(Port):

    example_values = [
        {},
        {'name': 'f', 'va': 5}
    ]

    def __init__(self, name='Meta'):
        super().__init__(name)

    @classmethod
    def check_value(cls, value):
        if type(value) != dict:
            return False, f"Should be dict; got {type(value)}, val: {value}."
        return True, None


class Port_np_compatible(Port):
    example_values = [
        1,
        [-1, 2],
        -0.5,
        np.array([[1]]),
        np.array([[[1, 2], [3, 4]]])
    ]

    @classmethod
    def check_value(cls, value):
        try:
            arr = np.array(value)
            if not np.issubdtype(arr.dtype, np.number):
                return False, "Numpy array is not numerical"
        except Exception as err:
            print(err)
            return False, "Could not convert to numpy array"
        return True, None
