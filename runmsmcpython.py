#!/usr/bin/env python
# -*- coding: utf-8 -*-
#$ -N python_MSMC1_fixedRecombination_singlechr
#$ -M max.ruscheweyh@tum.de
#$-cwd
"""
Created on Thu Nov 29 11:26:54 2018
@author: m.ruscheweyh
"""
import os, glob
from subprocess import call
  
input_directory = "/data/home/users/m.ruscheweyh/pythontest/input/" # specify input directory
input_rho_1 = "/data/home/users/m.ruscheweyh/pythontest/input/chr1/"
input_rho_2 = "/data/home/users/m.ruscheweyh/pythontest/input/chr2/"
input_rho_3 = "/data/home/users/m.ruscheweyh/pythontest/input/chr3/"
input_rho_4 = "/data/home/users/m.ruscheweyh/pythontest/input/chr4/"
input_rho_5 = "/data/home/users/m.ruscheweyh/pythontest/input/chr5/"
all_chr_input_madeira = glob.glob("/data/home/users/m.ruscheweyh/pythontest/input/madeira*.multihetsep.txt")
all_chr_input_madeira_reduced = glob.glob("/data/home/users/m.ruscheweyh/pythontest/input/madeira*.multihetsep_reduced.txt")
all_chr_input_spain = glob.glob("/data/home/users/m.ruscheweyh/pythontest/input/spain*.multihetsep.txt")
all_chr_input_spain_reduced = glob.glob("/data/home/users/m.ruscheweyh/pythontest/input/spain*.multihetsep_reduced.txt")
all_chr_input_swedenn = glob.glob("/data/home/users/m.ruscheweyh/pythontest/input/swedenn*.multihetsep.txt")
all_chr_input_swedenn_reduced = glob.glob("/data/home/users/m.ruscheweyh/pythontest/input/swedenn*.multihetsep_reduced.txt")
all_chr_input_swedens = glob.glob("/data/home/users/m.ruscheweyh/pythontest/input/swedens*.multihetsep.txt")
all_chr_input_swedens_reduced = glob.glob("/data/home/users/m.ruscheweyh/pythontest/input/swedens*.multihetsep_reduced.txt")
all_chr_input_tubingenha = glob.glob("/data/home/users/m.ruscheweyh/pythontest/input/tubingenha*.multihetsep.txt")
all_chr_input_tubingenha_reduced = glob.glob("/data/home/users/m.ruscheweyh/pythontest/input/tubingenha*.multihetsep_reduced.txt")
all_chr_input_tubingencent = glob.glob("/data/home/users/m.ruscheweyh/pythontest/input/tubingencent*.multihetsep.txt")
all_chr_input_tubingencent_reduced = glob.glob("/data/home/users/m.ruscheweyh/pythontest/input/tubingencent*.multihetsep_reduced.txt")
all_chr_input_tubingeneastlust = glob.glob("/data/home/users/m.ruscheweyh/pythontest/input/tubingeneastlust*.multihetsep.txt")
all_chr_input_tubingeneastlust_reduced = glob.glob("/data/home/users/m.ruscheweyh/pythontest/input/tubingeneastlust*.multihetsep_reduced.txt")
outdir = "output/msmc/"; # specifies output directory
outdir_rho = "output/msmc/rho_runs/"
outdir_allchr = "output/msmc/allchr"
hap_counter = 1     # counter for iteration over haplotype combinations, determines file output prefix, default prefix "01_"
index_counter = 0   # counters for the -I parameter of MSMC, iterates over x-amount of haplotypes in pairs of x-indexes
index_counter_1 = 1 #######################################################################################################
index_counter_2 = 2 #######################################################################################################
index_counter_3 = 3 #######################################################################################################
index_counter_4 = 4 #######################################################################################################
index_counter_5 = 5 #######################################################################################################
index_counter_6 = 6 #######################################################################################################
index_counter_7 = 7 #######################################################################################################

r_chr1 = 4.587
r_chr2 = 5.1429
r_chr3 = 5
r_chr4 = 5.4286
r_chr5 = 5.1429
r_average =  5.1143

for filename in os.listdir(input_directory): # retrieve filenames in input_directory for output prefix
    if filename.endswith(".multihetsep.txt"): # call MSMC with desired parameters on specified input files
      while hap_counter < 27:
              outputprefix = filename[:14]   # use only desired positions of input filenames as output prefix
              call (["./msmc_1.1.0_linux64bit","-I","%s,%s" %(index_counter,index_counter_1),"-p1*2+15*1+1*2","-R","-o",outdir+'2hap_fixeddef'+'%02d_%s' %(hap_counter,outputprefix),input_directory+filename])
              hap_counter += 1
              index_counter += 2
              index_counter_1 += 2
              continue
      else:
              hap_counter = 1
              index_counter = 0
              index_counter_1 = 1
              continue
          
    if filename.endswith(".multihetsep.txt"): # call MSMC with desired parameters on specified input files
      while hap_counter < 27:
              outputprefix = filename[:14]   # use only desired positions of input filenames as output prefix
              call (["./msmc_1.1.0_linux64bit","-I","%s,%s,%s,%s" %(index_counter,index_counter_1,index_counter_2,index_counter_3),"-p1*2+15*1+1*2","-R","-o",outdir+'4hap_fixeddef'+'%02d_%s' %(hap_counter,outputprefix),input_directory+filename])
              hap_counter += 1
              index_counter += 4
              index_counter_1 += 4
              index_counter_2 += 4
              index_counter_3 += 4
              continue
      else:
              hap_counter = 1
              index_counter = 0
              index_counter_1 = 1
              index_counter_2 = 2
              index_counter_3 = 3
              continue
      
    if filename.endswith(".multihetsep.txt"): # call MSMC with desired parameters on specified input files
          while hap_counter < 27:
              outputprefix = filename[:14]   # use only desired positions of input filenames as output prefix
              call (["./msmc_1.1.0_linux64bit","-I","%s,%s,%s,%s,%s,%s" %(index_counter,index_counter_1,index_counter_2,index_counter_3,index_counter_4,index_counter_5),"-p1*2+15*1+1*2","-R","-o",outdir+'6hap_fixeddef'+'%02d_%s' %(hap_counter,outputprefix),input_directory+filename])
              hap_counter += 1
              index_counter += 2
              index_counter_1 += 6
              index_counter_2 += 6
              index_counter_3 += 6
              index_counter_4 += 6
              index_counter_5 += 6
              continue
          else:
              hap_counter = 1
              index_counter = 0
              index_counter_1 = 1
              index_counter_2 = 2
              index_counter_3 = 3
              index_counter_4 = 4
              index_counter_5 = 5
              continue
           
    if filename.endswith(".multihetsep.txt"): # call MSMC with desired parameters on specified input files
          while hap_counter < 27:
              outputprefix = filename[:14]   # use only desired positions of input filenames as output prefix
              call (["./msmc_1.1.0_linux64bit","-I","%s,%s,%s,%s,%s,%s,%s,%s" %(index_counter,index_counter_1,index_counter_2,index_counter_3,index_counter_4,index_counter_5,index_counter_6,index_counter_7),"-p1*2+15*1+1*2","-R","-o",outdir+'8hap_fixeddef'+'%02d_%s' %(hap_counter,outputprefix),input_directory+filename])
              hap_counter += 1
              index_counter += 2
              index_counter_1 += 8
              index_counter_2 += 8
              index_counter_3 += 8
              index_counter_4 += 8
              index_counter_5 += 8
              index_counter_6 += 8
              index_counter_7 += 8
              continue
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
              continue 
          
    if filename.endswith(".multihetsep_reduced.txt"): # call MSMC with desired parameters on specified input files
        while hap_counter < 27:
              outputprefix = filename[:31]
              call (["./msmc_1.1.0_linux64bit","-I","%s,%s" %(index_counter,index_counter_1),"-p1*2+15*1+1*2","-R","-o",outdir+'2hap_fixeddef_nocent'+'%02d_%s' %(hap_counter,outputprefix),input_directory+filename])
              hap_counter += 1
              index_counter += 2
              index_counter_1 += 2
              continue
        else:
              hap_counter = 1
              index_counter = 0
              index_counter_1 = 1
              continue
 
