#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 11:26:54 2018

@author: m.ruscheweyh
"""
import os
from subprocess import call
print(os.getcwd() + "\n")
outdir = "output/";
input_directory = "/data/home/users/m.ruscheweyh/pythontest/input/"
haplotypes_madeira = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]
for filename in os.listdir(input_directory):
    if filename.endswith(".multihetsep.txt"):
        call (["./msmc2_linux64bit","-I0,1","-p1*2+15*1+1*2","-o",outdir+filename,filename])
    else:
         print("Specify valid input files.")