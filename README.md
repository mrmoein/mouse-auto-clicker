# mouse auto clicker

simple gui linux and windows mouse auto clicker with python3 and PyQt

### Usage
download or clone the project: `git clone https://github.com/mrmoein/mouse-auto-clicker.git`

install dependencies: 
```
pip3 install PyQt5
sudo apt-get install python3-pyqt5
pip3 install keybind
pip3 install pynput
```
run `main.py`
```
cd mouse-auto-clicker
python3 main.py
```

### screenshots
![mouse auto clicker by Moein Aghamirzaei](https://raw.githubusercontent.com/mrmoein/mouse-auto-clicker/main/Screenshot.png)

#### adding launcher for fast access
open a terminal and run this 
```
nano ~/.local/share/applications/mouse-auto-clicker.desktop
```
paste this into nano editor
```
[Desktop Entry]
Name= mouse auto clicker
Comment= simple gui linux and windows mouse auto clicker with python3 and PyQt By Moein Aghamirzaei
Exec= python3 /path/to/directory/main.py
Icon= /path/to/directory/mouse-icon.png
Terminal=false
Type=Application
StartupNotify=true
```
note: replace `/path/to/directory` with current application path

![Screenshot-launcher](https://raw.githubusercontent.com/mrmoein/mouse-auto-clicker/main/Screenshot-launcher.png)
