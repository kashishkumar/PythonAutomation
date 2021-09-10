# A program for segregating files into different folders
# Given a folder with image and text files, segregate images and text files into two different folders.
from glob import glob
import os
import shutil
import sys 

path = "..."

def get_file_paths(path):
    image_files = glob(path + '/*.tiff') + glob(path + '/*.png') + glob(path + '/*.jpg')
    text_files = glob(path + '/*.txt') 
    return image_files, text_files
image_files, text_files = get_file_paths(path)

# Create directories for image and text files
def create_directory(image_files, text_files):
    image_path = os.path.join(path, 'images')
    text_path = os.path.join(path, 'textfiles')
    if os.path.isdir(image_path) ==  False:
        os.mkdir(image_path)
    if os.path.isdir(text_path) ==  False:
        os.mkdir(text_path) 
    
    return image_path, text_path

image_path, text_path = create_directory(image_files, text_files)

# Move files to specific folders
def move_files(image_files, text_files, image_path, text_path):
    for image in image_files:
        shutil.move(image, os.path.join(image_path, os.path.basename(image)))
    for text_file in text_files:
        shutil.move(text_file, os.path.join(text_path, os.path.basename(text_file)))

move_files(image_files, text_files, image_path, text_path)
