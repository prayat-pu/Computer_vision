
import numpy as np


def Rotation_img(src_img,angle_of_rotation):
    rotation_mat = np.array([[round(np.cos(angle_of_rotation)),round(-np.sin(angle_of_rotation))],
                            [round(np.sin(angle_of_rotation)),round(np.cos(angle_of_rotation))]])
    
    h,w = src_img.shape[:2]
    x_center =  w//2
    y_center = h//2
    
    new_img = np.zeros(src_img.shape,dtype='u1')
    
    for i in range(h):
        for j in range(w):
            # because rotating use r distance from center of rotate
            # you have to find r from current x,y position
            #carefully if you want direction of rotate anticlockwise use x_center - j not(j - x_center image will transform wrong direction -> opposite) 
            #carefully if you want direction of rotate anticlockwise use y_center - i not(i - y_center image will transform wrong direction -> opposite) 
            xy_mat = np.array([x_center - j,y_center - i])
            rotate_mat = np.dot(rotation_mat,xy_mat)

            new_x = x_center+ int(rotate_mat[0])
            new_y =  y_center +int(rotate_mat[1])
            
            if 0<new_x<w and 0<new_y<h:
                new_img[new_y,new_x] = src_img[i,j]

    return new_img
