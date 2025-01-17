from PIL import Image, ImageOps
import numpy as np

# Load images from file
img = Image.open("before1.jpg")
shirt_img = Image.open("shirt.png")

# Resize and crop the input image
resized_img = img.copy()
width, height = resized_img.size
cropped_width, cropped_height = 1000, 600
cropped_rect = (height // 3, width // 3, cropped_height + height // 6 * 2, cropped_width + width // 6 * 2)
resized_cropped = img.crop(cropped_rect)

# Overlay the shirt image
shirt_scaled = shirt_img.resize(resized_cropped.size)
overlayed_shirt = ImageOps.fit(shirt_scaled, resized_cropped.size, method=Image.FIT proportionally

# Create a new image to hold the composition
composing_img = Image.new('RGB', (cropped_width, cropped_height), color=(255, 255, 255))

# Paste the overlaid shirt onto the composinimg
for x in range(cropped_width):
    for y in range(cropped_height):
        pixel_value = overlayed_shirt.getpixel((x % resized_cropped.size[0], y % resized_cropped.size[1]))
        composing_img.putpixel((x + cropped_rect[0], y + cropped_rect[1]), (int(pixel_value[0]),
                                                                int(pixel_value[1]),
                                                                int(pixel_value[2]),
                                                                255))

# Save the resulting image
shirt_scaled = shirt_img.resize(resized_cropped.size)
overlayed_shirt = ImageOps.fit(shirt_scaled, resized_cropped.size, method=Image.FIT
                                proportionally)
composing_img.paste(overlaid_shirt, mask=None)

# Overlaying a color so the transparency of overlaidshirt is visible in  after.png
for x in range(composing_img.size[0]):
    for y in range(composing_img.size[1]):
        pixel_value = (255, 255, 255)
        composing_img.putpixel((x ,y), pixel_value)

# Save the resulting image
composing_img.save("after.png")
