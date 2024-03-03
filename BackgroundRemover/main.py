from rembg import remove
from PIL import Image

input_path = 'input.jpg'
output_path = 'output.png'

input_image = Image.open(input_path)
output_image = remove(input_image)
output_image.save(output_path)

"""
from rembg import remove


input_path = "input.jpg"
output_path = "output.png"

with open(input_path, 'rb') as i:
    with open(output_path, 'wb') as o:
        input_file = i.read()
        output_file = remove(input_file)
        o.write(output_file)
"""