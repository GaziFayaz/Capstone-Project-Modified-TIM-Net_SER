import os
import shutil

# Specify the folder containing the files
folder_path = 'D:/University/CSE400/Capstone-Project-Modified-TIM-Net_SER/SUBESCO'

# Specify the substring to look for in the file names
substring_to_match = 'SAD'

# Create a dictionary to store file lists based on the substring
file_lists = {}

# List all files in the folder
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    
    # Check if the file name contains the specified substring
    if substring_to_match in filename:
        # Determine the destination folder based on the substring
        destination_folder = os.path.join(folder_path, substring_to_match)
        
        # Create the destination folder if it doesn't exist
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder.capitalize())
        
        # Move the file to the destination folder
        shutil.move(file_path, os.path.join(destination_folder, filename))
    else:
        # If the file name doesn't contain the substring, you can specify a different destination or handle it differently
        # For example, you can place these files in a different folder or ignore them
        pass

print("Files have been separated based on the substring.")
