import cv2
from PIL import Image, ImageOps

# Load images using open cv
img = cv2.imread("before1.jpg")
shirt_img =  cv2.imread("shirt.png")

# Resize and crop the input image
resized_img = img.copy()
cv2.resize(resized_img,(1000,600))
width,height= resized_img.shape[1],resized_img.shape[0]
cropped= resized_img[int(height/3):int(2*height/3), int(width/3):int(2*width/3)]

# Overlay the shirt image
overlayed = Image.fromarray(cropped)
shirt_pil =  Image.open("shirt.png")
shirtscaled=shirt_pil.resize((cropped.shape[1], cropped.shape[0]))
overlaid_shirt=ImageOps.fit(shirtscaled, overlayed.size, method=2, bleed=(20.0/100*overlayed.size), centering=(50.0/100*overlayed.size))
composing_img= Image.new('RGB', (cropped.shape[1], cropped.shape[0]), color = 255)
overlaid_shirt.paste(overlayed, mask=None)
composing_img.paste(composing_img, mask=None)

# Save the resulting image
cv2.imwrite("after1.png", cv2.cvtColor(np.array(composing_img), cv2.COLOR_RGB2BGR))
