#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 11:26:54 2018

@author: m.ruscheweyh
"""
import os
from subprocess import call
print(os.getcwd() + "\n")
outdir = "output/msmc/";
input_directory = "/data/home/users/m.ruscheweyh/pythontest/input/"
hap_mad = list(range(28))
hap_mad1 = hap_mad[0:1]
for filename in os.listdir(input_directory):
    if filename.endswith(".multihetsep.txt"):
        call (["./msmc_1.1.0_linux64bit","-I",hap_mad1,"-p1*2+15*1+1*2","-o",outdir+filename,filename])
    else:
         print("Specify valid input files.")
    
    