from PIL import Image

def read_image(filename):
    """read image from jpg file: returns image as PIL object and size (x,y)"""
    im = Image.open(filename) # str: filename
    (x,y) = im.size
    return(im, (x,y))

def resize_image(im, original_size):
    """resize image appropriately for reasonably sized excel file\n
    return list of pixel values and new size"""
    (x,y) = original_size
    for i in range(3): # brute force to resize this particular image to an appropriate size for now
        x//=2
        y//=2
        im = im.resize((x,y))
    return(list(im.getdata()), im.size)

def pixel_lists(pixels, size):
    """split pixel values into lists of correct size and shape for spreadsheet"""

    lists = [] # create empty lists
    (x,rows) = size
    for i in range(rows):
        # for each row (y) in image, create three new rows
        # one row for each colour r,g,b
        for j in range(3):
            colour = [k[j] for k in pixels[x*i:x*(i+1)]]
            lists.append(colour)
    return(lists)