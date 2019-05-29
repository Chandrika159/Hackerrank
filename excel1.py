#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 25 13:50:17 2019

@author: chandrika
"""

def col_to_num(col_str):
    """ Convert base26 column string to number. """
    expn = 0
    col_num = 0
    for char in reversed(col_str):
        col_num += (ord(char) - ord('A') + 1) * (26 ** expn)
        expn += 1
    return col_num
s=input("enter column name(Capital):")
print(col_to_num(s))
