import sys
from PIL import Image

def main():
    if len(sys.argv) < 2:
        print("Usage: python display_image.py <path_to_image>")
        return

    image_path = sys.argv[1]

    try:
        # Open an image file
        image = Image.open(image_path)
        # Display the image
        image.show()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
