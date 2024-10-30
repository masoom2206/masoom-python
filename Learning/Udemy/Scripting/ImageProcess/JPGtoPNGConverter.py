# /opt/homebrew/bin/python3 /Users/masoom2206/coading/python/masoom-python/Learning/Udemy/Scripting/ImageProcess/JPGtoPNGConverter.py Pokedesk/ NewFolder/

import sys
import os
from PIL import Image

# Grap first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]
print(image_folder, output_folder)
# check is folder exist, it not create
if not os.path.exists("Learning/Udemy/Scripting/ImageProcess/"+output_folder):
  os.makedirs("Learning/Udemy/Scripting/ImageProcess/"+output_folder)
# Loop all files from folder then save in new
# Convert image to png
# Save to the new folder
for filename in os.listdir("Learning/Udemy/Scripting/ImageProcess/"+image_folder):
  img = Image.open(f'Learning/Udemy/Scripting/ImageProcess/{image_folder}{filename}')
  clean_name = os.path.splitext(filename)[0]
  img.save(f'Learning/Udemy/Scripting/ImageProcess/{output_folder}{clean_name}.png', 'png')
  print("All Done!")
