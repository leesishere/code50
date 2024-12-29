import sys
import os
from PIL import Image


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
    overlay_path = 'shirt.png'

    try:
        # Open the overlay and background images
        overlay = Image.open(overlay_path)
        background = Image.open(background_image_path)


        output_size = (600, 600)
        aspect_ratio_output=background.size[0] /output_size[1]

        if aspect_ratio_output > output_size[0]/output_size[1]:
            new_height=int(output_size*aspect_ratio_output )

            resize_image= background.resize((int(new_height), int(1600)), Image.LANCZOS)

        else:
            #crop the image
            crop_box=( (int((background.size[0] - output_size[0])/2)) ,  (output_size[1], background.size[1]))
            resize_image = background.crop(crop_box)


        # Overlay the image with transparency handling
        overlay_paste=overlay.resize(output_size, Image.LANCZOS)
        resized_image=resize_image.paste(overlay_paste,(0, 0))

         # Save the result
        resized_image.save(sys.argv[2])
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
    file_extension_one = "."+file_path_one.split(".")[1].lower()
    file_extension_two = "."+file_path_two.split(".")[1]
    if (file_extension_one==file_extension_two):
        return True
    else:
        return False


if __name__ == "__main__":
      main()
