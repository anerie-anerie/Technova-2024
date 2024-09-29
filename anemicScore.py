import cv2
import dlib
import numpy as np
import tensorflow as tf
from imutils import face_utils
from decision_tree_model import predict_hb
from  nailsModel import predict_nail_filepath

#loading models in before might make it faster
model_NAIL = tf.keras.models.load_model('modelnail.keras')

model_PALM = tf.keras.models.load_model('modelpalm.keras')

def nailScore(img='nailsData/NAFingernails/Non-anemic-Fin-001 (2).png'):

    nailSco = predict_nail_filepath(img, model_NAIL)
    print(f"pre-score: {nailSco}")
    #spread out nail scores
    if nailSco > 0.416:
        nailSco += 0.5
    else:
        nailSco -= 0.3

    return nailSco

nailSco = nailScore()

def palmScore(img='palmData/NAPalm/Non-anemic-Pa-001 (2).png'):
    palmSco = predict_nail_filepath(img, model_PALM)
    print(f"pre-score palm: {palmSco}")
    if palmSco > 0.3:
        palmSco += 0.4
    else:
        palmSco -= 0.2

    return palmSco

palmSco = palmScore()

def eyePic ():
    # Load pre-trained dlib model
    # Location of the model (path of the model in the folder)
    Model_PATH = "shape_predictor_68_face_landmarks.dat"

    # Initialize the face detector
    detector = dlib.get_frontal_face_detector()

    # Initialize the shape predictor (landmark detector)
    predictor = dlib.shape_predictor(Model_PATH)

    # Load the image and USE IMG INPUT
    image = cv2.imread('NAConjectivitus.png')

    # Convert the image to grayscale (required for face detection)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    bbox = dlib.rectangle(left=10, top=10, right=8000, bottom=8000)

    # Predict the landmarks for the face
    landmarks = predictor(gray, bbox)

    # Convert the landmarks into a NumPy array
    landmarks = face_utils.shape_to_np(landmarks)

    left_eye = landmarks[36:42]  # Get the landmarks for the left eye

    # Define the rectangle coordinates
    top_left = (left_eye[4][0], left_eye[4][1])   # Outer corner of the left eye, moved down
    top_right = (left_eye[5][0] - 500, left_eye[5][1])  # Inner corner of the left eye, moved down
    bottom_left = (left_eye[4][0] - 300, left_eye[4][1] + 400)  # Move further down to create the rectangle
    bottom_right = (left_eye[5][0], left_eye[5][1] + 400) # Move further down to create the rectangle


    # Create a mask to isolate the under-eye area
    mask = np.zeros_like(image)

    # Define the polygon of the under-eye area using points 4 and 5 of the left eye
    under_eye_region = np.array([top_left, top_right, bottom_right, bottom_left])

    # Fill the mask with white in the under-eye region
    cv2.fillPoly(mask, [under_eye_region], (255, 255, 255))

    # Apply the mask to the image to isolate the under-eye region
    masked_image = cv2.bitwise_and(image, mask)

    cv2.fillPoly(mask, [under_eye_region], (255, 255, 255))

    # Mask the image to isolate the area of interest
    masked_image = cv2.bitwise_and(image, mask)

    # Convert the masked image to HSV for better color segmentation
    hsv_masked = cv2.cvtColor(masked_image, cv2.COLOR_BGR2HSV)

    # Define thresholds for red and green colors in HSV
    # Red color ranges
    red_lower = np.array([0, 100, 100])
    red_upper = np.array([10, 255, 255])
    red_mask = cv2.inRange(hsv_masked, red_lower, red_upper)

    # Green color ranges
    green_lower = np.array([40, 100, 100])
    green_upper = np.array([80, 255, 255])
    green_mask = cv2.inRange(hsv_masked, green_lower, green_upper)

    # Calculate total pixels in the mask
    total_masked_pixels = cv2.countNonZero(cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY))

    # Calculate red and green pixel counts
    red_pixels = cv2.countNonZero(red_mask)
    green_pixels = cv2.countNonZero(green_mask)

    # Calculate percentages with total pixel percetnage
    red_percentage = (red_pixels / total_masked_pixels) * 100 if total_masked_pixels > 0 else 0
    green_percentage = (green_pixels / total_masked_pixels) * 100 if total_masked_pixels > 0 else 0

    # Print the results
    print(f"Red Pixel Percentage: {red_percentage:.2f}%")
    print(f"Green Pixel Percentage: {green_percentage:.2f}%")


    if red_percentage <= 0:
        finalSc = 0.5
    else:
        finalSc = predict_hb(red_percentage, green_percentage)

    #return value of image
    return finalSc