for filename in os.listdir(input_directory): # retrieve filenames in input_directory for output prefix       
    if filename.endswith(".multihetsep_reduced.txt"): # call MSMC with desired parameters on specified input files
      while hap_counter < 27:
              outputprefix = filename[:31]   # use only desired positions of input filenames as output prefix
              call (["./msmc_1.1.0_linux64bit","-I","%s,%s,%s,%s" %(index_counter,index_counter_1,index_counter_2,index_counter_3),"-p1*2+15*1+1*2","-R","-o",outdir+'4hap_fixeddef_nocent'+'%02d_%s' %(hap_counter,outputprefix),input_directory+filename])
              hap_counter += 1
              index_counter += 4
              index_counter_1 += 4
              index_counter_2 += 4
              index_counter_3 += 4
              continue
      else:
              hap_counter = 1
              index_counter = 0
              index_counter_1 = 1
              index_counter_2 = 2
              index_counter_3 = 3
              continue
          
    if filename.endswith(".multihetsep_reduced.txt"): # call MSMC with desired parameters on specified input files
          while hap_counter < 27:
              outputprefix = filename[:31]   # use only desired positions of input filenames as output prefix
              call (["./msmc_1.1.0_linux64bit","-I","%s,%s,%s,%s,%s,%s" %(index_counter,index_counter_1,index_counter_2,index_counter_3,index_counter_4,index_counter_5),"-p1*2+15*1+1*2","-R","-o",outdir+'6hap_fixeddef_nocent'+'%02d_%s' %(hap_counter,outputprefix),input_directory+filename])
              hap_counter += 1
              index_counter += 6
              index_counter_1 += 6
              index_counter_2 += 6
              index_counter_3 += 6
              index_counter_4 += 6
              index_counter_5 += 6
              continue
          else:
              hap_counter = 1
              index_counter = 0
              index_counter_1 = 1
              index_counter_2 = 2
              index_counter_3 = 3
              index_counter_4 = 4
              index_counter_5 = 5
              continue
          
    if filename.endswith(".multihetsep_reduced.txt"): # call MSMC with desired parameters on specified input files
          while hap_counter < 27:
              outputprefix = filename[:31]   # use only desired positions of input filenames as output prefix
              call (["./msmc_1.1.0_linux64bit","-I","%s,%s,%s,%s,%s,%s,%s,%s" %(index_counter,index_counter_1,index_counter_2,index_counter_3,index_counter_4,index_counter_5,index_counter_6,index_counter_7),"-p1*2+15*1+1*2","-R","-o",outdir+'8hap_fixeddef_nocent'+'%02d_%s' %(hap_counter,outputprefix),input_directory+filename])
              hap_counter += 1
              index_counter += 8
              index_counter_1 += 8
              index_counter_2 += 8
              index_counter_3 += 8
              index_counter_4 += 8
              index_counter_5 += 8
              index_counter_6 += 8
              index_counter_7 += 8
              continue
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
              continue
          
##########################################################################################################################################################################################################################################################################################################################################
################Runs with chromosome specific rhoOverMu###################################################################################################################################################################################################################################################################################
for filename in os.listdir(input_rho_1): # retrieve filenames in input_directory for output prefix
    if filename.endswith(".multihetsep.txt"): # call MSMC with desired parameters on specified input files
      while hap_counter < 27:
              outputprefix = filename[:11]   # use only desired positions of input filenames as output prefix
              call (["./msmc_1.1.0_linux64bit","-I","%s,%s" %(index_counter,index_counter_1),"-p1*2+15*1+1*2","-R","-r",str(r_chr1),"-o",outdir_rho+'2hap_rhofixed'+'%02d_%s' %(hap_counter,outputprefix),input_rho_1+filename])
              hap_counter += 1
              index_counter += 2
              index_counter_1 += 2
              continue
      else:
              hap_counter = 1
              index_counter = 0
              index_counter_1 = 1
              continue

for filename in os.listdir(input_rho_2): # retrieve filenames in input_directory for output prefix
    if filename.endswith(".multihetsep.txt"): # call MSMC with desired parameters on specified input files
      while hap_counter < 27:
              outputprefix = filename[:11]   # use only desired positions of input filenames as output prefix
              call (["./msmc_1.1.0_linux64bit","-I","%s,%s" %(index_counter,index_counter_1),"-p1*2+15*1+1*2","-R","-r",str(r_chr2),"-o",outdir_rho+'2hap_rhofixed'+'%02d_%s' %(hap_counter,outputprefix),input_rho_2+filename])
              hap_counter += 1
              index_counter += 2
              index_counter_1 += 2
              continue
      else:
              hap_counter = 1
              index_counter = 0
              index_counter_1 = 1
              continue
          
