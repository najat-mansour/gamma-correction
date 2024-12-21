from imageio import *
from gammacorrections import GammaCorrection

import time

reader = Reader('resources\\images\\test.jpeg')
img = reader.get_read_img()

viwer = Viewer(img, 'Test Image')
viwer.show_img()
viwer.show_histogram()

gc = GammaCorrection(img)
print(f'Gamma Value = {gc.get_gamma_value()}')

start = time.time()
gc_by_lut_img = gc.gamma_correction_using_lut()
end = time.time()
print(f'LUT Time = {end - start}')
viwer = Viewer(gc_by_lut_img, 'Test Image With GC by LUT')
viwer.show_img()
viwer.show_histogram()

start = time.time()
gc_manually_img = gc.gamma_correction_manually()
end = time.time()
print(f'Manual Time = {end - start}')
viwer = Viewer(gc_manually_img, 'Test Image With GC Manually')
viwer.show_img()
viwer.show_histogram()