import numpy as np

def translate(vertices, tx, ty, tz):
    T = np.array([[1, 0, 0, tx],
                  [0, 1, 0, ty],
                  [0, 0, 1, tz],
                  [0, 0, 0, 1]])
    vertices = np.hstack((vertices, np.ones((vertices.shape[0], 1))))
    return np.dot(vertices, T.T)[:, :-1]

def scale(vertices, sx, sy, sz):
    S = np.array([[sx, 0, 0, 0],
                  [0, sy, 0, 0],
                  [0, 0, sz, 0],
                  [0, 0, 0, 1]])
    vertices = np.hstack((vertices, np.ones((vertices.shape[0], 1))))
    return np.dot(vertices, S.T)[:, :-1]

def rotate(vertices, angle, axis):
    if axis.lower() == 'x':
        R = np.array([[1, 0, 0, 0],
                      [0, np.cos(angle), -np.sin(angle), 0],
                      [0, np.sin(angle), np.cos(angle), 0],
                      [0, 0, 0, 1]])
    elif axis.lower() == 'y':
        R = np.array([[np.cos(angle), 0, np.sin(angle), 0],
                      [0, 1, 0, 0],
                      [-np.sin(angle), 0, np.cos(angle), 0],
                      [0, 0, 0, 1]])
    else:
        R = np.array([[np.cos(angle), -np.sin(angle), 0, 0],
                      [np.sin(angle), np.cos(angle), 0, 0],
                      [0, 0, 1, 0],
                      [0, 0, 0, 1]])
    vertices = np.hstack((vertices, np.ones((vertices.shape[0], 1))))
    return np.dot(vertices, R.T)[:, :-1]
