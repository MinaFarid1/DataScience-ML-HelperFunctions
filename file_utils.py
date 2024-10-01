import os

def get_folder_size_in_gb(directory: str) -> float:
    """
    Calculate the total size of a folder and its subfolders in gigabytes.

    Parameters:
    directory (str): The path to the folder.

    Returns:
    float: The total size in gigabytes.
    """
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            # Add the size of the file to the total size
            total_size += os.path.getsize(file_path)
    
    # Convert bytes to gigabytes
    total_size_gb = total_size / (1024 ** 3)  # or total_size / 1073741824
    return total_size_gb