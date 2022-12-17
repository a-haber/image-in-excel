# image-in-excel
Recreate .jpg image in excel using cells as pixels


## Summary ##

__dependencies / modules required:__ pandas, os, glob, Pillow (PIL Fork) Image module

### Process ###
The program converts __all .jpg images in the current directory__ into excel pixel art, by creating a spreadsheet where each cell contains a value from 0 to 255, representing a red, green or blue subpixel. The sheet is formatted so that each subpixel is coloured appropriately to make a full image.
### Examples ###
Using the example (540x481) jpeg image tweety.jpg, the output spreadsheet looks as follows (screenshots with various levels of zoom):

![Example Output with zoom](example-output-images\standard-output-screenshot.png)

### Formatting options ###
__image compression__
- standard compression will output a file with a max size of 240 rows x 187 columns
- size can be controlled using the optional parameters
  - `run(extra_compression=a)`
  - `run(extra_quality=b)`
- where _a_ and _b_ are positive integers
- there is an upper limit on the increased size which the `extra_quality` parameter will allow

__colouring options__
- standard: recreates the image as closely as possible
- invert: colour inversion
  - `run(colouring='invert')`
- black/white: rgb subpixels used to create overall greyscale image
  - `run(colouring='bw')`
- black/white alternative: each subpixel is greyscale, creating a smoother b/w image but without using rgb pixels
  - `run(colouring='bws')`

Some examples (screenshots of different outputs):

Invert

![Inverted](example-output-images\tweety_output_screenshot_invertcolours.png)

B/W (greyscale with rgb)

![Black/White](example-output-images\tweety_output_screenshot_bw.png)

BWS (pure greyscale, no rgb)

![Black/White Smoothened](example-output-images\tweety_output_screenshot_bws.png)