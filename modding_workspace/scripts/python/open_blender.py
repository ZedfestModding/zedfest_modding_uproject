import os
import subprocess

blender_path = None
latest_version = 0

# Search for Blender installations in the default installation directory
for root, dirs, files in os.walk('C:/Program Files/Blender Foundation/'):
    for dir in dirs:
        if dir.startswith('Blender '):
            version = dir[8:]
            try:
                version = float(version)
                if version > latest_version:
                    latest_version = version
                    blender_path = os.path.join(root, dir, 'blender.exe')
            except ValueError:
                pass

# Open the latest version of Blender found
if blender_path:
    subprocess.Popen([blender_path])
else:
    print('No Blender installation found.')
