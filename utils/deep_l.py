import numpy as np


def sigmoid_activation(x):
    return 1. / (1. + np.exp(-x))


def tanh_activation(x):
    return np.tanh(x)
