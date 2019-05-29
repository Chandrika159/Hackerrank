#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 23 12:14:07 2019

@author: chandrika
"""

import enchant
from itertools import permutations
c=input("enter a word:")
perms=[''.join(p) for p in permutations(c)]

d=enchant.Dict("en_US")
for i in perms:
    if d.check(i):
        print(i)   
