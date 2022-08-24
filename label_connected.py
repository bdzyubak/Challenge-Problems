import numpy as np
import matplotlib.pyplot as plt

label = 1
connectivity = 4
image = np.array([[1,1,0,0,1,1,0],
            [0,0,0,1,1,1,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [1,1,1,1,1,1,1]])
im_w = image.shape[0]
im_h = image.shape[1]
plt.imshow(image)

def label_image(): 
    global label
    for i in range(im_w): 
        for j in range(im_h): 
            if image[i,j] == 1: 
                label+=1
            label_connected(i,j)
            # New unlabeled cluster
            
    plt.figure()
    plt.imshow(image)

def label_connected(i,j): 
    pixel_needs_labeling = image[i,j] == 1
    if pixel_needs_labeling: 
        print('x: ' + str(i) + ' y: '  + str(j) + ' label: ' + str(label))
        image[i,j] = label
        for neighbors in connected_mask(): 
            x_i = i+neighbors[0]
            x_j = j+neighbors[1]
            location_within_image = (x_i>=0 and x_j>=0) and (x_i<(im_w) and x_j<(im_h))
            if location_within_image: 
                print('x_i: ' + str(x_i) + ' y_i: '  + str(x_j) + ' label_i: ' + str(label))
                label_connected(x_i,x_j)

def connected_mask(): 
    if connectivity == 4: 
        conn_mask = [[-1,0],[0,-1],[1,0],[0,1]]
    else: 
        conn_mask = list()
        for i in [-1,1]: 
            for j in [-1,1]: 
                conn_mask.append([i,j])
    return conn_mask


if __name__ == '__main__': 
    label_image()
    plt.show()