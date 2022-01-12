import numpy as np


def calculate(list_: list):
    if len(list_) != 9:
        raise ValueError('List must contain nine numbers.')
    matrix = np.array(list_).reshape((3, 3))
    functions = {
        'mean': np.mean,
        'variance': np.var,
        'standard deviation': np.std,
        'max': np.max,
        'min': np.min,
        'sum': np.sum,
    }
    axes = [0, 1, None]
    calculations = {}
    for key in functions:
        calculations[key] = []
        array: list = calculations[key]
        for axis_ in axes:
            value = functions[key](matrix, axis=axis_)
            value = list(value) if type(value) == np.ndarray else value
            array.append(value)
    return calculations