for filename in os.listdir(input_rho_3): # retrieve filenames in input_directory for output prefix
    if filename.endswith(".multihetsep.txt"): # call MSMC with desired parameters on specified input files
      while hap_counter < 27:
              outputprefix = filename[:11]   # use only desired positions of input filenames as output prefix
              call (["./msmc_1.1.0_linux64bit","-I","%s,%s" %(index_counter,index_counter_1),"-p1*2+15*1+1*2","-R","-r",str(r_chr3),"-o",outdir_rho+'2hap_rhofixed'+'%02d_%s' %(hap_counter,outputprefix),input_rho_3+filename])
              hap_counter += 1
              index_counter += 2
              index_counter_1 += 2
              continue
      else:
              hap_counter = 1
              index_counter = 0
              index_counter_1 = 1
              continue

for filename in os.listdir(input_rho_4): # retrieve filenames in input_directory for output prefix
    if filename.endswith(".multihetsep.txt"): # call MSMC with desired parameters on specified input files
      while hap_counter < 27:
              outputprefix = filename[:11]   # use only desired positions of input filenames as output prefix
              call (["./msmc_1.1.0_linux64bit","-I","%s,%s" %(index_counter,index_counter_1),"-p1*2+15*1+1*2","-R","-r",str(r_chr4),"-o",outdir_rho+'2hap_rhofixed'+'%02d_%s' %(hap_counter,outputprefix),input_rho_4+filename])
              hap_counter += 1
              index_counter += 2
              index_counter_1 += 2
              continue
      else:
              hap_counter = 1
              index_counter = 0
              index_counter_1 = 1
              continue
          
for filename in os.listdir(input_rho_5): # retrieve filenames in input_directory for output prefix
    if filename.endswith(".multihetsep.txt"): # call MSMC with desired parameters on specified input files
      while hap_counter < 27:
              outputprefix = filename[:11]   # use only desired positions of input filenames as output prefix
              call (["./msmc_1.1.0_linux64bit","-I","%s,%s" %(index_counter,index_counter_1),"-p1*2+15*1+1*2","-R","-r",str(r_chr5),"-o",outdir_rho+'2hap_rhofixed'+'%02d_%s' %(hap_counter,outputprefix),input_rho_5+filename])
              hap_counter += 1
              index_counter += 2
              index_counter_1 += 2
              continue
      else:
              hap_counter = 1
              index_counter = 0
              index_counter_1 = 1
              continue

for filename in os.listdir(input_rho_1): # retrieve filenames in input_directory for output prefix
    if filename.endswith(".multihetsep.txt"): # call MSMC with desired parameters on specified input files
      while hap_counter < 27:
              outputprefix = filename[:11]   # use only desired positions of input filenames as output prefix
              call (["./msmc_1.1.0_linux64bit","-I","%s,%s" %(index_counter,index_counter_1),"-p1*2+15*1+1*2","-r",str(r_chr1),"-o",outdir_rho+'2hap_rho'+'%02d_%s' %(hap_counter,outputprefix),input_rho_1+filename])
              hap_counter += 1
              index_counter += 2
              index_counter_1 += 2
              continue
      else:
              hap_counter = 1
              index_counter = 0
              index_counter_1 = 1
              continue
    
for filename in os.listdir(input_rho_2): # retrieve filenames in input_directory for output prefix
    if filename.endswith(".multihetsep.txt"): # call MSMC with desired parameters on specified input files
      while hap_counter < 27:
              outputprefix = filename[:11]   # use only desired positions of input filenames as output prefix
              call (["./msmc_1.1.0_linux64bit","-I","%s,%s" %(index_counter,index_counter_1),"-p1*2+15*1+1*2","-r",str(r_chr2),"-o",outdir_rho+'2hap_rho'+'%02d_%s' %(hap_counter,outputprefix),input_rho_2+filename])
              hap_counter += 1
              index_counter += 2
              index_counter_1 += 2
              continue
      else:
              hap_counter = 1
              index_counter = 0
              index_counter_1 = 1
              continue

for filename in os.listdir(input_rho_3): # retrieve filenames in input_directory for output prefix
    if filename.endswith(".multihetsep.txt"): # call MSMC with desired parameters on specified input files
      while hap_counter < 27:
              outputprefix = filename[:11]   # use only desired positions of input filenames as output prefix
              call (["./msmc_1.1.0_linux64bit","-I","%s,%s" %(index_counter,index_counter_1),"-p1*2+15*1+1*2","-r",str(r_chr3),"-o",outdir_rho+'2hap_rho'+'%02d_%s' %(hap_counter,outputprefix),input_rho_3+filename])
              hap_counter += 1
              index_counter += 2
              index_counter_1 += 2
              continue
      else:
              hap_counter = 1
              index_counter = 0
              index_counter_1 = 1
              continue

for filename in os.listdir(input_rho_4): # retrieve filenames in input_directory for output prefix
    if filename.endswith(".multihetsep.txt"): # call MSMC with desired parameters on specified input files
      while hap_counter < 27:
              outputprefix = filename[:11]   # use only desired positions of input filenames as output prefix
              call (["./msmc_1.1.0_linux64bit","-I","%s,%s" %(index_counter,index_counter_1),"-p1*2+15*1+1*2","-r",str(r_chr4),"-o",outdir_rho+'2hap_rho'+'%02d_%s' %(hap_counter,outputprefix),input_rho_4+filename])
              hap_counter += 1
              index_counter += 2
              index_counter_1 += 2
              continue
      else:
              hap_counter = 1
              index_counter = 0
              index_counter_1 = 1
              continue

for filename in os.listdir(input_rho_5): # retrieve filenames in input_directory for output prefix
    if filename.endswith(".multihetsep.txt"): # call MSMC with desired parameters on specified input files
      while hap_counter < 27:
              outputprefix = filename[:11]   # use only desired positions of input filenames as output prefix
              call (["./msmc_1.1.0_linux64bit","-I","%s,%s" %(index_counter,index_counter_1),"-p1*2+15*1+1*2","-r",str(r_chr5),"-o",outdir_rho+'2hap_rho'+'%02d_%s' %(hap_counter,outputprefix),input_rho_5+filename])
              hap_counter += 1
              index_counter += 2
              index_counter_1 += 2
              continue
      else:
              hap_counter = 1
              index_counter = 0
              index_counter_1 = 1
              continue
   
