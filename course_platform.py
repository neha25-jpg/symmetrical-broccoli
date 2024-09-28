import os
import shutil

# Directory to store course resources
RESOURCE_DIR = 'course_resources'

# Create the directory if it doesn't exist
if not os.path.exists(RESOURCE_DIR):
    os.makedirs(RESOURCE_DIR)

# Function to upload a file
def upload_file():
    file_path = input("Enter the path of the file to upload: ")
    
    if not os.path.exists(file_path):
        print("File does not exist. Please try again.")
        return
    
    try:
        file_name = os.path.basename(file_path)
        shutil.copy(file_path, os.path.join(RESOURCE_DIR, file_name))
        print(f"File '{file_name}' uploaded successfully.")
    except Exception as e:
        print(f"Error during file upload: {e}")

# Function to list available resources
def list_files():
    files = os.listdir(RESOURCE_DIR)
    
    if not files:
        print("No resources available.")
        return
    
    print("Available resources:")
    for idx, file in enumerate(files, start=1):
        print(f"{idx}. {file}")

# Function to download a file
def download_file():
    list_files()
    file_idx = input("\nEnter the number of the file you want to download: ")
    
    try:
        files = os.listdir(RESOURCE_DIR)
        file_choice = files[int(file_idx) - 1]
        destination_path = input(f"Enter the destination path to save '{file_choice}': ")
        shutil.copy(os.path.join(RESOURCE_DIR, file_choice), destination_path)
        print(f"File '{file_choice}' downloaded successfully to {destination_path}.")
    except (IndexError, ValueError):
        print("Invalid file choice.")
    except Exception as e:
        print(f"Error during file download: {e}")

# Function to display the main menu
def display_menu():
    print("\nCourse Resource Sharing Platform")
    print("1. Upload a new resource")
    print("2. List available resources")
    print("3. Download a resource")
    print("4. Exit")

# Main program loop
def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            upload_file()
        elif choice == '2':
            list_files()
        elif choice == '3':
            download_file()
        elif choice == '4':
            print("Exiting the platform.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()