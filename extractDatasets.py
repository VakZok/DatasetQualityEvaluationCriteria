import os
import shutil

def find_tsv_files(root_folder):
    tsv_files = []
    for foldername, subfolders, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename.endswith('.tsv'):
                tsv_files.append(os.path.join(foldername, filename))
    return tsv_files

def copy_tsv_files_to_folder(tsv_files, destination_folder):
    for tsv_file in tsv_files:
        shutil.copy(tsv_file, destination_folder)

# Specify the root folder where you want to start searching
root_folder = 'UCRArchive_2018'

# Specify the destination folder to copy .tsv files
destination_folder = 'UCR_Datasets'

# Get a list of all .tsv files in subfolders
tsv_files = find_tsv_files(root_folder)

# Copy .tsv files to the destination folder
copy_tsv_files_to_folder(tsv_files, destination_folder)

# Print the list of copied .tsv files
for tsv_file in tsv_files:
    destination_path = os.path.join(destination_folder, os.path.basename(tsv_file))
    print(f"Copied {tsv_file} to {destination_path}")