from PIL import Image, ImageOps

# Load images from file
img = Image.open("before1.jpg")
shirt_img = Image.open("shirt.png")

# Resize and crop the input image
width, height = img.size
cropped_width, cropped_height = 1000, 600
overlaid_shirt_size= shirt_img.size

resized_cropped= img.crop((0,width//3, 0,height))

shirt_scaled=shirt_img.resize(resized_cropped)

# Overlay the shirt image
overlayed_shirt = Image.new('RGBA', overlaid_shirt_size)
 overlayed_shirt.paste(shirt_scaled,(20, 50), mask=None)

# Create a new image to hold the composition
composing_img = Image.new('RGB', (cropped_width, cropped_height), color=(0,0,0))

for x in range(composed.width):
    for y in range(composed.height):
        pixel_value= overlayed_shirt.getpixel((x % overlaid_shirt_size[0],y% overlaid_shirt_size[1]))
        composing_img.putpixel((x + cropped_rect[0]//2, (cropped_height - 1-y) // 2), (int(pixel_value[0]),
                                                                int(pixel_value[1]),
                                                                int(pixel_value[2]),))

# Save the resulting image
composing_img.save("after1.png")
