import cv2

# Load the image 
img = cv2.imread("C:\\Users\\Acer\\Desktop\\nobi.jpg")

if img is None:
  print("Unable to load image.")

else:
  # Convert the image to RGB
  img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

  # Convert the image from RGB to Grayscale
  image_gray = cv2.cvtColor(img_rgb,cv2.COLOR_BGR2GRAY)

  # Display the image
  cv2.imshow("Grayscale", image_gray)

  # Wait until a key is pressed
  cv2.waitKey(0)

  # Destroy all windows opened by OpenCV
  cv2.destroyAllWindows()