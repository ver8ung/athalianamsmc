#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 14:08:46 2018

@author: m.ruscheweyh
"""
for filename in os.listdir(input_rho_1): # retrieve filenames in input_directory for output prefix
    if filename.endswith(".multihetsep.txt"): # call MSMC with desired parameters on specified input files
          while hap_counter < 27:
              outputprefix = filename[:14]   # use only desired positions of input filenames as output prefix
              call (["./msmc_1.1.0_linux64bit","-I","%s,%s,%s,%s,%s,%s,%s,%s" %(index_counter,index_counter_1,index_counter_2,index_counter_3,index_counter_4,index_counter_5,index_counter_6,index_counter_7),"-p1*2+15*1+1*2","-R","-r",str(r_chr1),"-o",outdir+'8hap_rhofixed'+'%02d_%s' %(hap_counter,outputprefix),input_directory+filename])
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
              call (["./msmc_1.1.0_linux64bit","-I","%s,%s,%s,%s,%s,%s,%s,%s" %(index_counter,index_counter_1,index_counter_2,index_counter_3,index_counter_4,index_counter_5,index_counter_6,index_counter_7),"-p1*2+15*1+1*2","-R","-r",str(r_chr2),"-o",outdir+'8hap_rhofixed'+'%02d_%s' %(hap_counter,outputprefix),input_directory+filename])
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
              call (["./msmc_1.1.0_linux64bit","-I","%s,%s,%s,%s,%s,%s,%s,%s" %(index_counter,index_counter_1,index_counter_2,index_counter_3,index_counter_4,index_counter_5,index_counter_6,index_counter_7),"-p1*2+15*1+1*2","-R","-r",str(r_chr3),"-o",outdir+'8hap_rhofixed'+'%02d_%s' %(hap_counter,outputprefix),input_directory+filename])
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
              call (["./msmc_1.1.0_linux64bit","-I","%s,%s,%s,%s,%s,%s,%s,%s" %(index_counter,index_counter_1,index_counter_2,index_counter_3,index_counter_4,index_counter_5,index_counter_6,index_counter_7),"-p1*2+15*1+1*2","-R","-r",str(r_chr4),"-o",outdir+'8hap_rhofixedf'+'%02d_%s' %(hap_counter,outputprefix),input_directory+filename])
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
              call (["./msmc_1.1.0_linux64bit","-I","%s,%s,%s,%s,%s,%s,%s,%s" %(index_counter,index_counter_1,index_counter_2,index_counter_3,index_counter_4,index_counter_5,index_counter_6,index_counter_7),"-p1*2+15*1+1*2","-R","-r",str(r_chr5),"-o",outdir+'8hap_rhofixed'+'%02d_%s' %(hap_counter,outputprefix),input_directory+filename])
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