for filename in os.listdir(input_rho_1): # retrieve filenames in input_directory for output prefix
    if filename.endswith(".multihetsep.txt"): # call MSMC with desired parameters on specified input files
      while hap_counter < 27:
              outputprefix = filename[:11]   # use only desired positions of input filenames as output prefix
              call (["./msmc_1.1.0_linux64bit","-I","%s,%s,%s,%s" %(index_counter,index_counter_1,index_counter_3,index_counter_4),"-p1*2+15*1+1*2","-R","-r",str(r_chr1),"-o",outdir_rho+'4hap_rhofixed'+'%02d_%s' %(hap_counter,outputprefix),input_rho_1+filename])
              hap_counter += 1
              index_counter += 4
              index_counter_1 += 4
              index_counter_2 += 4
              index_counter_3 += 4
              continue
      else:
              hap_counter = 1
              index_counter = 0
              index_counter_1 = 1
              index_counter_2 = 2
              index_counter_3 = 3
              continue

for filename in os.listdir(input_rho_2): # retrieve filenames in input_directory for output prefix
    if filename.endswith(".multihetsep.txt"): # call MSMC with desired parameters on specified input files
      while hap_counter < 27:
              outputprefix = filename[:11]   # use only desired positions of input filenames as output prefix
              call (["./msmc_1.1.0_linux64bit","-I","%s,%s,%s,%s" %(index_counter,index_counter_1,index_counter_3,index_counter_4),"-p1*2+15*1+1*2","-R","-r",str(r_chr2),"-o",outdir_rho+'4hap_rhofixed'+'%02d_%s' %(hap_counter,outputprefix),input_rho_2+filename])
              hap_counter += 1
              index_counter += 4
              index_counter_1 += 4
              index_counter_2 += 4
              index_counter_3 += 4
              continue
      else:
              hap_counter = 1
              index_counter = 0
              index_counter_1 = 1
              index_counter_2 = 2
              index_counter_3 = 3
              continue
          
for filename in os.listdir(input_rho_3): # retrieve filenames in input_directory for output prefix
    if filename.endswith(".multihetsep.txt"): # call MSMC with desired parameters on specified input files
      while hap_counter < 27:
              outputprefix = filename[:11]   # use only desired positions of input filenames as output prefix
              call (["./msmc_1.1.0_linux64bit","-I","%s,%s,%s,%s" %(index_counter,index_counter_1,index_counter_3,index_counter_4),"-p1*2+15*1+1*2","-R","-r",str(r_chr3),"-o",outdir_rho+'4hap_rhofixed'+'%02d_%s' %(hap_counter,outputprefix),input_rho_3+filename])
              hap_counter += 1
              index_counter += 4
              index_counter_1 += 4
              index_counter_2 += 4
              index_counter_3 += 4
              continue
      else:
              hap_counter = 1
              index_counter = 0
              index_counter_1 = 1
              index_counter_2 = 2
              index_counter_3 = 3
              continue

for filename in os.listdir(input_rho_4): # retrieve filenames in input_directory for output prefix
    if filename.endswith(".multihetsep.txt"): # call MSMC with desired parameters on specified input files
      while hap_counter < 27:
              outputprefix = filename[:11]   # use only desired positions of input filenames as output prefix
              call (["./msmc_1.1.0_linux64bit","-I","%s,%s,%s,%s" %(index_counter,index_counter_1,index_counter_3,index_counter_4),"-p1*2+15*1+1*2","-R","-r",str(r_chr4),"-o",outdir_rho+'4hap_rhofixed'+'%02d_%s' %(hap_counter,outputprefix),input_rho_4+filename])
              hap_counter += 1
              index_counter += 4
              index_counter_1 += 4
              index_counter_2 += 4
              index_counter_3 += 4
              continue
      else:
              hap_counter = 1
              index_counter = 0
              index_counter_2 = 2
              index_counter_3 = 3
              index_counter_1 = 1
              continue
          
for filename in os.listdir(input_rho_5): # retrieve filenames in input_directory for output prefix
    if filename.endswith(".multihetsep.txt"): # call MSMC with desired parameters on specified input files
      while hap_counter < 27:
              outputprefix = filename[:11]   # use only desired positions of input filenames as output prefix
              call (["./msmc_1.1.0_linux64bit","-I","%s,%s,%s,%s" %(index_counter,index_counter_1,index_counter_3,index_counter_4),"-p1*2+15*1+1*2","-R","-r",str(r_chr5),"-o",outdir_rho+'4hap_rhofixed'+'%02d_%s' %(hap_counter,outputprefix),input_rho_5+filename])
              hap_counter += 1
              index_counter += 4
              index_counter_1 += 4
              index_counter_2 += 4
              index_counter_3 += 4
              continue
      else:
              hap_counter = 1
              index_counter = 0
              index_counter_1 = 1
              index_counter_2 = 2
              index_counter_3 = 3
              continue

for filename in os.listdir(input_rho_1): # retrieve filenames in input_directory for output prefix
    if filename.endswith(".multihetsep.txt"): # call MSMC with desired parameters on specified input files
      while hap_counter < 27:
              outputprefix = filename[:11]   # use only desired positions of input filenames as output prefix
              call (["./msmc_1.1.0_linux64bit","-I","%s,%s,%s,%s" %(index_counter,index_counter_1,index_counter_3,index_counter_4),"-p1*2+15*1+1*2","-r",str(r_chr1),"-o",outdir_rho+'4hap_rho'+'%02d_%s' %(hap_counter,outputprefix),input_rho_1+filename])
              hap_counter += 1
              index_counter += 4
              index_counter_1 += 4
              index_counter_2 += 4
              index_counter_3 += 4
              continue
      else:
              hap_counter = 1
              index_counter = 0
              index_counter_1 = 1
              index_counter_2 = 2
              index_counter_3 = 3
              continue
    
