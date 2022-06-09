# Import required packages:
import cv2
# "dataset-original/test/24.94.2020.01.28.08.48.54.489.25735078_input.png"
# Load the image and convert it to grayscale:
image = cv2.imread("dataset-original/test/IMG-0005-00019_label.png")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply cv2.threshold() to get a binary image
ret, thresh = cv2.threshold(gray_image, 50, 255, cv2.THRESH_BINARY)

# Find contours:
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

image = cv2.imread("dataset-original/test/IMG-0005-00019_input.png")
# Draw contours:
cv2.drawContours(image, contours, 0, (0, 255, 0), 1)

# Show image:
cv2.imshow("outline contour", image)

# Wait until a key is pressed:
cv2.waitKey(0)

# Destroy all created windows:
cv2.destroyAllWindows()