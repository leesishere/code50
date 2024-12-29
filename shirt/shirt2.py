import sys
import os
from PIL import Image, ImageOps


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

    try:
        # Open the overlay and background images
        overlay = Image.open(overlay_path)
        background = Image.open(background_image_path)

        # Resize and crop the input image with default values for method, bleed, and centering
        output_size = (600, 600)
        aspect_ratio = output_size[0] / output_size[1]
        width, height = background.size

        if aspect_ratio > height/width:
            new_width = int((height * aspect_ratio))
            new_height= height
            crop_box=(int(new_width - (new_width-width)/2), 0, int(new_width+(new_width-width)/2) , new_height)
        else:
           new_width = width
           new_height= int(height*aspect_ratio )
           crop_box=( 0, int((height-new_height)/2), width , int((height-new_height)+new_height/2))

        background = ImageOps.fit(background, output_size, Image.LANCZOS)

        # Overlay the image with transparency handling
        background.paste(overlay, (crop_box[1], crop_box[0]))

        # Save the result
        background.save(output_path)
    except Exception as e:
       print(str(e))
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
    file_extension_one = os.path.splitext(file_path_one)[1].lower()
    file_extension_two = "."+file_path_two.split(".")[1]
    if file_extension_one == file_extension_two:
        return True
    else:
        return False

if __name__ == "__main__":
      main()
