import csv
import os
import random
path = os.getcwd()
files = []
randomyo = []


with os.scandir("{0}/images/".format(path)) as entries:
    for entry in entries:
        files.append(entry.name)
        randomyo.append(entry.name)
print(files)
random.shuffle(randomyo)
print(randomyo)



with open('input.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["image1", "image2"])
    for file, randoms in zip(files, randomyo):
        writer.writerow(['=HYPERLINK("{0}/{1}", "{1}")'.format(path, file), '=HYPERLINK("{0}/{1}", "{1}")'.format(path, randoms)])
