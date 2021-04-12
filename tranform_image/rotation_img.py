
import numpy as np

def change_angle_to_radius_unit(angle):
    angle_radius = angle * (np.pi/180)
    return angle_radius

def rotate(src_img,angle_of_rotation,pivot_point,shape_img):

    #1.create rotation matrix with numpy array
    rotation_mat = np.transpose(np.array([[np.cos(angle_of_rotation),-np.sin(angle_of_rotation)],
                            [np.sin(angle_of_rotation),np.cos(angle_of_rotation)]]))
    h,w = shape_img
    
    pivot_point_x =  pivot_point[0]
    pivot_point_y = pivot_point[1]
    
    new_img = np.zeros(src_img.shape,dtype='u1') 

    for height in range(h): #h = number of row
        for width in range(w): #w = number of col
            xy_mat = np.array([[width-pivot_point_x],[height-pivot_point_y]])
            
            rotate_mat = np.dot(rotation_mat,xy_mat)

            new_x = pivot_point_x + int(rotate_mat[0])
            new_y = pivot_point_y + int(rotate_mat[1])


            if (0<=new_x<=w-1) and (0<=new_y<=h-1): 
                new_img[new_y,new_x] = src_img[height,width]

    return new_img

#import cv2
# img = cv2.imread('2.jpg') # import image with cv2
# height,width = img.shape[:2] #get width and height of image
# # start_time = time.time()
# own_rotated = rotate(img.copy(),change_angle_to_radius_unit(-25),(0,0),(height,width))
# # end_time = time.time() - start_time
# # print("all process time: ",end_time)

# #show image
# cv2.imshow("original_img",img)
# cv2.imshow("own_rotate_img",own_rotated)
# cv2.waitKey(0)