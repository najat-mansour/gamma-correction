from helpers import Constants

import cv2 as cv
from matplotlib import pyplot as plt

class Reader:
    def __init__(self, path):
        try:
            colored_img = cv.imread(path)
        except Exception:
            print('Invalid Path')
        self.img = cv.cvtColor(colored_img, cv.COLOR_BGR2GRAY)

    def get_read_img(self):
        return self.img

class Viewer:
    def __init__(self, img, title):
        self.img = img
        self.title = title

    def show_img(self):
        cv.imshow(self.title, self._resized_img(self.img))                                                          
        cv.waitKey(0)                                                                 
        cv.destroyAllWindows()                                                        

    def show_histogram(self):
        plt.figure().set_figwidth(12)                                                 
        plt.plot(cv.calcHist([self.img], [0], None, [Constants.MAX_GRAY_LVL.value + 1], [0, Constants.MAX_GRAY_LVL.value + 1]))
        plt.title(f'{self.title} histogram')                                                           
        plt.xlabel('Gray Levels')                                                     
        plt.ylabel('No. Of Pixels')                                                   
        plt.xlim([0, Constants.MAX_GRAY_LVL.value])                                                   
        plt.ylim(ymin = 0)                                                            
        plt.locator_params(axis = 'x', nbins = 50)                                    
        plt.show()     

    def _resized_img(self, gray_scale_img):
        width = int(gray_scale_img.shape[1] * Constants.SCALING_FACTOR.value)                                              
        height = int(gray_scale_img.shape[0] * Constants.SCALING_FACTOR.value)                                              
        dim = (width, height)                                                         
        resized_image = cv.resize(gray_scale_img, dim, interpolation = cv.INTER_AREA)
        return resized_image          