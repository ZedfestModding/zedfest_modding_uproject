import os
import sys
import time
import psutil
import shutil
import subprocess
from pathlib import Path

os.chdir(os.path.dirname(sys.argv[0]))

process_list = (
    "Fmodel.exe",
    "umodel.exe",
    "umodel_64.exe",
    "Zedfest.exe",
)


def is_process_running(process_name):
    for proc in psutil.process_iter():
        try:
            if process_name.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False


def find_zedfest_install_folder():
    game_name = "Zedfest"
    steam_install_dir = os.path.join(os.environ['ProgramFiles(x86)'], 'Steam')
    zedfest_executable = 'Zedfest.exe'

    for root, dirs, files in os.walk(steam_install_dir):
        if game_name in dirs:
            game_install_dir = os.path.join(root, game_name)
            if os.path.exists(os.path.join(game_install_dir, 'KevinSpel', 'Binaries', 'Win64', zedfest_executable)):
                return game_install_dir

    return None


def find_mod_name():
    text_file = f"{os.path.dirname(os.path.dirname(os.getcwd()))}\\storage\\mod_name.txt"
    with open(text_file) as f:
        mod_name = f.readline()
    return mod_name


for process in process_list:
    if is_process_running(process):
        os.system(f"taskkill /f /im {process}")

time.sleep(1)

pak_mod_name = find_mod_name()
zedfest_install_location = find_zedfest_install_folder()

old_pak_base = r"\\KevinSpel\\Content\\Paks\\LogicMods\\"
new_pak_base = f"{os.path.dirname(os.path.dirname(os.getcwd()))}\\output\\WindowsNoEditor\\KevinSpel\\Content\\Paks"

old_framework_pak_location = f"{zedfest_install_location}{old_pak_base}ModdingFramework_P.pak"
new_framework_pak_location = os.path.join(new_pak_base, "pakchunk1-WindowsNoEditor.pak")
old_framework_pak_location = Path(old_framework_pak_location)
new_framework_pak_location = Path(new_framework_pak_location)

if old_framework_pak_location.is_file():
    old_framework_pak_location.unlink()
shutil.copy(new_framework_pak_location, old_framework_pak_location)

old_testing_pak_location = f"{zedfest_install_location}{old_pak_base}{pak_mod_name}.pak"
new_testing_pak_location = os.path.join(new_pak_base, "pakchunk2-WindowsNoEditor.pak")
old_testing_pak_location = Path(old_testing_pak_location)
new_testing_pak_location = Path(new_testing_pak_location)

if old_testing_pak_location.is_file():
    old_testing_pak_location.unlink()
shutil.copy(new_testing_pak_location, old_testing_pak_location)

time.sleep(1)

game_exe = os.path.join(zedfest_install_location, "KevinSpel", "Binaries", "Win64", "Zedfest.exe")
subprocess.Popen(game_exe)

quit()
