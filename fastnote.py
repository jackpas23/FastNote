#!/usr/bin/env python3
import pyperclip # type: ignore
import easygui
import config # type: ignore

print(help)
from easygui import *
##inital path
outfile= config.text_path
def txtPaste(text,outfile):
    with open(outfile, "a") as fhandle:
            fhandle.write(f'{text}\n')
            fhandle.close()
            return

def changeOut(clipboard_text):
    myvar = easygui.enterbox("select 1 to choose new output file")
    if myvar == '1':
        myvar = easygui.enterbox("enter full text file path")
        path = myvar
        txtPaste(clipboard_text,path)
clipboard_text = pyperclip.paste()
txtPaste(clipboard_text,outfile)







 
 



