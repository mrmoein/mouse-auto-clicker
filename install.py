import os
import sys
from pathlib import Path

cur_path = sys.path[0]

os.system("pip3 install -U pip wheel setuptools")
os.system("pip3 install -r {}/requirements.txt".format(cur_path))

desktop_file = '{}/.local/share/applications/mouse-auto-clicker.desktop'.format(Path.home())

file = open(desktop_file, 'w+')
file.write('''[Desktop Entry]
Name=Mouse Auto Clicker
Version=3.0
Comment=Mouse Auto Clicker
Exec=python3 {}/main.py
Icon={}/images/mouse-icon.png
Terminal=false
Type=Application
'''.format(cur_path, cur_path))
print('Desktop file created at "{}"'.format(desktop_file))
