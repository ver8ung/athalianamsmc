#!/usr/bin/env python3.6
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

hap_counter = 1     # counter for iteration over haplotype combinations, determines file output prefix, default prefix "01_"
index_counter = 0   # counters for the -I parameter of MSMC, iterates over x-amount of haplotypes in pairs of x-indexes
index_counter_1 = 1 #######################################################################################################
index_counter_2 = 2 #######################################################################################################
index_counter_3 = 3 #######################################################################################################
index_counter_4 = 4 #######################################################################################################
index_counter_5 = 5 #######################################################################################################
index_counter_6 = 6 #######################################################################################################
index_counter_7 = 7 #######################################################################################################

index_input = "%s,%s" %(index_counter,index_counter_1) # currently obsolete

for filename in os.listdir(input_directory): # retrieve filenames in input_directory for output prefix
    if filename.endswith(".multihetsep.txt"): # call MSMC2 with desired parameters on specified input files
      while hap_counter < 27:
              outputprefix = filename[:23] + '.msmc2'   # use only desired positions of input filenames as output prefix
              call (["./msmc2_linux64bit","-I","%s,%s" %(index_counter,index_counter_1),"-p1*2+15*1+1*2","--fixedRecombination","-o",outdir+'2hap_fixeddef'+'%02d_%s' %(hap_counter,outputprefix),filename])
              hap_counter += 1
              index_counter += 2
              index_counter_1 += 2    
      else:
              hap_counter = 1
              index_counter = 0
              index_counter_1 = 1
              continue
            
    if filename.endswith("_reduced.multihetsep.txt"): # call MSMC2 with desired parameters on specified input files
        while hap_counter < 27:
              outputprefix = filename[:31]
              call (["./msmc2_linux64bit","-I","%s,%s" %(index_counter,index_counter_1),"-p1*2+15*1+1*2","--fixedRecombination","-o",outdir+'2hap_fixeddef_nocent'+'%02d_%s' %(hap_counter,outputprefix),filename])
              hap_counter += 1
              index_counter += 2
              index_counter_1 += 2    
        else:
             hap_counter = 1
             index_counter = 0
             index_counter_1 = 1
             continue
    
    else:   
        print("Specify valid input files.")