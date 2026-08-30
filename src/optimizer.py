import numpy as np

def compute_cost(X, y, w, b):
    m = X.shape[0]
    predictions = np.dot(X, w) + b
    cost = np.sum((predictions - y) ** 2) / (2 * m)
    return cost

def compute_gradient(X, y, w, b):
    m = X.shape[0]
    predictions = np.dot(X, w) + b
    dj_dw = np.dot(X.T, (predictions - y)) / m
    dj_db = np.sum(predictions - y) / m
    return dj_dw, dj_db
