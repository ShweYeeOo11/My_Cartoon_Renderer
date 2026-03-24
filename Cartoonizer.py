import cv2
import numpy as np

# Load the image
img = cv2.imread('test_image.JPG')

# Change to grayscale so I can process the edges
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Boost the contrast here so the hair strands show up better
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
gray_enhanced = clahe.apply(gray)

# Create the black outlines
edges = cv2.adaptiveThreshold(gray_enhanced, 255, 
                              cv2.ADAPTIVE_THRESH_MEAN_C, 
                              cv2.THRESH_BINARY, 3, 2)

# Clean up some of the tiny black dots (noise) but keep the lines sharp
edges = cv2.medianBlur(edges, 3)

# Put the original image and the black outlines together
cartoon = cv2.bitwise_and(img, img, mask=edges)

# Show the final result and save a copy for my GitHub
cv2.imshow("My Detailed Cartoon Style", cartoon)
cv2.imwrite('final_result.jpg', cartoon)

# Wait for a key press to close the window
cv2.waitKey(0)
cv2.destroyAllWindows()