
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
cmd= "./msmc_1.1.0_linux64bit"
for filename in os.listdir(input_directory):
       if filename.endswith(".multihetsep.txt"):
            call (["./msmc_1.1.0_linux64bit","-I0,1","-p1*2+15*1+1*2","-o",outdir+filename,filename])
            call (["./msmc_1.1.0_linux64bit","-I2,3","-p1*2+15*1+1*2","-o",outdir+filename,filename])
            call (["./msmc_1.1.0_linux64bit","-I4,5","-p1*2+15*1+1*2","-o",outdir+filename,filename])
            call (["./msmc_1.1.0_linux64bit","-I6,7","-p1*2+15*1+1*2","-o",outdir+filename,filename])
            call (["./msmc_1.1.0_linux64bit","-I8,9","-p1*2+15*1+1*2","-o",outdir+filename,filename])
            call (["./msmc_1.1.0_linux64bit","-I10,11","-p1*2+15*1+1*2","-o",outdir+filename,filename])
            call (["./msmc_1.1.0_linux64bit","-I12,13","-p1*2+15*1+1*2","-o",outdir+filename,filename])
            call (["./msmc_1.1.0_linux64bit","-I14,15","-p1*2+15*1+1*2","-o",outdir+filename,filename])
            call (["./msmc_1.1.0_linux64bit","-I16,17","-p1*2+15*1+1*2","-o",outdir+filename,filename])
            call (["./msmc_1.1.0_linux64bit","-I18,19","-p1*2+15*1+1*2","-o",outdir+filename,filename])
            call (["./msmc_1.1.0_linux64bit","-I20,21","-p1*2+15*1+1*2","-o",outdir+filename,filename])
            call (["./msmc_1.1.0_linux64bit","-I22,23","-p1*2+15*1+1*2","-o",outdir+filename,filename])
            call (["./msmc_1.1.0_linux64bit","-I24,25","-p1*2+15*1+1*2","-o",outdir+filename,filename])
            call (["./msmc_1.1.0_linux64bit","-I24,25","-p1*2+15*1+1*2","-o",outdir+filename,filename])
            call (["./msmc_1.1.0_linux64bit","-I26,27","-p1*2+15*1+1*2","-o",outdir+filename,filename])
    else:
        print("Specify valid input files.")