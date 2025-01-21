
# Seamlessly remove background from any object using this code

from rembg import remove
from PIL import Image

input_path = 'filename.png'
output_path = 'filename_bgrem.png'

# Open the input image
inp = Image.open(input_path)

# Remove the background
output = remove(inp)

# Save the output image
output.save(output_path)

# Open the new image
Image.open("filename_bgrem.png")

