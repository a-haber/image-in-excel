import glob, os

from image import *
from spreadsheet import *

def run(extra_compression=0, extra_quality=0, colouring='std'):
    """options for colouring: 'std' (standard - default), 'invert',
    'bw' (black/white), 'bws' (black/white smoothened - doesn't use individual rgb pixels)\n
    compression and quality are optional integers to increase/decrease output size"""
    for path in glob.glob("*.jpg"): # run on all images in current directory
        filename,ext = os.path.splitext(path)

        im,size1 = read_image(path)
        pix_val, size2 = resize_image(im,size1,extra_compression,extra_quality)
        lists = pixel_lists(pix_val, size2,colouring)
        df = create_df(lists)
        create_sheet(df,filename,colouring)


if __name__ == "__main__": # will not run if module is imported elsewhere
    
    # OPTIONAL FEATURES CAN BE CONTROLLED HERE (eg. colouring modes):
    run()