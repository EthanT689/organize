import os          # Handles file and folder paths
import shutil      # Used to move files from one place to another

# Set the folder you want to organize
source_folder = r'C:\Users\YourUsername\Downloads'  # <- change this to your actual folder

# Define the types of files to look for
file_types = {
    "Images": ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    "Documents": ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    "Videos": ['.mp4', '.mkv', '.mov'],
    "Music": ['.mp3', '.wav', '.aac'],
    "Archives": ['.zip', '.rar', '.tar', '.gz'],
}
# Function to organize the files
def organize_files():
    for filename in os.listdir(source_folder):  # Go through every file in the folder
        file_path = os.path.join(source_folder, filename)

        # Only act on actual files (ignore folders)
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(filename)[1].lower()  # Get the file extension

            moved = False  # Flag to track if file was sorted
            # Check if file matches a known category
            for folder, extensions in file_types.items():
                if file_ext in extensions:
                    folder_path = os.path.join(source_folder, folder)  # e.g. Downloads/Images
                    os.makedirs(folder_path, exist_ok=True)           # Create folder if it doesn’t exist
                    shutil.move(file_path, os.path.join(folder_path, filename))  # Move the file
                    moved = True
                    break
            # If it didn't match any known types, move it to "Others"
            if not moved:
                other_path = os.path.join(source_folder, "Others")
                os.makedirs(other_path, exist_ok=True)
                shutil.move(file_path, os.path.join(other_path, filename))
# Run the function when script is started
if __name__ == "__main__":
    organize_files() 
    print("✅ Files organized!")
