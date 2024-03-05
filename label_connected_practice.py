import numpy as np
import matplotlib.pyplot as plt
import time

label = 1
connectivity = 4
image = np.array([[1, 1, 0, 0, 1, 1, 0],
                  [0, 0, 0, 1, 1, 1, 0],
                  [1, 0, 0, 0, 0, 0, 1],
                  [1, 0, 0, 1, 0, 0, 1],
                  [1, 0, 1, 1, 1, 0, 1],
                  [0, 0, 0, 0, 0, 0, 0],
                  [1, 1, 1, 1, 1, 1, 1]])

rows = image.shape[0]
columns = image.shape[1]


def label_image():
    counter = 0
    labeled_image = np.zeros_like(image)
    for r in range(rows):
        for c in range(columns):
            if image[r, c] > 0:
                if labeled_image[r, c] == 0:
                    counter += 1
                labeled_image = label_neighborhood(image, labeled_image, r, c, counter)
    return labeled_image


def label_neighborhood(image, labeled_image, r, c, counter):
    # Already labeled, or does not need labeling
    out_of_bounds = r < 0 or c < 0 or r > (rows - 1) or c > (columns - 1)
    if out_of_bounds: return labeled_image
    doesnt_need_label = image[r, c] == 0 or labeled_image[r, c] > 0
    if doesnt_need_label: return labeled_image
    labeled_image[r, c] = counter
    for neighbors in connect_mask():
        rn = r + neighbors[0]
        cn = c + neighbors[1]
        labeled_image = label_neighborhood(image, labeled_image, rn, cn, counter)
    return labeled_image


def connect_mask():
    if connectivity == 4:
        conn_mask = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    else:
        raise (ValueError('Valid connectivities are 4 and 8 in 2D. Only 4 is supported at this time.'))
    return conn_mask


def plot(img):
    plt.figure()
    plt.imshow(img)


if __name__ == '__main__':
    labeled_image_correct = np.array([[1, 1, 0, 0, 2, 2, 0],
                                      [0, 0, 0, 2, 2, 2, 0],
                                      [3, 0, 0, 0, 0, 0, 4],
                                      [3, 0, 0, 5, 0, 0, 4],
                                      [3, 0, 5, 5, 5, 0, 4],
                                      [0, 0, 0, 0, 0, 0, 0],
                                      [6, 6, 6, 6, 6, 6, 6]])
    start_time = time.time()
    labeled_image_result = label_image()
    run_time = time.time() - start_time
    print('The run time was: ' + str(run_time))
    plot(labeled_image_result)
    # plt.show()
    assert (labeled_image_result == labeled_image_correct).all(), 'Image labeled incorrectly'
    print('Done')
