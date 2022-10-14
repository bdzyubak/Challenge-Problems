import numpy as np
import matplotlib.pyplot as plt
import time

label = 1
connectivity = 4
image = np.array([[1,1,0,0,1,1,0],
            [0,0,0,1,1,1,0],
            [1,0,0,0,0,0,1],
            [1,0,0,1,0,0,1],
            [1,0,1,1,1,0,1],
            [0,0,0,0,0,0,0],
            [1,1,1,1,1,1,1]])
im_w = image.shape[0]
im_h = image.shape[1]

def label_image(): 
    global image, label
    plot(image)
    for i in range(im_w): 
        for j in range(im_h): 
            if image[i,j] == 1: 
                label+=1
            label_connected(i,j)
            # New unlabeled cluster
    
    # Shift labels to start at 1
    image = image-1
    image[image<0] = 0
    
    return image

def label_connected(i,j): 
    pixel_needs_labeling = image[i,j] == 1
    if pixel_needs_labeling: 
        # print('x: ' + str(i) + ' y: '  + str(j) + ' label: ' + str(label))
        image[i,j] = label
        for neighbors in connected_mask(): 
            x_i = i+neighbors[0]
            x_j = j+neighbors[1]
            location_within_image = (x_i>=0 and x_j>=0) and (x_i<(im_w) and x_j<(im_h))
            if location_within_image: 
                # print('x_i: ' + str(x_i) + ' y_i: '  + str(x_j) + ' label_i: ' + str(label))
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

def plot(img): 
    plt.figure()
    plt.imshow(img)

if __name__ == '__main__': 
    labeled_image = np.array([[1,1,0,0,2,2,0],
            [0,0,0,2,2,2,0],
            [3,0,0,0,0,0,4],
            [3,0,0,5,0,0,4],
            [3,0,5,5,5,0,4],
            [0,0,0,0,0,0,0],
            [6,6,6,6,6,6,6]])
    
    start_time = time.time()
    label_image()
    run_time = time.time() - start_time
    print('The run time was: ' + str(run_time))
    label_image()
    plot(image)
    plt.show()
    assert (image == labeled_image).all(), 'Image labeled incorrectly'
    print('Done')