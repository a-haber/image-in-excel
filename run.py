import glob, os

from image import *
from spreadsheet import *




if __name__ == "__main__": # will not run if module is imported elsewhere
    
    for path in glob.glob("*.jpg"): # run on all images in current directory
        filename,ext = os.path.splitext(path)

        im,size1 = read_image(path)
        pix_val, size2 = resize_image(im,size1)
        lists = pixel_lists(pix_val, size2)
        df = create_df(lists)
        create_sheet(df,filename)