eyeSco = eyePic()
'''
def nailScore(img='nailsData/AFingernails/Anemic-Fin-007 (2).png'):

    nailSco = predict_nail_filepath(img, model_NAIL)
    print(f"pre-score: {nailSco}")
    #spread out nail scores
    if nailSco > 0.41:
        nailSco += 0.5
    else:
        nailSco -= 0.3

    return nailSco

nailSco = nailScore()

def palmScore(img='palmData/APalm/Anemic-260 (2).png'):
    palmSco = predict_nail_filepath(img, model_PALM)
    print(f"pre-score palm: {palmSco}")
    if palmSco > 0.3:
        palmSco += 0.4
    else:
        palmSco -= 0.2

    return palmSco

palmSco = palmScore()

def eyePic ():
    # Load pre-trained dlib model
    # Location of the model (path of the model in the folder)
    Model_PATH = "shape_predictor_68_face_landmarks.dat"

    # Initialize the face detector
    detector = dlib.get_frontal_face_detector()

    # Initialize the shape predictor (landmark detector)
    predictor = dlib.shape_predictor(Model_PATH)

    # Load the image and USE IMG INPUT
    image = cv2.imread('92.png')

    # Convert the image to grayscale (required for face detection)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    bbox = dlib.rectangle(left=10, top=10, right=8000, bottom=8000)

    # Predict the landmarks for the face
    landmarks = predictor(gray, bbox)

    # Convert the landmarks into a NumPy array
    landmarks = face_utils.shape_to_np(landmarks)

    left_eye = landmarks[36:42]  # Get the landmarks for the left eye

    # Define the rectangle coordinates
    top_left = (left_eye[4][0], left_eye[4][1])   # Outer corner of the left eye, moved down
    top_right = (left_eye[5][0] - 500, left_eye[5][1])  # Inner corner of the left eye, moved down
    bottom_left = (left_eye[4][0] - 300, left_eye[4][1] + 400)  # Move further down to create the rectangle
    bottom_right = (left_eye[5][0], left_eye[5][1] + 400) # Move further down to create the rectangle


    # Create a mask to isolate the under-eye area
    mask = np.zeros_like(image)

    # Define the polygon of the under-eye area using points 4 and 5 of the left eye
    under_eye_region = np.array([top_left, top_right, bottom_right, bottom_left])

    # Fill the mask with white in the under-eye region
    cv2.fillPoly(mask, [under_eye_region], (255, 255, 255))

    # Apply the mask to the image to isolate the under-eye region
    masked_image = cv2.bitwise_and(image, mask)

    cv2.fillPoly(mask, [under_eye_region], (255, 255, 255))

    # Mask the image to isolate the area of interest
    masked_image = cv2.bitwise_and(image, mask)

    # Convert the masked image to HSV for better color segmentation
    hsv_masked = cv2.cvtColor(masked_image, cv2.COLOR_BGR2HSV)

    # Define thresholds for red and green colors in HSV
    # Red color
    red_lower = np.array([0, 100, 100])
    red_upper = np.array([10, 255, 255])
    red_mask = cv2.inRange(hsv_masked, red_lower, red_upper)

    # Green color
    green_lower = np.array([40, 100, 100])
    green_upper = np.array([80, 255, 255])
    green_mask = cv2.inRange(hsv_masked, green_lower, green_upper)

    # Calculate total pixels in the mask
    total_masked_pixels = cv2.countNonZero(cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY))

    # Calculate red and green pixel counts
    red_pixels = cv2.countNonZero(red_mask)
    green_pixels = cv2.countNonZero(green_mask)

    # Calculate percentages
    red_percentage = (red_pixels / total_masked_pixels) * 100 if total_masked_pixels > 0 else 0
    green_percentage = (green_pixels / total_masked_pixels) * 100 if total_masked_pixels > 0 else 0

    # Print the results
    print(f"Red Pixel Percentage: {red_percentage:.2f}%")
    print(f"Green Pixel Percentage: {green_percentage:.2f}%")

    finalSc = predict_hb(red_percentage, green_percentage)

    #return value of image
    return finalSc

eyeSco = eyePic()
'''
finalAnemiaScore = 0
finalAnemiaScore = (eyeSco*0.7)+(palmSco*0.2)+(nailSco*0.1)

print(f"Final Anemia: {finalAnemiaScore*100}%")