for filename in os.listdir(input_rho_2): # retrieve filenames in input_directory for output prefix
    if filename.endswith(".multihetsep.txt"): # call MSMC with desired parameters on specified input files
      while hap_counter < 27:
              outputprefix = filename[:11]   # use only desired positions of input filenames as output prefix
              call (["./msmc_1.1.0_linux64bit","-I","%s,%s,%s,%s" %(index_counter,index_counter_1,index_counter_3,index_counter_4),"-p1*2+15*1+1*2","-r",str(r_chr2),"-o",outdir_rho+'4hap_rho'+'%02d_%s' %(hap_counter,outputprefix),input_rho_2+filename])
              hap_counter += 1
              index_counter += 4
              index_counter_1 += 4
              index_counter_2 += 4
              index_counter_3 += 4
              continue
      else:
              hap_counter = 1
              index_counter = 0
              index_counter_1 = 1
              index_counter_2 = 2
              index_counter_3 = 3
              continue

for filename in os.listdir(input_rho_3): # retrieve filenames in input_directory for output prefix
    if filename.endswith(".multihetsep.txt"): # call MSMC with desired parameters on specified input files
      while hap_counter < 27:
              outputprefix = filename[:11]   # use only desired positions of input filenames as output prefix
              call (["./msmc_1.1.0_linux64bit","-I","%s,%s,%s,%s" %(index_counter,index_counter_1,index_counter_3,index_counter_4),"-p1*2+15*1+1*2","-r",str(r_chr3),"-o",outdir_rho+'4hap_rho'+'%02d_%s' %(hap_counter,outputprefix),input_rho_3+filename])
              hap_counter += 1
              index_counter += 4
              index_counter_1 += 4
              index_counter_2 += 4
              index_counter_3 += 4
              continue
      else:
              hap_counter = 1
              index_counter = 0
              index_counter_1 = 1
              index_counter_2 = 2
              index_counter_3 = 3
              continue

for filename in os.listdir(input_rho_4): # retrieve filenames in input_directory for output prefix
    if filename.endswith(".multihetsep.txt"): # call MSMC with desired parameters on specified input files
      while hap_counter < 27:
              outputprefix = filename[:11]   # use only desired positions of input filenames as output prefix
              call (["./msmc_1.1.0_linux64bit","-I","%s,%s,%s,%s" %(index_counter,index_counter_1,index_counter_3,index_counter_4),"-p1*2+15*1+1*2","-r",str(r_chr4),"-o",outdir_rho+'4hap_rho'+'%02d_%s' %(hap_counter,outputprefix),input_rho_4+filename])
              hap_counter += 1
              index_counter += 4
              index_counter_1 += 4
              index_counter_2 += 4
              index_counter_3 += 4
              continue
      else:
              hap_counter = 1
              index_counter = 0
              index_counter_1 = 1
              index_counter_2 = 2
              index_counter_3 = 3
              continue

for filename in os.listdir(input_rho_5): # retrieve filenames in input_directory for output prefix
    if filename.endswith(".multihetsep.txt"): # call MSMC with desired parameters on specified input files
      while hap_counter < 27:
              outputprefix = filename[:11]   # use only desired positions of input filenames as output prefix
              call (["./msmc_1.1.0_linux64bit","-I","%s,%s,%s,%s" %(index_counter,index_counter_1,index_counter_3,index_counter_4),"-p1*2+15*1+1*2","-r",str(r_chr5),"-o",outdir_rho+'4hap_rho'+'%02d_%s' %(hap_counter,outputprefix),input_rho_5+filename])
              hap_counter += 1
              index_counter += 4
              index_counter_1 += 4
              index_counter_2 += 4
              index_counter_3 += 4
              continue
      else:
              hap_counter = 1
              index_counter = 0
              index_counter_1 = 1
              index_counter_2 = 2
              index_counter_3 = 3
              continue

for filename in os.listdir(input_rho_1): # retrieve filenames in input_directory for output prefix
    if filename.endswith(".multihetsep.txt"): # call MSMC with desired parameters on specified input files
          while hap_counter < 27:
              outputprefix = filename[:14]   # use only desired positions of input filenames as output prefix
              call (["./msmc_1.1.0_linux64bit","-I","%s,%s,%s,%s,%s,%s" %(index_counter,index_counter_1,index_counter_2,index_counter_3,index_counter_4,index_counter_5),"-p1*2+15*1+1*2","-R","-r",str(r_chr1),"-o",outdir+'6hap_rhofixed'+'%02d_%s' %(hap_counter,outputprefix),input_rho_1+filename])
              hap_counter += 1
              index_counter += 2
              index_counter_1 += 6
              index_counter_2 += 6
              index_counter_3 += 6
              index_counter_4 += 6
              index_counter_5 += 6
              continue
          else:
              hap_counter = 1
              index_counter = 0
              index_counter_1 = 1
              index_counter_2 = 2
              index_counter_3 = 3
              index_counter_4 = 4
              index_counter_5 = 5
              continue

for filename in os.listdir(input_rho_2): # retrieve filenames in input_directory for output prefix
    if filename.endswith(".multihetsep.txt"): # call MSMC with desired parameters on specified input files
          while hap_counter < 27:
              outputprefix = filename[:14]   # use only desired positions of input filenames as output prefix
              call (["./msmc_1.1.0_linux64bit","-I","%s,%s,%s,%s,%s,%s" %(index_counter,index_counter_1,index_counter_2,index_counter_3,index_counter_4,index_counter_5),"-p1*2+15*1+1*2","-R","-r",str(r_chr2),"-o",outdir+'6hap_rhofixed'+'%02d_%s' %(hap_counter,outputprefix),input_rho_2+filename])
              hap_counter += 1
              index_counter += 2
              index_counter_1 += 6
              index_counter_2 += 6
              index_counter_3 += 6
              index_counter_4 += 6
              index_counter_5 += 6
              continue
          else:
              hap_counter = 1
              index_counter = 0
              index_counter_1 = 1
              index_counter_2 = 2
              index_counter_3 = 3
              index_counter_4 = 4
              index_counter_5 = 5
              continue
         
