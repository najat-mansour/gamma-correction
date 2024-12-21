from helpers import *

import cv2 as cv
import numpy as np 

class GammaCorrection:
    def __init__(self, img):
        self.gamma = RandomNumberGenerator.generate_random_number()
        self.c = Constants.MAX_GRAY_LVL.value / (Constants.MAX_GRAY_LVL.value ** self.gamma)
        self.img = img
    
    def gamma_correction_using_lut(self):
        lut = [(self.c * (i ** self.gamma)) for i in range(Constants.MAX_GRAY_LVL.value + 1)]                                         
        lut = np.array(lut, np.uint8)                                                                       
        modified_img_by_lut = cv.LUT(self.img, lut)  
        return modified_img_by_lut
    
    def gamma_correction_manually(self):
        rows = len(self.img)                                                                         
        columns = len(self.img[0]) 
        modified_img_manullay = np.zeros((rows, columns), dtype = np.uint8) 
        for i in range(rows):                                                                               
            for j in range(columns):
                modified_img_manullay[i][j] = self.c * (self.img[i][j] ** self.gamma)
        return modified_img_manullay

    def get_gamma_value(self):
        return self.gamma