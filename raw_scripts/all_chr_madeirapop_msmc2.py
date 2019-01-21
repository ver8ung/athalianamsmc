#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 14:55:15 2019

@author: m.ruscheweyh
"""
import os, glob, fnmatch
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
input_rho_1 = "/data/home/users/m.ruscheweyh/pythontest/input/chr1/"
input_rho_2 = "/data/home/users/m.ruscheweyh/pythontest/input/chr2/"
input_rho_3 = "/data/home/users/m.ruscheweyh/pythontest/input/chr3/"
input_rho_4 = "/data/home/users/m.ruscheweyh/pythontest/input/chr4/"
input_rho_5 = "/data/home/users/m.ruscheweyh/pythontest/input/chr5/"
all_chr_input_madeira = glob.glob("/data/home/users/m.ruscheweyh/pythontest/input/madeira*.multihetsep.txt")
all_chr_input_spain = glob.glob("/data/home/users/m.ruscheweyh/pythontest/input/spain*.multihetsep.txt")
outdir = "output/msmc2/" # specifies output directory
outdir_allchr = "output/msmc2/allchr/"
sample_list = sorted(glob.glob("/data/home/users/m.ruscheweyh/pythontest/input/*.multihetsep.txt"))
sample_string = str(sample_list)
while run_counter < 2 :
     while index_counter < 27:
              outputprefix = "MadeiraFD"   # use only desired positions of input filenames as output prefix
              call (["./msmc2_linux64bit","-I","%s,%s,%s,%s" %(index_counter,index_counter_1,index_counter_2,index_counter_3),"-r",str(r_average),"-o",outdir_allchr+'4hap_rho_allchr'+'%02d_%s' %(hap_counter,outputprefix),"%s" %(all_chr_input_madeira[0]),"%s" %(all_chr_input_madeira[1]),"%s" %(all_chr_input_madeira[2]),"%s" %(all_chr_input_madeira[3]),"%s" %(all_chr_input_madeira[4])])
              result_name = '4hap_rho_allchr'+'%02d_%s' %(hap_counter,outputprefix) + '.final.txt'
              os.chdir(outdir_allchr)
              plot_input = pd.read_csv("%s" %(result_name), delim_whitespace=True)
              figure(num=None, figsize=(10, 8), dpi=100, facecolor='w', edgecolor='k')
              plt.step(plot_input["left_time_boundary"]/mu*gen, (1/plot_input["lambda"])/(2*mu), label="%s" %(result_name), color="black")
              plt.ylim(50000,800000)
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
              index_counter_2 = 2
              index_counter_3 = 3
              run_counter += 1

while run_counter < 3 :
    while index_counter < 27:
             outputprefix = "MadeiraFD"   # use only desired positions of input filenames as output prefix
             call (["./msmc2_linux64bit","-I","%s,%s,%s,%s,%s,%s" %(index_counter,index_counter_1,index_counter_2,index_counter_3,index_counter_4,index_counter_5),"-r",str(r_average),"-o",outdir+'6hap_rho'+'%02d_%s' %(hap_counter,outputprefix),"%s" %(all_chr_input_madeira[0]),"%s" %(all_chr_input_madeira[1]),"%s" %(all_chr_input_madeira[2]),"%s" %(all_chr_input_madeira[3]),"%s" %(all_chr_input_madeira[4])])
             result_name = '6hap_rho_allchr'+'%02d_%s' %(hap_counter,outputprefix) + '.final.txt'
             os.chdir(outdir_allchr)
             plot_input = pd.read_csv("%s" %(result_name), delim_whitespace=True)
             figure(num=None, figsize=(10, 8), dpi=100, facecolor='w', edgecolor='k')
             plt.step(plot_input["left_time_boundary"]/mu*gen, (1/plot_input["lambda"])/(2*mu), label="%s" %(result_name), color="black")
             plt.ylim(50000,800000)
             plt.xlabel("years ago");
             plt.ylabel("effective population size");
             plt.gca().set_xscale('log')
             plt.legend(loc=0)
             os.chdir("/data/home/users/m.ruscheweyh/MSMCresults/pyplots/scripttest")
             plt.savefig(result_name + ".png")
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

while run_counter < 3:
    while index_counter < 27:
              outputprefix = "MadeiraFD"   # use only desired positions of input filenames as output prefix´
              call (["./msmc2_linux64bit","-I","%s,%s,%s,%s,%s,%s,%s,%s" %(index_counter,index_counter_1,index_counter_2,index_counter_3,index_counter_4,index_counter_5,index_counter_6,index_counter_7),"-r",str(r_average),"-o",outdir+'8hap_rho'+'%02d_%s' %(hap_counter,outputprefix),"%s" %(all_chr_input_madeira[0]),"%s" %(all_chr_input_madeira[1]),"%s" %(all_chr_input_madeira[2]),"%s" %(all_chr_input_madeira[3]),"%s" %(all_chr_input_madeira[4])])
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