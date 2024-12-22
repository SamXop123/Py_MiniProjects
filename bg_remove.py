from rembg import remove
from PIL import Image

input_path = 'thor.png'
output_path = 'thor_rem.png'

# Open the input image
inp = Image.open(input_path)

# Remove the background
output = remove(inp)

# Save the output image
output.save(output_path)

# Open the new image
Image.open("thor_rem.png")

