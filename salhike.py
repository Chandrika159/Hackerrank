#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 16 14:58:12 2019

@author: chandrika
"""

def find_new_salary(current_salary,job_level):
    # write your logic here
    if(job_level==3):
        new_salary=current_salary+(current_salary*15/100)
    if(job_level==4):
        new_salary=current_salary+(current_salary*7/100)
    if(job_level==5):
        new_salary=current_salary+(current_salary*5/100)
    return new_salary

new_salary=find_new_salary(15000,3)
print(new_salary)