import numpy as np
from PIL import Image
from math import sqrt

File = "images/dallE_earthday.png"


# open the image and loading it into a 
# numpy array using PIL and Image
img = Image.open(File)
pixels = np.array(img)

# dimensions of the image
width, height, channels = pixels.shape

# this is information you will need to 
# compute the real life distance
actual_width = 1
actual_units = "meter"

# computing the pixel distance using the distance formula
(x1,y1) = (500, 300)
(x2, y2) = (264, 159)

pixel_distance = sqrt((x1 - x2)**2 + (y1 - y2)**2)

# scale the pixel distance to the actual distance
actual_distance = (pixel_distance/width) * actual_width

print(f"The distance between the two points is about {actual_distance:.3f} : {actual_units}")