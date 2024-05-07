import os
import datetime

current_date = datetime.datetime.now().strftime("%Y-%m-%d")

os.mkdir(current_date)

file_path = os.path.join(current_date, "empty_file.txt")
with open(file_path, 'w') as file:
    pass

subdirectory_path = os.path.join(current_date, "subdirectory")
os.mkdir(subdirectory_path)

new_file_path = os.path.join(subdirectory_path, "empty_file.txt")
os.rename(file_path, new_file_path)
