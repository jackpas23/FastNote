import subprocess
import sys
import pathlib

def install_dependencies():
    print("\nInstalling required Python packages...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

def prep():
    print("\nWelcome to FastNote Setup!")
    print("----------------------------")
    print("To get started, provide the full path to the text file for FastNote.")
    print("Press ENTER for easy installation with a default path.")
    print("Example of a full path: /home/username/Documents/notes.txt")
    
    flavor = input("Are you using Kali(1) or Ubuntu(2)?: ").strip()
    while flavor not in ["1", "2"]:
        flavor = input("Please enter 1 for Kali or 2 for Ubuntu: ").strip()

    txt_location = input("Enter full path (or press ENTER for default): ").strip()
    if not txt_location:
        txt_location = str(pathlib.Path().resolve() / 'fast.txt')

    with open('config.py', 'w') as file:
        file.write(f'text_path="{txt_location}"')

    return flavor

def ubuntu(name):
    key = "org.gnome.settings-daemon.plugins.media-keys.custom-keybindings"
    subkey = "org.gnome.settings-daemon.plugins.media-keys.custom-keybindings"
    item_s = "/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/"
    
    get = lambda cmd: subprocess.check_output(["/bin/bash", "-c", cmd]).decode("utf-8")
    current = eval(get(f"gsettings get {key}").lstrip("@as"))

    n = 0
    while True:
        new = f"{item_s}custom{n}/"
        if new in current:
            n += 1
        else:
            break
    
    current.append(new)
    commands = [
        f'gsettings set {key} "{str(current)}"',
        f"gsettings set {subkey}:{new} name '{name[0]}'",
        f"gsettings set {subkey}:{new} command 'python3 {pathlib.Path().resolve()}/{name[1]}'",
        f"gsettings set {subkey}:{new} binding '{name[2]}'"
    ]
    for cmd in commands:
        subprocess.call(["/bin/bash", "-c", cmd])

def linux(name):
    path = str(pathlib.Path().resolve())
    cmd = f"xfconf-query -c xfce4-keyboard-shortcuts -p '/commands/custom/{name[2]}' -n -t string -s 'python3 {path}/{name[1]}'"
    subprocess.call(["/bin/bash", "-c", cmd])

def main():
    install_dependencies()
    distro = prep()
    if distro == "2":
        for name in [fnclear, fndisplay, fastnote]:
            ubuntu(name)
    elif distro == "1":
        for name in [fnclear, fndisplay, fastnote]:
            linux(name)

fnclear = ['fnclear', 'fastnoteclear.py', '<Super>n']
fndisplay = ['fndisplay', 'fastDisplay.py', '<Ctrl><Shift>s']
fastnote = ['fastnote', 'fastnote.py', '<Ctrl><Shift>c']

if __name__ == '__main__':
    main()
    print("Ctrl+Shift+s to display your FNs")
    print("Ctrl+Shift+c to forward your clipboard to your FN")
    print("Super+n to clear your FNs")
    print("SPACE or ESC to exit FN display")
