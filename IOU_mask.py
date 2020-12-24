import numpy as np

def iou_mask(mat_1, mat_2):
    # pass
    intersection = mat_1 * mat_2
    # return intersection
    union = np.clip(mat_1 + mat_2, 0, 1)
    return np.sum(intersection) / np.sum(union)


if __name__ == '__main__':
    mat_1 = np.array([
        [0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ])

    mat_2 = np.array([
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 0],
        [0, 0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ])

    print(iou_mask(mat_1, mat_2))
