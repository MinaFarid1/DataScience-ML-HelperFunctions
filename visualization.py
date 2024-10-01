import os
import random
import matplotlib.pyplot as plt
from PIL import Image

def print_folder_tree(directory: str, indent: str = "", include_files: bool = False) -> None:
    """
    Print the folder structure of a given directory.

    Parameters:
        directory (str): The path to the directory to display.
        indent (str): The string used for indentation (default is an empty string).
        include_files (bool): If True, include files in the printed output (default is False).
    
    Returns:
        None: This function prints the directory tree but does not return a value.
    """
    try:
        # Print the name of the current directory with a trailing slash
        print(indent + os.path.basename(directory) + "/")
        
        # Increase the indentation for contents of the current directory
        indent += "    " 
        
        # Use os.scandir to iterate through entries in the directory
        with os.scandir(directory) as entries:
            for entry in entries:
                # If the entry is a directory, recursively call this function
                if entry.is_dir():
                    print_folder_tree(entry.path, indent, include_files)
                # If the entry is a file and include_files is True, print its name
                elif include_files:
                    print(indent + entry.name)
    
    except FileNotFoundError:
        # Handle the case where the specified directory does not exist
        print(f"Error: The directory '{directory}' does not exist.")
def show_random_images(directory: str, n: int = 1):
    """
    Displays a random selection of images from a directory in rows with 5 images per row.

    Parameters:
        directory (str): The path to the directory containing images.
        n (int): The number of random images to display (default is 1).

    Returns:
        None: This function displays images and does not return a value.
    """
    try:
        # List all supported image files in the directory
        all_images = [f for f in os.listdir(directory) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
        
        # Select random images
        selected_images = random.sample(all_images, min(n, len(all_images)))
        
        # Setup figure dimensions based on 5 images per row
        cols = 5  # Number of images per row
        rows = (len(selected_images) + cols - 1) // cols  # Calculate required rows
        figure_width, figure_height = 3 * cols, 3 * rows
        plt.figure(figsize=(figure_width, figure_height))

        for i, img_file in enumerate(selected_images):
            img_path = os.path.join(directory, img_file)
            try:
                img = Image.open(img_path)
                plt.subplot(rows, cols, i + 1)
                plt.imshow(img)
                plt.axis('off')  # Hide axis
            except (IOError, OSError):
                print(f"Error: Could not open image: {img_path}")

        # Adjust layout for better spacing
        plt.tight_layout()
        plt.subplots_adjust(left=0.05, right=0.95, top=0.9, bottom=0.1, wspace=0.2, hspace=0.2)
        plt.show()
        
    except FileNotFoundError:
        print(f"Error: The directory '{directory}' does not exist.")
def count_files_in_directory(directory: str) -> int:
    """
    Counts the number of files in a directory (including files in subdirectories).

    Parameters:
        directory (str): The path to the directory.

    Returns:
        int: The number of files in the directory.
    """
    try:
        file_count = 0
        for _, _, filenames in os.walk(directory):
            file_count += len(filenames)
        return file_count
    except FileNotFoundError:
        print(f"Error: The directory '{directory}' does not exist.")