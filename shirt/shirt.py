from PIL import Image, ImageOps
import sys
import os


def main():
    # check image file args...
    if not check_arguments(sys.argv):
        if len(sys.argv) < 3:
            print("Too few command-line arguments")
            sys.exit(1)
        if len(sys.argv) > 3:
            print("Too many command-line arguments")
            sys.exit(1)
    else:
        if not extension(sys.argv[1], sys.argv[2]):
            print("Input and output have different extensions")
            sys.exit(1)
        if not validate_extension(sys.argv[2]):
            print("Invalid output")
            sys.exit(1)

    # Open an image file

    background_image_path = sys.argv[1]
    output_path = sys.argv[2]

    overlay_path = 'shirt.png'
    # Open the overlay and background images
    overlay = Image.open(overlay_path)
    background = Image.open(background_image_path)
    background = ImageOps.fit(600, 600)

    #with Image.open(background_image_path) as im:
    #    ImageOps.fit(im, size).save("imageops_fit.webp")


    
    '''
    # Image size: 1200 x 1600 pixels

    # Get the dimensions of the background image
    width, height = background.size
    # Define the crop box (left, upper, right, lower)
    top_pixels = 0
    if "1" in background_image_path:
        crop_box = (0, top_pixels + 75, width, height - 76)
        crop_box = (0, top_pixels + 72, width, height - 72)
    else:
        crop_box = (0, top_pixels + 200, width + 0, height - 200)
    # Crop the image
    background = background.crop(crop_box)
    '''

    # Resize the background image to fit the overlay size
    #overlay = overlay.resize(background.size, Image.LANCZOS)
    background = background.resize(overlay.size, Image.LANCZOS)


    # Set the position for the overlay (e.g., center it on the background)
    position = (0, -40)
    position = (0, 0)

    # Top-left corner
    # # Overlay the image with transparency handling
    background.paste(overlay, position, overlay)
    # Save the result
    background.save(output_path)

def check_arguments(params):
    if len(params) == 3:
        return True
    else:
        return False

def file_exists(file_path):
    # Check if the file exists
    if os.path.isfile(file_path):
        return True
    else:
        return False
def validate_extension(file_extension):
    extension = os.path.splitext(file_extension)[1]
    if (extension == '.jpg' or extension == '.png'):
        return True
    else:
        return False

def extension(file_path_one, file_path_two):
    file_extension_one = os.path.splitext(file_path_one)[1]
    file_extension_two = file_path_two.split(".")[1]
    file_extension_two = "." + file_extension_two
    if file_extension_one == file_extension_two:
        return True
    else:
        return False

if __name__ == "__main__":
      main()
