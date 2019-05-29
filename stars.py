#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 18 14:52:04 2019

@author: chandrika
"""

counter1=0
counter2=5
while(counter1 < 5):
  star=""
  while(counter2>counter1):
     star=star+"*"
     counter2+=1
     print(star)
counter1+=1