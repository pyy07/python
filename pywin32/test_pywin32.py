#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import win32gui
from ctypes import *

def get_mouse_pos():
	x,y = win32gui.GetCursorPos()
	return x,y

def move_mouse(x, y):
	windll.user32.SetCursorPos(x, y)

print(get_mouse_pos())
move_mouse(40, 40)