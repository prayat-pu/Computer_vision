import numpy

def speedUp_translation_img2(src_img,shift_distance,shape_of_out_img):
    h,w = src_img.shape[:2]
    x_distance = shift_distance[0]
    y_distance = shift_distance[1]
    ts_mat = np.array([[1,0,x_distance],[0,1,y_distance]])
    
    out_img = np.zeros(shape_of_out_img,dtype='u1')
    
    origin_x = 0
    origin_y = 0
    origin_xy = np.array([origin_x,origin_y,1])
    
    new_xy = np.dot(ts_mat,origin_xy)
    new_x = new_xy[0]
    new_y = new_xy[1]
    
    if 0 < new_x < w and 0 < new_y < h:
        out_img[new_y:,new_x:]  = src_img[origin_y:h-new_y,origin_x:w-new_x]
    elif new_x < 0 and new_y >= 0:
        out_img[new_y:,:new_x] = src_img[origin_y:h-new_y,:new_x]
    elif new_y < 0 and new_x >=0:
        out_img[:new_y,new_x:] = src_img[origin_y:new_y,origin_x:w-new_x]
    elif new_y <  0 and new_x <0:
        out_img[:new_y,:new_x] = src_img[origin_y:new_y,:new_x]

    return out_img