for filename in os.listdir(input_rho_3): # retrieve filenames in input_directory for output prefix
    if filename.endswith(".multihetsep.txt"): # call MSMC with desired parameters on specified input files
          while hap_counter < 27:
              outputprefix = filename[:14]   # use only desired positions of input filenames as output prefix
              call (["./msmc_1.1.0_linux64bit","-I","%s,%s,%s,%s,%s,%s" %(index_counter,index_counter_1,index_counter_2,index_counter_3,index_counter_4,index_counter_5),"-p1*2+15*1+1*2","-R","-r",str(r_chr3),"-o",outdir+'6hap_rhofixed'+'%02d_%s' %(hap_counter,outputprefix),input_rho_3+filename])
              hap_counter += 1
              index_counter += 2
              index_counter_1 += 6
              index_counter_2 += 6
              index_counter_3 += 6
              index_counter_4 += 6
              index_counter_5 += 6
              continue
          else:
              hap_counter = 1
              index_counter = 0
              index_counter_1 = 1
              index_counter_2 = 2
              index_counter_3 = 3
              index_counter_4 = 4
              index_counter_5 = 5
              continue

for filename in os.listdir(input_rho_4): # retrieve filenames in input_directory for output prefix
    if filename.endswith(".multihetsep.txt"): # call MSMC with desired parameters on specified input files
          while hap_counter < 27:
              outputprefix = filename[:14]   # use only desired positions of input filenames as output prefix
              call (["./msmc_1.1.0_linux64bit","-I","%s,%s,%s,%s,%s,%s" %(index_counter,index_counter_1,index_counter_2,index_counter_3,index_counter_4,index_counter_5),"-p1*2+15*1+1*2","-R","-r",str(r_chr4),"-o",outdir+'6hap_rhofixed'+'%02d_%s' %(hap_counter,outputprefix),input_rho_4+filename])
              hap_counter += 1
              index_counter += 2
              index_counter_1 += 6
              index_counter_2 += 6
              index_counter_3 += 6
              index_counter_4 += 6
              index_counter_5 += 6
              continue
          else:
              hap_counter = 1
              index_counter = 0
              index_counter_1 = 1
              index_counter_2 = 2
              index_counter_3 = 3
              index_counter_4 = 4
              index_counter_5 = 5
              continue

for filename in os.listdir(input_rho_5): # retrieve filenames in input_directory for output prefix
    if filename.endswith(".multihetsep.txt"): # call MSMC with desired parameters on specified input files
          while hap_counter < 27:
              outputprefix = filename[:14]   # use only desired positions of input filenames as output prefix
              call (["./msmc_1.1.0_linux64bit","-I","%s,%s,%s,%s,%s,%s" %(index_counter,index_counter_1,index_counter_2,index_counter_3,index_counter_4,index_counter_5),"-p1*2+15*1+1*2","-R","-r",str(r_chr5),"-o",outdir+'6hap_rhofixed'+'%02d_%s' %(hap_counter,outputprefix),input_rho_5+filename])
              hap_counter += 1
              index_counter += 2
              index_counter_1 += 6
              index_counter_2 += 6
              index_counter_3 += 6
              index_counter_4 += 6
              index_counter_5 += 6
              continue
          else:
              hap_counter = 1
              index_counter = 0
              index_counter_1 = 1
              index_counter_2 = 2
              index_counter_3 = 3
              index_counter_4 = 4
              index_counter_5 = 5
              continue

for filename in os.listdir(input_rho_1): # retrieve filenames in input_directory for output prefix
    if filename.endswith(".multihetsep.txt"): # call MSMC with desired parameters on specified input files
          while hap_counter < 27:
              outputprefix = filename[:14]   # use only desired positions of input filenames as output prefix
              call (["./msmc_1.1.0_linux64bit","-I","%s,%s,%s,%s,%s,%s" %(index_counter,index_counter_1,index_counter_2,index_counter_3,index_counter_4,index_counter_5),"-p1*2+15*1+1*2","-R","-r",str(r_chr1),"-o",outdir+'6hap_rho'+'%02d_%s' %(hap_counter,outputprefix),input_rho_1+filename])
              hap_counter += 1
              index_counter += 2
              index_counter_1 += 6
              index_counter_2 += 6
              index_counter_3 += 6
              index_counter_4 += 6
              index_counter_5 += 6
              continue
          else:
              hap_counter = 1
              index_counter = 0
              index_counter_1 = 1
              index_counter_2 = 2
              index_counter_3 = 3
              index_counter_4 = 4
              index_counter_5 = 5
              continue

for filename in os.listdir(input_rho_2): # retrieve filenames in input_directory for output prefix
    if filename.endswith(".multihetsep.txt"): # call MSMC with desired parameters on specified input files
          while hap_counter < 27:
              outputprefix = filename[:14]   # use only desired positions of input filenames as output prefix
              call (["./msmc_1.1.0_linux64bit","-I","%s,%s,%s,%s,%s,%s" %(index_counter,index_counter_1,index_counter_2,index_counter_3,index_counter_4,index_counter_5),"-p1*2+15*1+1*2","-R","-r",str(r_chr2),"-o",outdir+'6hap_rho'+'%02d_%s' %(hap_counter,outputprefix),input_rho_2+filename])
              hap_counter += 1
              index_counter += 2
              index_counter_1 += 6
              index_counter_2 += 6
              index_counter_3 += 6
              index_counter_4 += 6
              index_counter_5 += 6
              continue
          else:
              hap_counter = 1
              index_counter = 0
              index_counter_1 = 1
              index_counter_2 = 2
              index_counter_3 = 3
              index_counter_4 = 4
              index_counter_5 = 5
              continue

for filename in os.listdir(input_rho_3): # retrieve filenames in input_directory for output prefix
    if filename.endswith(".multihetsep.txt"): # call MSMC with desired parameters on specified input files
          while hap_counter < 27:
              outputprefix = filename[:14]   # use only desired positions of input filenames as output prefix
              call (["./msmc_1.1.0_linux64bit","-I","%s,%s,%s,%s,%s,%s" %(index_counter,index_counter_1,index_counter_2,index_counter_3,index_counter_4,index_counter_5),"-p1*2+15*1+1*2","-R","-r",str(r_chr3),"-o",outdir+'6hap_rho'+'%02d_%s' %(hap_counter,outputprefix),input_rho_3+filename])
              hap_counter += 1
              index_counter += 2
              index_counter_1 += 6
              index_counter_2 += 6
              index_counter_3 += 6
              index_counter_4 += 6
              index_counter_5 += 6
              continue
          else:
              hap_counter = 1
              index_counter = 0
              index_counter_1 = 1
              index_counter_2 = 2
              index_counter_3 = 3
              index_counter_4 = 4
              index_counter_5 = 5
              continue
         
