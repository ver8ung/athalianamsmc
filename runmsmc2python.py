#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 15:30:09 2018
"""
import os
from subprocess import call
  
outdir = "output/msmc2/";
input_directory = "/data/home/users/m.ruscheweyh/pythontest/input/"
hap_counter = 1
index_counter = 0
index_counter_1 = 1
index_input = "%s,%s" %(index_counter,index_counter_1)

for filename in os.listdir(input_directory):
    if filename.endswith(".multihetsep.txt"):
            outputprefix = filename[:23]
            call (["./msmc2_linux64bit","-I",index_input,"-p1*2+15*1+1*2","-o",outdir+'2hap'+'%02d_%s' %(hap_counter,outputprefix),filename])
            hap_counter+= 1
            call (["./msmc2_linux64bit","-I2,3","-p1*2+15*1+1*2","-o",outdir+'2hap'+'%02d_%s' %(hap_counter,outputprefix),filename])
            hap_counter+= 1
            call (["./msmc2_linux64bit","-I4,5","-p1*2+15*1+1*2","-o",outdir+'2hap'+'%02d_%s' %(hap_counter,outputprefix),filename])
            hap_counter+= 1
            call (["./msmc2_linux64bit","-I6,7","-p1*2+15*1+1*2","-o",outdir+'2hap'+'%02d_%s' %(hap_counter,outputprefix),filename])
            hap_counter+= 1
            call (["./msmc2_linux64bit","-I8,9","-p1*2+15*1+1*2","-o",outdir+'2hap'+'%02d_%s'%(hap_counter,outputprefix),filename])
            hap_counter+= 1
            call (["./msmc2_linux64bit","-I10,11","-p1*2+15*1+1*2","-o",outdir+'2hap'+'%02d_%s'%(hap_counter,outputprefix),filename])
            hap_counter+= 1
            call (["./msmc2_linux64bit","-I12,13","-p1*2+15*1+1*2","-o",outdir+'2hap'+'%02d_%s'%(hap_counter,outputprefix),filename])
            hap_counter+= 1
            call (["./msmc2_linux64bit","-I14,15","-p1*2+15*1+1*2","-o",outdir+'2hap'+'%02d_%s'%(hap_counter,outputprefix),filename])
            hap_counter+= 1
            call (["./msmc2_linux64bit","-I16,17","-p1*2+15*1+1*2","-o",outdir+'2hap'+'%02d_%s'%(hap_counter,outputprefix),filename])
            hap_counter+= 1
            call (["./msmc2_linux64bit","-I18,19","-p1*2+15*1+1*2","-o",outdir+'2hap'+'%02d_%s'%(hap_counter,outputprefix),filename])
            hap_counter+= 1
            call (["./msmc2_linux64bit","-I20,21","-p1*2+15*1+1*2","-o",outdir+'2hap'+'%02d_%s'%(hap_counter,outputprefix),filename])
            hap_counter+= 1
            call (["./msmc2_linux64bit","-I22,23","-p1*2+15*1+1*2","-o",outdir+'2hap'+'%02d_%s'%(hap_counter,outputprefix),filename])
            hap_counter+= 1
            call (["./msmc2_linux64bit","-I24,25","-p1*2+15*1+1*2","-o",outdir+'2hap'+'%02d_%s'%(hap_counter,outputprefix),filename])
            hap_counter+= 1
            call (["./msmc2_linux64bit","-I26,27","-p1*2+15*1+1*2","-o",outdir+'2hap'+'%02d_%s'%(hap_counter,outputprefix),filename])
            hap_counter = 1
    else:
        print("Specify valid input files.")