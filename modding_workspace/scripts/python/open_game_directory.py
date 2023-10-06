import os
import subprocess

def find_game_install_location(game_name):
    steam_install_dir = os.path.join(os.environ['ProgramFiles(x86)'], 'Steam')
    zedfest_executable = 'Zedfest.exe'

    for root, dirs, files in os.walk(steam_install_dir):
        if game_name in dirs:
            game_install_dir = os.path.join(root, game_name)
            if os.path.exists(os.path.join(game_install_dir, 'KevinSpel', 'Binaries', 'Win64', zedfest_executable)):
                return game_install_dir

    return None

# Example usage for Zedfest game
game_name = "Zedfest"
zedfest_install_path = find_game_install_location(game_name)
if zedfest_install_path is not None:
    subprocess.Popen(f"explorer {zedfest_install_path}")
else:
    print("Failed to find Zedfest installation location.")


quit()
