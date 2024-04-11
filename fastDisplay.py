#!/usr/bin/env python3
import config  # type: ignore
import easygui
from easygui import *
outfile= config.text_path
def fastDisplay():
    with open(outfile, "r+") as data:
            message= data.read() 
            data.close()     
    title = "Fast Note 1.0"
    ok_btn_txt = "Continue"
    easygui.msgbox(message, title, ok_btn_txt)
fastDisplay()
