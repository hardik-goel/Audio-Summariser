import os


def delete_files(folder_path):
    try:
        files = os.listdir(folder_path)
        for file_name in files:
            file_path = os.path.join(folder_path, file_name)
            if os.path.isfile(file_path):
                os.remove(file_path)
        print("All files deleted successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