for filename in os.listdir(input_rho_4): # retrieve filenames in input_directory for output prefix
    if filename.endswith(".multihetsep.txt"): # call MSMC with desired parameters on specified input files
          while hap_counter < 27:
              outputprefix = filename[:14]   # use only desired positions of input filenames as output prefix
              call (["./msmc_1.1.0_linux64bit","-I","%s,%s,%s,%s,%s,%s" %(index_counter,index_counter_1,index_counter_2,index_counter_3,index_counter_4,index_counter_5),"-p1*2+15*1+1*2","-R","-r",str(r_chr4),"-o",outdir+'6hap_rho'+'%02d_%s' %(hap_counter,outputprefix),input_rho_4+filename])
              hap_counter += 1
              index_counter += 2
              index_counter_1 += 6
              index_counter_2 += 6
              index_counter_3 += 6
              index_counter_4 += 6
              index_counter_5 += 6
              continue
          else:
              hap_counter = 1
              index_counter = 0
              index_counter_1 = 1
              index_counter_2 = 2
              index_counter_3 = 3
              index_counter_4 = 4
              index_counter_5 = 5
              continue

for filename in os.listdir(input_rho_5): # retrieve filenames in input_directory for output prefix
    if filename.endswith(".multihetsep.txt"): # call MSMC with desired parameters on specified input files
          while hap_counter < 27:
              outputprefix = filename[:14]   # use only desired positions of input filenames as output prefix
              call (["./msmc_1.1.0_linux64bit","-I","%s,%s,%s,%s,%s,%s" %(index_counter,index_counter_1,index_counter_2,index_counter_3,index_counter_4,index_counter_5),"-p1*2+15*1+1*2","-R","-r",str(r_chr5),"-o",outdir+'6hap_rho'+'%02d_%s' %(hap_counter,outputprefix),input_rho_5+filename])
              hap_counter += 1
              index_counter += 2
              index_counter_1 += 6
              index_counter_2 += 6
              index_counter_3 += 6
              index_counter_4 += 6
              index_counter_5 += 6
              continue
          else:
              hap_counter = 1
              index_counter = 0
              index_counter_1 = 1
              index_counter_2 = 2
              index_counter_3 = 3
              index_counter_4 = 4
              index_counter_5 = 5
              continue

for filename in os.listdir(input_rho_1): # retrieve filenames in input_directory for output prefix
    if filename.endswith(".multihetsep.txt"): # call MSMC with desired parameters on specified input files
          while hap_counter < 27:
              outputprefix = filename[:14]   # use only desired positions of input filenames as output prefix
              call (["./msmc_1.1.0_linux64bit","-I","%s,%s,%s,%s,%s,%s,%s,%s" %(index_counter,index_counter_1,index_counter_2,index_counter_3,index_counter_4,index_counter_5,index_counter_6,index_counter_7),"-p1*2+15*1+1*2","-R","-r",str(r_chr1),"-o",outdir+'8hap_rhofixed'+'%02d_%s' %(hap_counter,outputprefix),input_rho_1+filename])
              hap_counter += 1
              index_counter += 2
              index_counter_1 += 8
              index_counter_2 += 8
              index_counter_3 += 8
              index_counter_4 += 8
              index_counter_5 += 8
              index_counter_6 += 8
              index_counter_7 += 8
              continue
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
              continue 

for filename in os.listdir(input_rho_2): # retrieve filenames in input_directory for output prefix
    if filename.endswith(".multihetsep.txt"): # call MSMC with desired parameters on specified input files
          while hap_counter < 27:
              outputprefix = filename[:14]   # use only desired positions of input filenames as output prefix
              call (["./msmc_1.1.0_linux64bit","-I","%s,%s,%s,%s,%s,%s,%s,%s" %(index_counter,index_counter_1,index_counter_2,index_counter_3,index_counter_4,index_counter_5,index_counter_6,index_counter_7),"-p1*2+15*1+1*2","-R","-r",str(r_chr2),"-o",outdir+'8hap_rhofixed'+'%02d_%s' %(hap_counter,outputprefix),input_rho_2+filename])
              hap_counter += 1
              index_counter += 2
              index_counter_1 += 8
              index_counter_2 += 8
              index_counter_3 += 8
              index_counter_4 += 8
              index_counter_5 += 8
              index_counter_6 += 8
              index_counter_7 += 8
              continue
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
              continue 

for filename in os.listdir(input_rho_3): # retrieve filenames in input_directory for output prefix
    if filename.endswith(".multihetsep.txt"): # call MSMC with desired parameters on specified input files
          while hap_counter < 27:
              outputprefix = filename[:14]   # use only desired positions of input filenames as output prefix
              call (["./msmc_1.1.0_linux64bit","-I","%s,%s,%s,%s,%s,%s,%s,%s" %(index_counter,index_counter_1,index_counter_2,index_counter_3,index_counter_4,index_counter_5,index_counter_6,index_counter_7),"-p1*2+15*1+1*2","-R","-r",str(r_chr3),"-o",outdir+'8hap_rhofixed'+'%02d_%s' %(hap_counter,outputprefix),input_rho_3+filename])
              hap_counter += 1
              index_counter += 2
              index_counter_1 += 8
              index_counter_2 += 8
              index_counter_3 += 8
              index_counter_4 += 8
              index_counter_5 += 8
              index_counter_6 += 8
              index_counter_7 += 8
              continue
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
              continue 
          
for filename in os.listdir(input_rho_4): # retrieve filenames in input_directory for output prefix
    if filename.endswith(".multihetsep.txt"): # call MSMC with desired parameters on specified input files
          while hap_counter < 27:
              outputprefix = filename[:14]   # use only desired positions of input filenames as output prefix
              call (["./msmc_1.1.0_linux64bit","-I","%s,%s,%s,%s,%s,%s,%s,%s" %(index_counter,index_counter_1,index_counter_2,index_counter_3,index_counter_4,index_counter_5,index_counter_6,index_counter_7),"-p1*2+15*1+1*2","-R","-r",str(r_chr4),"-o",outdir+'8hap_rhofixedf'+'%02d_%s' %(hap_counter,outputprefix),input_rho_4+filename])
              hap_counter += 1
              index_counter += 2
              index_counter_1 += 8
              index_counter_2 += 8
              index_counter_3 += 8
              index_counter_4 += 8
              index_counter_5 += 8
              index_counter_6 += 8
              index_counter_7 += 8
              continue
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
              continue 

