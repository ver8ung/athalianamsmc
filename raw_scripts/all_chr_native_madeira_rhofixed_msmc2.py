#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 13:03:11 2019

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
r_chr1 = 4.587
r_chr2 = 5.1429
r_chr3 = 5
r_chr4 = 5.4286
r_chr5 = 5.1429
r_average =  5.1143

#variables for the script
input_directory = "/data/home/users/m.ruscheweyh/pythontest/input/" # specify input directory
all_chr_input_madeira = sorted(glob.glob("/data/home/users/m.ruscheweyh/pythontest/input/madeiraFD_2_*.multihetsep.txt"))
outdir = "output/msmc2/" # specifies output directory
outdir_allchr = "output/msmc2/allchr/"
sample_list = sorted(glob.glob("/data/home/users/m.ruscheweyh/pythontest/input/*.multihetsep.txt"))
sample_string = str(sample_list)
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
         while index_counter <= 20:
              outputprefix = "MadeiraFD_native"   # use only desired positions of input filenames as output prefix
              call (["./msmc2_linux64bit","-I","%s,%s" %(index_counter,index_counter_1),"-r",str(r_average),"--fixedRecombination","-o",outdir_allchr+'2hap_rhofixed_allchr'+'%02d_%s' %(hap_counter,outputprefix),"%s" %(all_chr_input_madeira[0]),"%s" %(all_chr_input_madeira[1]),"%s" %(all_chr_input_madeira[2]),"%s" %(all_chr_input_madeira[3]),"%s" %(all_chr_input_madeira[4])])
              result_name = '2hap_rhofixed_allchr'+'%02d_%s' %(hap_counter,outputprefix) + '.final.txt'
              os.chdir(outdir_allchr)
              plot_input = pd.read_csv("%s" %(result_name), delim_whitespace=True)
              figure(num=None, figsize=(10, 8), dpi=100, facecolor='w', edgecolor='k')
              plt.step(plot_input["left_time_boundary"]/mu*gen, (1/plot_input["lambda"])/(2*mu), label="%s" %(result_name), color="black")
              plt.ylim(10000,400000)
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

while run_counter < 2 :
     while index_counter <= 16:
              outputprefix = "MadeiraFD_native"   # use only desired positions of input filenames as output prefix
              call (["./msmc2_linux64bit","-I","%s,%s,%s,%s" %(index_counter,index_counter_1,index_counter_2,index_counter_3),"-r",str(r_average),"--fixedRecombination","-o",outdir_allchr+'4hap_rhofixed_allchr'+'%02d_%s' %(hap_counter,outputprefix),"%s" %(all_chr_input_madeira[0]),"%s" %(all_chr_input_madeira[1]),"%s" %(all_chr_input_madeira[2]),"%s" %(all_chr_input_madeira[3]),"%s" %(all_chr_input_madeira[4])])
              result_name = '4hap_rhofixed_allchr'+'%02d_%s' %(hap_counter,outputprefix) + '.final.txt'
              os.chdir(outdir_allchr)
              plot_input = pd.read_csv("%s" %(result_name), delim_whitespace=True)
              figure(num=None, figsize=(10, 8), dpi=100, facecolor='w', edgecolor='k')
              plt.step(plot_input["left_time_boundary"]/mu*gen, (1/plot_input["lambda"])/(2*mu), label="%s" %(result_name), color="black")
              plt.ylim(10000,400000)
              plt.xlabel("years ago");
              plt.ylabel("effective population size");
              plt.gca().set_xscale('log')
              plt.legend(loc=0)
              os.chdir("/data/home/users/m.ruscheweyh/MSMCresults/pyplots/scripttest")
              plt.savefig(result_name + ".png")
              os.chdir("/data/home/users/m.ruscheweyh/pythontest")
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
              run_counter += 1

while run_counter < 3 :
    while index_counter <= 12:
             outputprefix = "MadeiraFD_native"   # use only desired positions of input filenames as output prefix
             call (["./msmc2_linux64bit","-I","%s,%s,%s,%s,%s,%s" %(index_counter,index_counter_1,index_counter_2,index_counter_3,index_counter_4,index_counter_5),"-r",str(r_average),"--fixedRecombination","-o",outdir_allchr+'6hap_rhofixed_allchr'+'%02d_%s' %(hap_counter,outputprefix),"%s" %(all_chr_input_madeira[0]),"%s" %(all_chr_input_madeira[1]),"%s" %(all_chr_input_madeira[2]),"%s" %(all_chr_input_madeira[3]),"%s" %(all_chr_input_madeira[4])])
             result_name = '6hap_rhofixed_allchr'+'%02d_%s' %(hap_counter,outputprefix) + '.final.txt'
             os.chdir(outdir_allchr)
             plot_input = pd.read_csv("%s" %(result_name), delim_whitespace=True)
             figure(num=None, figsize=(10, 8), dpi=100, facecolor='w', edgecolor='k')
             plt.step(plot_input["left_time_boundary"]/mu*gen, (1/plot_input["lambda"])/(2*mu), label="%s" %(result_name), color="black")
             plt.ylim(10000,400000)
             plt.xlabel("years ago");
             plt.ylabel("effective population size");
             plt.gca().set_xscale('log')
             plt.legend(loc=0)
             os.chdir("/data/home/users/m.ruscheweyh/MSMCresults/pyplots/scripttest")
             plt.savefig(result_name + ".png")
             os.chdir("/data/home/users/m.ruscheweyh/pythontest")
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
              run_counter += 1

while run_counter < 4:
    while index_counter <= 8:
             outputprefix = "MadeiraFD_native"   # use only desired positions of input filenames as output prefix´
             call (["./msmc2_linux64bit","-I","%s,%s,%s,%s,%s,%s,%s,%s" %(index_counter,index_counter_1,index_counter_2,index_counter_3,index_counter_4,index_counter_5,index_counter_6,index_counter_7),"-r",str(r_average),"--fixedRecombination","-o",outdir_allchr+'8hap_rhofixed_allchr'+'%02d_%s' %(hap_counter,outputprefix),"%s" %(all_chr_input_madeira[0]),"%s" %(all_chr_input_madeira[1]),"%s" %(all_chr_input_madeira[2]),"%s" %(all_chr_input_madeira[3]),"%s" %(all_chr_input_madeira[4])])
             result_name = '8hap_rhofixed_allchr'+'%02d_%s' %(hap_counter,outputprefix) + '.final.txt'
             os.chdir(outdir_allchr)
             plot_input = pd.read_csv("%s" %(result_name), delim_whitespace=True)
             figure(num=None, figsize=(10, 8), dpi=100, facecolor='w', edgecolor='k')
             plt.step(plot_input["left_time_boundary"]/mu*gen, (1/plot_input["lambda"])/(2*mu), label="%s" %(result_name), color="black")
             plt.ylim(10000,400000)
             plt.xlabel("years ago");
             plt.ylabel("effective population size");
             plt.gca().set_xscale('log')
             plt.legend(loc=0)
             os.chdir("/data/home/users/m.ruscheweyh/MSMCresults/pyplots/scripttest")
             plt.savefig(result_name + ".png")
             os.chdir("/data/home/users/m.ruscheweyh/pythontest")
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
              run_counter += 1