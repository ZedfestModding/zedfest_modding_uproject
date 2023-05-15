import os

def open_downloads_folder():
    # Get the user's home directory
    home_dir = os.path.expanduser('~')

    # Get the path to the Downloads folder
    downloads_dir = os.path.join(home_dir, 'Downloads')

    # Open the Downloads folder using the default file manager
    os.startfile(downloads_dir)

open_downloads_folder()


quit()
