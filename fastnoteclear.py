#!/usr/bin/env python3
import config # type: ignore
from easygui import *
def clearTxt():
    open(config.text_path, 'w').close()
clearTxt()