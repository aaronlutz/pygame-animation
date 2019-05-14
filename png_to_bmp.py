import os
import pygame
from PIL import Image

folder_path = '\\Users\\aaron\\Documents\\python_work\\Animating\\climbing_left\\'

for file_name in os.listdir(folder_path):
    image = Image.open(folder_path + file_name)
    file_name_txt = file_name[:-4]
    bmp = '.bmp'
    new_file_name = file_name_txt + bmp
    image.save(folder_path + new_file_name)
    print(folder_path + new_file_name)
