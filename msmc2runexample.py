#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 15:10:33 2019

@author: m.ruscheweyh
"""
import os, glob, fnmatch
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.pyplot import figure
from subprocess import call

#parameters for Arabidopsis thaliana 
mu = 7e-9
gen = 1
r_chr1 = 4.587
r_chr2 = 5.1429
r_chr3 = 5
r_chr4 = 5.4286
r_chr5 = 5.1429
r_average =  5.1143

#variables for the script
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
outdir = "output/msmc2/"; # specifies output directory
outdir_rho = "output/msmc2/rho_runs/"
outdir_allchr = "output/msmc2/allchr/"
results = glob.glob("/data/home/users/m.ruscheweyh/pythontest/output/msmc2/allchr")
hap_counter = 1     # counter for iteration over haplotype combinations, determines file output prefix, default prefix "01_"
index_counter = 0   # counters for the -I parameter of MSMC, iterates over x-amount of haplotypes in pairs of x-indexes
index_counter_1 = 1 #######################################################################################################
index_counter_2 = 2 #######################################################################################################
index_counter_3 = 3 #######################################################################################################
index_counter_4 = 4 #######################################################################################################
index_counter_5 = 5 #######################################################################################################
index_counter_6 = 6 #######################################################################################################
index_counter_7 = 7 #######################################################################################################

for file in os.listdir(input_directory): # retrieve filenames in input_directory for output prefix
    if fnmatch.fnmatch(file, "madeiraFDchr1.multi*.txt"): # call MSMC with desired parameters on specified input files
      while hap_counter < 27:
              outputprefix = file[:13]   # use only desired positions of input filenames as output prefix
              call (["./msmc2_linux64bit","-I","%s,%s" %(index_counter,index_counter_1),"--fixedRecombination","-r",str(r_average),"-o",outdir_allchr+'2hap_rhofixed_allchr'+'%02d_%s' %(hap_counter,outputprefix),"%s" %(all_chr_input_madeira[0]),"%s" %(all_chr_input_madeira[1]),"%s" %(all_chr_input_madeira[2]),"%s" %(all_chr_input_madeira[3]),"%s" %(all_chr_input_madeira[4])])
              result_name = '2hap_rhofixed_allchr'+'%02d_%s' %(hap_counter,outputprefix) + '.final.txt'
              os.chdir(outdir_allchr)
              plot_input = pd.read_csv("%s" %(result_name), delim_whitespace=True)
              figure(num=None, figsize=(10, 8), dpi=100, facecolor='w', edgecolor='k')
              plt.step(plot_input["left_time_boundary"]/mu*gen, (1/plot_input["lambda"])/(2*mu), label="%s" %(outputprefix), color="black")
              plt.ylim(50000,800000)
              plt.xlabel("years ago");
              plt.ylabel("effective population size");
              plt.gca().set_xscale('log')
              plt.legend(loc=0)
              os.chdir("/data/home/users/m.ruscheweyh/MSMCresults/pyplots/scripttest")
              plt.savefig("test1.png")
              os.chdir(input_directory)
              hap_counter += 1
              index_counter += 2
              index_counter_1 += 2
              continue
      else:
              hap_counter = 1
              index_counter = 0
              index_counter_1 = 1
              continue