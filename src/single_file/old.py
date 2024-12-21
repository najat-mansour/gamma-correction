import cv2 as cv                                        #! computer vision library
import numpy as np                                      #! numerical python library
from matplotlib import pyplot as plt                    #! plot curves (histogram)
import random as rand                                   #! generate random number
import time                                             #! calculate execution time

#! constants
MAX_GRAY_LVL = 255
MIN_GAMMA_VAL = 0.04
MAX_GAMMA_VAL = 5

#! function to show an image after resizing it and wait for the user
def show_img(img_title, img):
    width = int(img.shape[1] * 0.5)                                               # width scaling
    height = int(img.shape[0] * 0.5)                                              # height scaling
    dim = (width, height)                                                         # define a tuple 
    resized_image = cv.resize(img, dim, interpolation = cv.INTER_AREA)            # resize the image
    cv.imshow(img_title, resized_image)                                           # show the image                  
    cv.waitKey(0)                                                                 # wait for the user
    cv.destroyAllWindows()                                                        # close the window

#! function to show the histogram of an image
def show_hist(hist_tile, img):
    plt.figure().set_figwidth(12)                                                 # customize the width of the figure
    plt.plot(cv.calcHist([img],[0],None,[MAX_GRAY_LVL + 1],[0,MAX_GRAY_LVL + 1])) # plot the histogram
    plt.title(hist_tile)                                                          # set the title
    plt.xlabel('Gray Levels')                                                     # label for x-axis
    plt.ylabel('No. Of Pixels')                                                   # label for y-axis
    plt.xlim([0, MAX_GRAY_LVL])                                                   # range of x-axis
    plt.ylim(ymin = 0)                                                            # range of y-axis
    plt.locator_params(axis = 'x', nbins = 50)                                    # customize the number of pins in x-axis
    plt.show()                                                                    # show the figure

#TODO: read the input image
img = cv.imread('resources\\images\\test.jpeg')                                   # change the path to test my code             

#TODO: convert the input image into the grayscale
gray_sacle_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)    
show_img('Grayscale Image', gray_sacle_img)
show_hist('Grayscale Image Histogram', gray_sacle_img)

#TODO: modify the brightness of the image using gamma-correction 
#! generate random number
while True:
    gamma = rand.uniform(MIN_GAMMA_VAL, MAX_GAMMA_VAL) 
    # if gamma < 1 ---> takes two decimal point digits
    if gamma < 1:
        gamma = round(gamma, 2)
        break
    
    # if gamma >= 2 ---> no fraction is allowed 
    elif gamma >= 2:
        gamma = int(gamma)
        break

#! calculate the scaling factor (c), s = c * r^gamma
c = MAX_GRAY_LVL / (MAX_GRAY_LVL ** gamma) 

#! modification using lookup table
start = time.time();                                                                                # time before
lut = [(c * (i ** gamma)) for i in range(MAX_GRAY_LVL + 1)]                                         # generate the lookup table
lut = np.array(lut, np.uint8)                                                                       # convert it into array
modified_img_by_lut = cv.LUT(gray_sacle_img, lut)                                                   # perform it on the image
end = time.time();                                                                                  # time after
show_img('Modified Image Using LUT with gamma ' + str(gamma), modified_img_by_lut)
show_hist('Modified Image Using LUT with gamma ' + str(gamma) + ' Histogram', modified_img_by_lut)
print('LUT execution time =',end - start,'seconds')

#! modification manually pixel by pixel
rows = len(gray_sacle_img)                                                                          # calculate the rows
columns = len(gray_sacle_img[0])                                                                    # calculate the columns
modified_img_manullay = np.zeros((rows, columns), dtype = np.uint8)                                               # generate an array for the output image
start = time.time()                                                                                 # time before
for i in range(rows):                                                                               
    for j in range(columns):
        modified_img_manullay[i][j] = c * (gray_sacle_img[i][j] ** gamma)                           # modified each pixel
end = time.time()                                                                                   # time after
show_img('Modified Image Manually with gamma ' + str(gamma), modified_img_manullay)
show_hist('Modified Image Manually with gamma ' + str(gamma) + ' Histogram', modified_img_manullay)
print('Manual execution time =',end - start,'seconds')