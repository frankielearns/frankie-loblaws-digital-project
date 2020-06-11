# import the necessary packages
from skimage import metrics
import matplotlib.pyplot as plt
import numpy as np
import cv2
import csv

with open('input.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

def mse(imageA, imageB):
	# the 'Mean Squared Error' between the two images is the
	# sum of the squared difference between the two images;
	# NOTE: the two images must have the same dimension
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])

	# return the MSE, the lower the error, the more "similar"
	# the two images are
	return err

def compare_images(imageA, imageB, title):
	# compute the mean squared error and structural similarity
	# index for the images
	s = metrics.structural_similarity(imageA, imageB)
	print(1 - s)

# load the images -- the original, the original + contrast,
# and the original + photoshop
original = cv2.imread("/i/frankie-loblaws-digital-project/images/aa.jpg")
contrast = cv2.imread("images/ab.png")
shopped = cv2.imread("images/ba.jpg")

# convert the images to grayscale
original = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
contrast = cv2.cvtColor(contrast, cv2.COLOR_BGR2GRAY)
shopped = cv2.cvtColor(shopped, cv2.COLOR_BGR2GRAY)



# compare the images
compare_images(original, original, "Original vs. Original")
compare_images(original, contrast, "Original vs. Contrast")
compare_images(original, shopped, "Original vs. Photoshopped")
