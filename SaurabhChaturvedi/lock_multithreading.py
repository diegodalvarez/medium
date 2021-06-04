# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 21:39:42 2020

@author: Diego
"""


from threading import Lock, Thread

lock = Lock()
g = 0

def add_one():
    
    gl