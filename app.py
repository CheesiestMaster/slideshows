#!/usr/bin/python3

from os import getlogin, system, listdir
from sys import argv
from random import shuffle
from time import sleep

# have three command line arguments passed in a directory, a number for seconds and a boolean for random
# the directory is the image directory
# default is ~/Pictures/
image_dir = argv[1] if len(argv) > 1 else f"/home/{getlogin()}/Pictures/"
# the number is the number of seconds to wait before changing the image
# default is 60 seconds
seconds = int(argv[2]) if len(argv) > 2 else 60
# the boolean is whether or not to randomize the images after each cycle
# default is false
randomize = bool(argv[3]) if len(argv) > 3 else False

_extensions = ['jpg', 'jpeg', 'png', 'gif']

images = []
for filename in listdir(image_dir):
    if filename.endswith(tuple(_extensions)):
        images.append(filename)

if randomize:
    shuffle(images)

while True:
    for image in images:
        system("gsettings set org.gnome.desktop.background picture-uri 'file://"+image_dir+image+"'")
        sleep(seconds)
    if randomize:
        shuffle(images)
