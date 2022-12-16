"""Test for image.py and spreadsheet.py modules"""

from image import *
from spreadsheet import *

def test_read_image():
    im, size= read_image("tweety.jpg")
    pix_val = list(im.getdata())
    assert size == (540,481)
    assert len(pix_val) == 259740
    PILclass = type(im)

    im2, size2 = read_image("chicken.jpg")
    pix_val2 = list(im2.getdata())
    assert size2 == (341,425)
    assert len(pix_val2) == 144925
    assert isinstance(im2,PILclass)

def test_resize_image():
    im, size = read_image("tweety.jpg")
    pix_val, newsize = resize_image(im, size)
    assert isinstance(pix_val, list)
    assert isinstance(pix_val[0], tuple)
    assert (size[0]*size[1] >= len(pix_val)) 
    assert (size[0] >= newsize[0])

def test_pixel_lists():
    pixels = [(255,255,255)]*4020
    (x,y) = (67,60)
    lists = pixel_lists(pixels, (x, y))
    assert(len(lists) == 3*y)
    assert(len(lists[0]) == x)
    
def test_create_df():
    (x,y) = (67,60)
    lists = [255] * x
    lists = [lists] * y
    df = create_df(lists)
    assert (df.shape == (y,x))

test_create_df()