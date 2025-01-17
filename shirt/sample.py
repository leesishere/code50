from PIL import Image, ImageOps
import numpy as np

# Load images from file
img = Image.open("before1.jpg")
shirt_img = Image.open("shirt.png")

# Resize and crop the input image
resized_img = img.copy()
width, height = resized_img.size
cropped_width, cropped_height = 1000, 600
overlaid_shirt_size= shirt_img.size

# Overlay the shirt image
overlayed_shirt = Image.new('RGBA', overlaid_shirt_size)

shirt_scaled=shirt_img.resize((resized_cropped.width*0.8,resized_cropped.height*0.8))
overlayed_shirt.paste(shirt_scaled,(20, 50), mask=None)
# Create a new image to hold the composition
composing_img = Image.new('RGB', (cropped_width, cropped_height), color=(255, 255, 255))

for x in range(composed.width):
    for y in range(composed.height):
        pixel_value= overlayed_shirt.getpixel((x % overlaid_shirt_size[0],y% overlaid_shirt_size[1]))
        composing_img.putpixel((x + cropped_rect[0], y + cropped_rect[1]), (int(pixel_value[0]),
                                                                int(pixel_value[1]),
                                                                int(pixel_value[2]),
                                                                255))

# Save the resulting image
composing_img.save("after.png")
