#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 14:50:26 2017

@author: root
"""

f = open('code.csv')
code = []
while 1:
    line = f.readline().strip()
    if not line:
        break
    code.append(line)
        
f.close()
code_dict = {}
for i in xrange(len(code)):
    [value, key] = code[i].split(',')
    code_dict.update({key:value})
    


    