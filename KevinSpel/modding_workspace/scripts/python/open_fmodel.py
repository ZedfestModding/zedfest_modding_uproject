import os
import tempfile
import zipfile
import subprocess
import requests

def install_fmodel():
    # Check if fmodel is already installed
    install_dir = os.path.join(os.environ.get('ProgramFiles'), 'fmodel')
    if os.path.isfile(os.path.join(install_dir, 'fmodel.exe')):
        print('fmodel is already installed.')
        open_fmodel()
        return True
    
    # Download the ZIP file to a temporary directory
    zip_url = 'https://github.com/4sval/FModel/releases/download/4.4.2.0/FModel.zip'
    with requests.get(zip_url, stream=True) as r:
        r.raise_for_status()
        with tempfile.NamedTemporaryFile(delete=False) as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
            zip_file_path = f.name
    
    # Extract the contents of the ZIP file to a temporary directory
    with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
        tmp_dir = tempfile.mkdtemp(prefix='fmodel_')
        zip_file.extractall(tmp_dir)
    
    # Find the EXE file in the extracted contents
    exe_file_path = None
    for root, dirs, files in os.walk(tmp_dir):
        for file in files:
            if file.endswith('.exe'):
                exe_file_path = os.path.join(root, file)
                break
        if exe_file_path is not None:
            break
    
    if exe_file_path is None:
        print("Failed to find fmodel installer in ZIP file.")
        return False
    
    # Run the installer
    cmd = f'"{exe_file_path}" /S /D="{install_dir}"'
    print(f"Running fmodel installer located at {exe_file_path}")
    result = subprocess.run(cmd, capture_output=True, shell=True)
    
    if result.returncode != 0:
        print(f"Failed to install fmodel. Error output: {result.stderr.decode()}")
        return False
    else:
        print("fmodel installed successfully.")
        open_fmodel()
    
    # Delete the downloaded ZIP file and temporary directory
    os.remove(zip_file_path)
    for root, dirs, files in os.walk(tmp_dir, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    os.rmdir(tmp_dir)
    
    return True

def open_fmodel():
    # Check if fmodel is installed
    install_dir = os.path.join(os.environ.get('ProgramFiles'), 'fmodel')
    if os.path.isfile(os.path.join(install_dir, 'fmodel.exe')):
        print(f"Opening fmodel from {os.path.join(install_dir, 'fmodel.exe')}")
        os.startfile(os.path.join(install_dir, 'fmodel.exe'))
    else:
        print('fmodel is not installed.')
    
if __name__ == '__main__':
    install_fmodel()
