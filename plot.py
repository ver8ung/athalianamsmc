#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 15:10:33 2019

@author: m.ruscheweyh
"""
import os
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.pyplot import figure

#Parameters specific for Arabidopsis thaliana, needed to scale results accordingly
mu = 7e-9 #mutation rate
gen = 1 # generation time
####################################

os.chdir("/data/home/users/m.ruscheweyh/msmc/pop_results_wholechr_allchr")
###################################
#plotting##########################

Mad2hap = pd.read_csv("Madeira2hapfd_pop1fixeddef_all.msmc2.final.txt", delim_whitespace=True)
Spain2hap = pd.read_csv("Spain/spain2hapfd_pop1fixeddef_all.msmc2.final.txt", delim_whitespace=True)

figure(num=None, figsize=(10, 8), dpi=100, facecolor='w', edgecolor='k')
plt.step(Mad2hap["left_time_boundary"]/mu*gen, (1/Mad2hap["lambda"])/(2*mu), label="Madeira_2haplotypes_fixeddef")
plt.step(Spain2hap["left_time_boundary"]/mu*gen, (1/Spain2hap["lambda"])/(2*mu), label="Spain_2haplotypes_fixeddef")
plt.ylim(50000,800000)
plt.xlabel("years ago");
plt.ylabel("effective population size");
plt.gca().set_xscale('log')
plt.legend(loc=0)

os.chdir("/data/home/users/m.ruscheweyh/MSMCresults/pyplots")
plt.savefig("2haplotypes.png")
