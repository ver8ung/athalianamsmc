#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 11:26:54 2018
@author: m.ruscheweyh
"""
import os
from subprocess import call
  
outdir = "output/msmc/";
input_directory = "/data/home/users/m.ruscheweyh/pythontest/input/"
hap_counter = 1
index_counter = 0
index_counter_1 = 1
index_input = "%s,%s" %(index_counter,index_counter_1)

for filename in os.listdir(input_directory):
    if filename.endswith(".multihetsep.txt"):
            outputprefix = filename[:23]
            call (["./msmc_1.1.0_linux64bit","-I","%s,%s" %(index_counter,index_counter_1),"-p1*2+15*1+1*2","-o",outdir+'2hap'+'%02d_%s' %(hap_counter,outputprefix),filename])
            hap_counter += 1
            index_counter += 2
            index_counter_1 += 2
            call (["./msmc_1.1.0_linux64bit","-I","%s,%s" %(index_counter,index_counter_1),"-p1*2+15*1+1*2","-o",outdir+'2hap'+'%02d_%s' %(hap_counter,outputprefix),filename])
            hap_counter+= 1
            index_counter+= 2
            index_counter_1+= 2
            call (["./msmc_1.1.0_linux64bit","-I","%s,%s" %(index_counter,index_counter_1),"-p1*2+15*1+1*2","-o",outdir+'2hap'+'%02d_%s' %(hap_counter,outputprefix),filename])
            hap_counter+= 1
            index_counter+= 2
            index_counter_1+= 2
            call (["./msmc_1.1.0_linux64bit","-I","%s,%s" %(index_counter,index_counter_1),"-p1*2+15*1+1*2","-o",outdir+'2hap'+'%02d_%s' %(hap_counter,outputprefix),filename])
            hap_counter+= 1
            index_counter+= 2
            index_counter_1+= 2
            call (["./msmc_1.1.0_linux64bit","-I","%s,%s" %(index_counter,index_counter_1),"-p1*2+15*1+1*2","-o",outdir+'2hap'+'%02d_%s'%(hap_counter,outputprefix),filename])
            hap_counter+= 1
            index_counter+= 2
            index_counter_1+= 2
            call (["./msmc_1.1.0_linux64bit","-I","%s,%s" %(index_counter,index_counter_1),"-p1*2+15*1+1*2","-o",outdir+'2hap'+'%02d_%s'%(hap_counter,outputprefix),filename])
            hap_counter+= 1
            index_counter+= 2
            index_counter_1+= 2
            call (["./msmc_1.1.0_linux64bit","-I","%s,%s" %(index_counter,index_counter_1),"-p1*2+15*1+1*2","-o",outdir+'2hap'+'%02d_%s'%(hap_counter,outputprefix),filename])
            hap_counter+= 1
            index_counter+= 2
            index_counter_1+= 2
            call (["./msmc_1.1.0_linux64bit","-I","%s,%s" %(index_counter,index_counter_1),"-p1*2+15*1+1*2","-o",outdir+'2hap'+'%02d_%s'%(hap_counter,outputprefix),filename])
            hap_counter+= 1
            index_counter+= 2
            index_counter_1+= 2
            call (["./msmc_1.1.0_linux64bit","-I","%s,%s" %(index_counter,index_counter_1),"-p1*2+15*1+1*2","-o",outdir+'2hap'+'%02d_%s'%(hap_counter,outputprefix),filename])
            hap_counter+= 1
            index_counter+= 2
            index_counter_1+= 2
            call (["./msmc_1.1.0_linux64bit","-I","%s,%s" %(index_counter,index_counter_1),"-p1*2+15*1+1*2","-o",outdir+'2hap'+'%02d_%s'%(hap_counter,outputprefix),filename])
            hap_counter+= 1
            index_counter+= 2
            index_counter_1+= 2
            call (["./msmc_1.1.0_linux64bit","-I","%s,%s" %(index_counter,index_counter_1),"-p1*2+15*1+1*2","-o",outdir+'2hap'+'%02d_%s'%(hap_counter,outputprefix),filename])
            hap_counter+= 1
            index_counter+= 2
            index_counter_1+= 2
            call (["./msmc_1.1.0_linux64bit","-I","%s,%s" %(index_counter,index_counter_1),"-p1*2+15*1+1*2","-o",outdir+'2hap'+'%02d_%s'%(hap_counter,outputprefix),filename])
            hap_counter+= 1
            index_counter+= 2
            index_counter_1+= 2
            call (["./msmc_1.1.0_linux64bit","-I","%s,%s" %(index_counter,index_counter_1),"-p1*2+15*1+1*2","-o",outdir+'2hap'+'%02d_%s'%(hap_counter,outputprefix),filename])
            hap_counter+= 1
            index_counter+= 2
            index_counter_1+= 2
            call (["./msmc_1.1.0_linux64bit","-I","%s,%s" %(index_counter,index_counter_1),"-p1*2+15*1+1*2","-o",outdir+'2hap'+'%02d_%s'%(hap_counter,outputprefix),filename])
            hap_counter = 1
            index_counter = 0
            index_counter_1 = 1
    else:
        print("Specify valid input files.")