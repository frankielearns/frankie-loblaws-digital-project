# import the necessary packages
from skimage import metrics
import numpy as np
import cv2
import csv
import re
import os
from timeit import default_timer as timer


def dir_list():
    path = os.getcwd()
    files = []

    with os.scandir("{0}/images/".format(path)) as entries:
        for entry in entries:
            files.append(entry.name)
    return files,path

def input_file(files, path):
    with open('input.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        files_list = iter(files)
        writer.writerow(["image1", "image2"])
        for file in files_list:
            writer.writerow(['=HYPERLINK("{0}/images/{1}", "{1}")'.format(path, file), '=HYPERLINK("{0}/images/{1}", "{1}")'.format(path, next(files_list))])

def filter_csv():
    image_1_files_list = []
    image_2_files_list = []

    with open('input.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            image_1 = (re.sub('\=HYPERLINK\(|\)', '',row[0]))
            image_2 = (re.sub('\=HYPERLINK\(|\)', '',row[1]))
            image_1_string_to_list = image_1.split(',')
            image_2_string_to_list = image_2.split(',')
            image_1_files_list.append(image_1_string_to_list[0].strip('""'))
            image_2_files_list.append(image_2_string_to_list[0].strip('""'))
    return image_1_files_list, image_2_files_list

def compare_images(imageA, imageB, title):
	s = metrics.structural_similarity(imageA, imageB)
	return (1 - s)

def output(files, path, image_1_files_list, image_2_files_list):

    similarities = []
    elapsed = []
    for images1, images2 in zip(image_1_files_list, image_2_files_list):
        start = timer()
        original = cv2.imread(images1)
        contrast = cv2.imread(images2)

        original = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
        contrast = cv2.cvtColor(contrast, cv2.COLOR_BGR2GRAY)
        end = timer()
        elapsed.append(end - start)

        similarities.append(compare_images(original, contrast, "Original vs. Contrast"))

    with open('output.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["image1", "image2", "similar", "elapsed"])
        files_list = iter(files)
        for file, similar_scoring, elapsed_time  in zip(files_list, similarities, elapsed):
            writer.writerow(['=HYPERLINK("{0}/images/{1}", "{1}")'.format(path, file), '=HYPERLINK("{0}/images/{1}", "{1}")'.format(path, next(files_list)), '{0}'.format(similar_scoring), '{0}'.format(elapsed_time)])

def main():
    files, path = dir_list()
    input_file(files, path)
    image_1_files_list, image_2_files_list = filter_csv()
    output(files, path, image_1_files_list, image_2_files_list)
if __name__ == '__main__':
    main()
