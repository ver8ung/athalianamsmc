#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 15:10:33 2019

@author: m.ruscheweyh
"""
import os, glob
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import pandas as pd
from matplotlib.pyplot import figure
from subprocess import call

#parameters for Arabidopsis thaliana 
###################################
#plotting
mu = 7e-9
gen = 1
###################################
#rhoOverMu
r_average =  5.1143

#variables for the script
input_directory = "/data/home/users/m.ruscheweyh/pythontest/input/" # specify input directory
all_chr_input_madeira = glob.glob("/data/home/users/m.ruscheweyh/pythontest/input/madeira*.multihetsep.txt")
outdir_allchr = "output/msmc2/allchr/" # specifies output directory

hap_counter = 1     # counter for iteration over haplotype combinations, determines file output prefix, default prefix "01_"
index_counter = 0   # counters for the -I parameter of MSMC, iterates over x-amount of haplotypes in pairs of x-indexes
run_counter = 0
index_counter_1 = 1 #######################################################################################################
index_counter_2 = 2 #######################################################################################################
index_counter_3 = 3 #######################################################################################################
index_counter_4 = 4 #######################################################################################################
index_counter_5 = 5 #######################################################################################################
index_counter_6 = 6 #######################################################################################################
index_counter_7 = 7 #######################################################################################################

while run_counter < 1:
         while index_counter < 27:
              outputprefix = "MadeiraFD"   # use only desired positions of input filenames as output prefix
              call (["./msmc2_linux64bit","-I","%s,%s" %(index_counter,index_counter_1),"-r",str(r_average),"-o",outdir_allchr+'2hap_rho_allchr'+'%02d_%s' %(hap_counter,outputprefix),"%s" %(all_chr_input_madeira[0]),"%s" %(all_chr_input_madeira[1]),"%s" %(all_chr_input_madeira[2]),"%s" %(all_chr_input_madeira[3]),"%s" %(all_chr_input_madeira[4])])
              result_name = '2hap_rho_allchr'+'%02d_%s' %(hap_counter,outputprefix) + '.final.txt'
              os.chdir(outdir_allchr)
              plot_input = pd.read_csv("%s" %(result_name), delim_whitespace=True)
              figure(num=None, figsize=(10, 8), dpi=100, facecolor='w', edgecolor='k')
              plt.step(plot_input["left_time_boundary"]/mu*gen, (1/plot_input["lambda"])/(2*mu), label="%s" %(result_name), color="black")
              plt.ylim(50000,400000)
              plt.xlabel("years ago");
              plt.ylabel("effective population size");
              plt.gca().set_xscale('log')
              plt.legend(loc=0)
              os.chdir("/data/home/users/m.ruscheweyh/MSMCresults/pyplots/scripttest")
              plt.savefig(result_name + ".png")
              os.chdir("/data/home/users/m.ruscheweyh/pythontest")
              hap_counter += 1
              index_counter += 2
              index_counter_1 += 2
              continue
         else:
              hap_counter = 1
              index_counter = 0
              index_counter_1 = 1
              run_counter +=1
