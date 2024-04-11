#!/usr/bin/env python3
import subprocess
import sys
import pathlib
def prep():
    print("Include the full path to the text file for fastnote")
    try:
        txt_location = input("full PATH: ").strip()
        file1 = open('config.py', 'w')
        file1.write('text_path='+"'"+txt_location+"'")
        file1.close()
    except Exception as e:
        print(e)
 
# Writing a string to file


def commando(name):
    paff=pathlib.Path().resolve()
    path=str(paff)
    # defining keys & strings to be used
    key = "org.gnome.settings-daemon.plugins.media-keys custom-keybindings"
    subkey1 = key.replace(" ", ".")[:-1]+":"
    item_s = "/"+key.replace(" ", "/").replace(".", "/")+"/"
    firstname = "custom"
    # get the current list of custom shortcuts
    get = lambda cmd: subprocess.check_output(["/bin/bash", "-c", cmd]).decode("utf-8")
    array_str = get("gsettings get "+key)
    # in case the array was empty, remove the annotation hints
    command_result = array_str.lstrip("@as")
    current = eval(command_result)
    # make sure the additional keybinding mention is no duplicate
    n = 0
    while True:
        new = item_s+firstname+str(n)+"/"
        if new in current:
            n = n+1
        else:
            
            break
    # add the new keybinding to the list
    current.append(new)
    # create the shortcut, set the name, command and shortcut key
    cmd0 = 'gsettings set '+key+' "'+str(current)+'"'
    cmd1 = 'gsettings set '+subkey1+new+" name '"+name[0]+"'"
    cmd2 = 'gsettings set '+subkey1+new+" command '"+'python3'+' '+path+'/'+name[1]+"'"
    cmd3 = 'gsettings set '+subkey1+new+" binding '"+name[2]+"'"
    for cmd in [cmd0, cmd1, cmd2, cmd3]:
        subprocess.call(["/bin/bash", "-c", cmd])
#commands = ['fnclear','fndisplay','fndash']
fnclear=['fnclear','fastnoteclear.py','<Super>n']
fndisplay=['fndisplay','fastDisplay.py','<Ctrl><Shift>s']
fastnote=['fastnote','fastnote.py','<Ctrl><Shift>c']
prep()
commando(fnclear)
commando(fndisplay)
commando(fastnote)

print("done")


        