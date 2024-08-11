#Filename Example: GMT20210727-200343_Recording

import os
import os.path
from datetime import datetime

# Absolute path for the directory where all the zoom recording files are
SOURCE_DIR = r''
# Datetime format for the folder that will contain the respective zoom recording files
FORMAT_OUTPUT_FOLDER_NAME = '%m_%d_%Y'
FORMAT_ZOOM_FILE = '%Y%m%d-%H%M%S'

for filename in os.listdir(SOURCE_DIR):
    file_path = os.path.join(SOURCE_DIR, filename)

    if not os.path.isfile(file_path): continue

    try:
        datetime_str = filename[3:18]
        item_datetime = datetime.strptime(datetime_str, FORMAT_ZOOM_FILE)
    except ValueError:
        print(f'Invalid filename format: {filename}')
        continue

    destination_folder_name = item_datetime.strftime(FORMAT_OUTPUT_FOLDER_NAME)
    destination_folder_path = os.path.join(SOURCE_DIR, destination_folder_name)
    destination_file_path = os.path.join(destination_folder_path, filename)

    if os.path.isdir(destination_folder_path):
        print('moving file')
    else:
        os.makedirs(destination_folder_path)
        print('creating folder and moving file')

    os.rename(file_path, destination_file_path)
