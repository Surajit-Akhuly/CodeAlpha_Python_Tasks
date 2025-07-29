import os
import shutil

# Source and destination folders
source_folder = "source_images"
destination_folder = "jpg_images"

# Create destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Move all .jpg files
files_moved = 0
for file_name in os.listdir(source_folder):
    if file_name.lower().endswith(".jpg"):
        src_path = os.path.join(source_folder, file_name)
        dest_path = os.path.join(destination_folder, file_name)
        shutil.move(src_path, dest_path)
        files_moved += 1

print(f"✅ Moved {files_moved} .jpg files to '{destination_folder}' folder.")
