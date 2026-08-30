import numpy as np

def get_stats(X):
    n = len(X)
    x = X.mean()
    s = X.std(ddof=1)
    return (n, x, s)

def degrees_of_freedom(s_c, n_c, s_v, n_v):
    s_v_n_v = (s_v ** 2) / n_v
    s_c_n_c = (s_c ** 2) / n_c
    numerator = (s_c_n_c + s_v_n_v) ** 2
    denominator = ((s_c_n_c ** 2) / (n_c - 1)) + ((s_v_n_v ** 2) / (n_v - 1))
    return numerator / denominator
