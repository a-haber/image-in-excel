from image import *
from spreadsheet import *

# Filename goes here
path = "tweety.jpg"
# Filename goes here


if __name__ == "__main__": # will not run if module is imported elsewhere
    im,size1 = read_image(path)
    pix_val, size2 = resize_image(im,size1)
    lists = pixel_lists(pix_val, size2)
    df = create_df(lists)
    create_sheet(df)