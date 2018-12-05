#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 11:26:54 2018
@author: m.ruscheweyh
"""
import os
from subprocess import call
  
input_directory = "/data/home/users/m.ruscheweyh/pythontest/input/" # specify input directory
outdir = "output/msmc/"; # specifies output directory
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
    if filename.endswith(".multihetsep.txt"): # call MSMC with desired parameters on specified input files
      while hap_counter < 27:
              outputprefix = filename[:24]   # use only desired positions of input filenames as output prefix
              call (["./msmc_1.1.0_linux64bit","-I","%s,%s" %(index_counter,index_counter_1),"-p1*2+15*1+1*2","-R","-o",outdir+'2hap_fixeddef'+'%02d_%s' %(hap_counter,outputprefix),input_directory+filename])
              hap_counter += 1
              index_counter += 2
              index_counter_1 += 2
      else:
              hap_counter = 1
              index_counter = 0
              index_counter_1 = 1
              break

for filename in os.listdir(input_directory): # retrieve filenames in input_directory for output prefix
    if filename.endswith(".multihetsep.txt"): # call MSMC with desired parameters on specified input files
      while hap_counter < 27:
              outputprefix = filename[:24]   # use only desired positions of input filenames as output prefix
              call (["./msmc_1.1.0_linux64bit","-I","%s,%s,%s,%s" %(index_counter,index_counter_1,index_counter_2,index_counter_3),"-p1*2+15*1+1*2","-R","-o",outdir+'4hap_fixeddef'+'%02d_%s' %(hap_counter,outputprefix),input_directory+filename])
              hap_counter += 1
              index_counter += 2
              index_counter_1 += 2
              index_counter_2 += 2
              index_counter_3 += 2
      else:
              hap_counter = 1
              index_counter = 0
              index_counter_1 = 1
              index_counter_2 = 2
              index_counter_3 = 3
              break
  
for filename in os.listdir(input_directory): # retrieve filenames in input_directory for output prefix          
    if filename.endswith(".multihetsep.txt"): # call MSMC with desired parameters on specified input files
          while hap_counter < 27:
              outputprefix = filename[:24]   # use only desired positions of input filenames as output prefix
              call (["./msmc_1.1.0_linux64bit","-I","%s,%s,%s,%s,%s,%s" %(index_counter,index_counter_1,index_counter_2,index_counter_3,index_counter_4,index_counter_5),"-p1*2+15*1+1*2","-R","-o",outdir+'6hap_fixeddef'+'%02d_%s' %(hap_counter,outputprefix),input_directory+filename])
              hap_counter += 1
              index_counter += 2
              index_counter_1 += 2
              index_counter_2 += 2
              index_counter_3 += 2
              index_counter_4 += 2
              index_counter_5 += 2
          else:
              hap_counter = 1
              index_counter = 0
              index_counter_1 = 1
              index_counter_2 = 2
              index_counter_3 = 3
              index_counter_4 = 4
              index_counter_5 = 5
              break
 
for filename in os.listdir(input_directory): # retrieve filenames in input_directory for output prefix           
    if filename.endswith(".multihetsep.txt"): # call MSMC with desired parameters on specified input files
          while hap_counter < 27:
              outputprefix = filename[:24]   # use only desired positions of input filenames as output prefix
              call (["./msmc_1.1.0_linux64bit","-I","%s,%s,%s,%s,%s,%s,%s,%s" %(index_counter,index_counter_1,index_counter_2,index_counter_3,index_counter_4,index_counter_5,index_counter_6,index_counter_7),"-p1*2+15*1+1*2","-R","-o",outdir+'8hap_fixeddef'+'%02d_%s' %(hap_counter,outputprefix),input_directory+filename])
              hap_counter += 1
              index_counter += 2
              index_counter_1 += 2
              index_counter_2 += 2
              index_counter_3 += 2
              index_counter_4 += 2
              index_counter_5 += 2
              index_counter_6 += 2
              index_counter_7 += 2
          else:
              hap_counter = 1
              index_counter = 0
              index_counter_1 = 1
              index_counter_2 = 2
              index_counter_3 = 3
              index_counter_4 = 4
              index_counter_5 = 5
              index_counter_6 = 6
              index_counter_7 = 7
              break       
 
for filename in os.listdir(input_directory): # retrieve filenames in input_directory for output prefix           
    if filename.endswith(".multihetsep_reduced.txt"): # call MSMC with desired parameters on specified input files
        while hap_counter < 27:
              outputprefix = filename[:32]
              call (["./msmc_1.1.0_linux64bit","-I","%s,%s" %(index_counter,index_counter_1),"-p1*2+15*1+1*2","-R","-o",outdir+'2hap_fixeddef_nocent'+'%02d_%s' %(hap_counter,outputprefix),input_directory+filename])
              hap_counter += 1
              index_counter += 2
              index_counter_1 += 2    
        else:
              hap_counter = 1
              index_counter = 0
              index_counter_1 = 1
              break
 
for filename in os.listdir(input_directory): # retrieve filenames in input_directory for output prefix       
    if filename.endswith(".multihetsep_reduced.txt"): # call MSMC with desired parameters on specified input files
      while hap_counter < 27:
              outputprefix = filename[:32]   # use only desired positions of input filenames as output prefix
              call (["./msmc_1.1.0_linux64bit","-I","%s,%s,%s,%s" %(index_counter,index_counter_1,index_counter_2,index_counter_3),"-p1*2+15*1+1*2","-R","-o",outdir+'4hap_fixeddef_nocent'+'%02d_%s' %(hap_counter,outputprefix),input_directory+filename])
              hap_counter += 1
              index_counter += 2
              index_counter_1 += 2
              index_counter_2 += 2
              index_counter_3 += 2
      else:
              hap_counter = 1
              index_counter = 0
              index_counter_1 = 1
              index_counter_2 = 2
              index_counter_3 = 3
              break

for filename in os.listdir(input_directory): # retrieve filenames in input_directory for output prefix            
    if filename.endswith(".multihetsep_reduced.txt"): # call MSMC with desired parameters on specified input files
          while hap_counter < 27:
              outputprefix = filename[:32]   # use only desired positions of input filenames as output prefix
              call (["./msmc_1.1.0_linux64bit","-I","%s,%s,%s,%s,%s,%s" %(index_counter,index_counter_1,index_counter_2,index_counter_3,index_counter_4,index_counter_5),"-p1*2+15*1+1*2","-R","-o",outdir+'6hap_fixeddef_reduced'+'%02d_%s' %(hap_counter,outputprefix),input_directory+filename])
              hap_counter += 1
              index_counter += 2
              index_counter_1 += 2
              index_counter_2 += 2
              index_counter_3 += 2
              index_counter_4 += 2
              index_counter_5 += 2
          else:
              hap_counter = 1
              index_counter = 0
              index_counter_1 = 1
              index_counter_2 = 2
              index_counter_3 = 3
              index_counter_4 = 4
              index_counter_5 = 5
              break

for filename in os.listdir(input_directory): # retrieve filenames in input_directory for output prefix          
    if filename.endswith(".multihetsep_reduced.txt"): # call MSMC with desired parameters on specified input files
          while hap_counter < 27:
              outputprefix = filename[:32]   # use only desired positions of input filenames as output prefix
              call (["./msmc_1.1.0_linux64bit","-I","%s,%s,%s,%s,%s,%s,%s,%s" %(index_counter,index_counter_1,index_counter_2,index_counter_3,index_counter_4,index_counter_5,index_counter_6,index_counter_7),"-p1*2+15*1+1*2","-R","-o",outdir+'8hap_fixeddef_reduced'+'%02d_%s' %(hap_counter,outputprefix),input_directory+filename])
              hap_counter += 1
              index_counter += 2
              index_counter_1 += 2
              index_counter_2 += 2
              index_counter_3 += 2
              index_counter_4 += 2
              index_counter_5 += 2
              index_counter_6 += 2
              index_counter_7 += 2
          else:
              hap_counter = 1
              index_counter = 0
              index_counter_1 = 1
              index_counter_2 = 2
              index_counter_3 = 3
              index_counter_4 = 4
              index_counter_5 = 5
              index_counter_6 = 6
              index_counter_7 = 7
              break       

    else:   
        print("Specify valid input files.")