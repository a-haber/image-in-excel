from PIL import Image

def read_image(filename):
    """read image from jpg file: returns image as PIL object and size (x,y)"""
    im = Image.open(filename) # str: filename
    (x,y) = im.size
    return(im, (x,y))

def resize_image(im, original_size, extra_compression=0, extra_quality=0):
    """resize image appropriately for reasonably sized excel file\n
    integers extra_compression and extra_quality allow greater control of output size\n
    return list of pixel values and new size"""
    (x,y) = original_size
    while (y >= 80 or x >= 187): # sets limit of 3*80=240 rows, 187 columns
        x//=2
        y//=2
        im = im.resize((x,y))
    
    # optional parameters to control output quality
    for i in range(extra_compression): # optional: compress size even further
        x,y = int(0.75*x), int(0.75*y)
        im = im.resize((x,y))
    for i in range(extra_quality):
        if (y<=135 and x <=280): # set upper limit on size
            x,y = int(1.5*x), int(1.5*y)
            im = im.resize((x,y))
        else:
            print("Warning: Image size getting too large!\nConsider reducing output size with the extra_compression and extra_quality parameters")
            break

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