for filename in os.listdir(input_rho_5): # retrieve filenames in input_directory for output prefix
    if filename.endswith(".multihetsep.txt"): # call MSMC with desired parameters on specified input files
          while hap_counter < 27:
              outputprefix = filename[:14]   # use only desired positions of input filenames as output prefix
              call (["./msmc_1.1.0_linux64bit","-I","%s,%s,%s,%s,%s,%s,%s,%s" %(index_counter,index_counter_1,index_counter_2,index_counter_3,index_counter_4,index_counter_5,index_counter_6,index_counter_7),"-p1*2+15*1+1*2","-R","-r",str(r_chr5),"-o",outdir+'8hap_rhofixed'+'%02d_%s' %(hap_counter,outputprefix),input_rho_5+filename])
              hap_counter += 1
              index_counter += 2
              index_counter_1 += 8
              index_counter_2 += 8
              index_counter_3 += 8
              index_counter_4 += 8
              index_counter_5 += 8
              index_counter_6 += 8
              index_counter_7 += 8
              continue
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
              continue 
          
for filename in os.listdir(input_rho_1): # retrieve filenames in input_directory for output prefix
    if filename.endswith(".multihetsep.txt"): # call MSMC with desired parameters on specified input files
          while hap_counter < 27:
              outputprefix = filename[:14]   # use only desired positions of input filenames as output prefix
              call (["./msmc_1.1.0_linux64bit","-I","%s,%s,%s,%s,%s,%s,%s,%s" %(index_counter,index_counter_1,index_counter_2,index_counter_3,index_counter_4,index_counter_5,index_counter_6,index_counter_7),"-p1*2+15*1+1*2","-r",str(r_chr1),"-o",outdir+'8hap_rho'+'%02d_%s' %(hap_counter,outputprefix),input_directory+filename])
              hap_counter += 1
              index_counter += 2
              index_counter_1 += 8
              index_counter_2 += 8
              index_counter_3 += 8
              index_counter_4 += 8
              index_counter_5 += 8
              index_counter_6 += 8
              index_counter_7 += 8
              continue
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
              continue 

for filename in os.listdir(input_rho_2): # retrieve filenames in input_directory for output prefix
    if filename.endswith(".multihetsep.txt"): # call MSMC with desired parameters on specified input files
          while hap_counter < 27:
              outputprefix = filename[:14]   # use only desired positions of input filenames as output prefix
              call (["./msmc_1.1.0_linux64bit","-I","%s,%s,%s,%s,%s,%s,%s,%s" %(index_counter,index_counter_1,index_counter_2,index_counter_3,index_counter_4,index_counter_5,index_counter_6,index_counter_7),"-p1*2+15*1+1*2","-r",str(r_chr2),"-o",outdir+'8hap_rho'+'%02d_%s' %(hap_counter,outputprefix),input_directory+filename])
              hap_counter += 1
              index_counter += 2
              index_counter_1 += 8
              index_counter_2 += 8
              index_counter_3 += 8
              index_counter_4 += 8
              index_counter_5 += 8
              index_counter_6 += 8
              index_counter_7 += 8
              continue
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
              continue 

for filename in os.listdir(input_rho_3): # retrieve filenames in input_directory for output prefix
    if filename.endswith(".multihetsep.txt"): # call MSMC with desired parameters on specified input files
          while hap_counter < 27:
              outputprefix = filename[:14]   # use only desired positions of input filenames as output prefix
              call (["./msmc_1.1.0_linux64bit","-I","%s,%s,%s,%s,%s,%s,%s,%s" %(index_counter,index_counter_1,index_counter_2,index_counter_3,index_counter_4,index_counter_5,index_counter_6,index_counter_7),"-p1*2+15*1+1*2","-r",str(r_chr3),"-o",outdir+'8hap_rho'+'%02d_%s' %(hap_counter,outputprefix),input_directory+filename])
              hap_counter += 1
              index_counter += 2
              index_counter_1 += 8
              index_counter_2 += 8
              index_counter_3 += 8
              index_counter_4 += 8
              index_counter_5 += 8
              index_counter_6 += 8
              index_counter_7 += 8
              continue
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
              continue 
for filename in os.listdir(input_rho_4): # retrieve filenames in input_directory for output prefix
    if filename.endswith(".multihetsep.txt"): # call MSMC with desired parameters on specified input files
          while hap_counter < 27:
              outputprefix = filename[:14]   # use only desired positions of input filenames as output prefix
              call (["./msmc_1.1.0_linux64bit","-I","%s,%s,%s,%s,%s,%s,%s,%s" %(index_counter,index_counter_1,index_counter_2,index_counter_3,index_counter_4,index_counter_5,index_counter_6,index_counter_7),"-p1*2+15*1+1*2","-r",str(r_chr4),"-o",outdir+'8hap_rho'+'%02d_%s' %(hap_counter,outputprefix),input_directory+filename])
              hap_counter += 1
              index_counter += 2
              index_counter_1 += 8
              index_counter_2 += 8
              index_counter_3 += 8
              index_counter_4 += 8
              index_counter_5 += 8
              index_counter_6 += 8
              index_counter_7 += 8
              continue
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
              continue 

for filename in os.listdir(input_rho_5): # retrieve filenames in input_directory for output prefix
    if filename.endswith(".multihetsep.txt"): # call MSMC with desired parameters on specified input files
          while hap_counter < 27:
              outputprefix = filename[:14]   # use only desired positions of input filenames as output prefix
              call (["./msmc_1.1.0_linux64bit","-I","%s,%s,%s,%s,%s,%s,%s,%s" %(index_counter,index_counter_1,index_counter_2,index_counter_3,index_counter_4,index_counter_5,index_counter_6,index_counter_7),"-p1*2+15*1+1*2","-r",str(r_chr5),"-o",outdir+'8hap_rho'+'%02d_%s' %(hap_counter,outputprefix),input_directory+filename])
              hap_counter += 1
              index_counter += 2
              index_counter_1 += 8
              index_counter_2 += 8
              index_counter_3 += 8
              index_counter_4 += 8
              index_counter_5 += 8
              index_counter_6 += 8
              index_counter_7 += 8
              continue
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
              continue 

    else:   
        print("Specify valid input files.")