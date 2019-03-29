#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 19:34:45 2019

@author: rahul
"""

    

filename='student_grades.csv'
fh=open(filename)
let=[]
for line in fh:
    print(line.strip())
    for letter in line:
        let.append(letter)
        for item in let:
            if item==',':
                item='.'
print(let)