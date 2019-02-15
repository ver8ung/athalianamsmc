#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 13:16:36 2019

@author: m.ruscheweyh
"""

import os, glob
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.pyplot import figure

###################################
#plotting
mu = 7e-9
gen = 1

simulation_results = sorted(glob.glob("/data/home/users/m.ruscheweyh/pythontest/output/msmc2/allchr/*msmc2ms*.final.txt"))
list_index = 0
short_results = [i[61: -4].split(',') for i in simulation_results]
short_index = 0

while list_index < len(str(simulation_results)):
              plot_input = pd.read_csv("%s" %(str(simulation_results[list_index])), delim_whitespace=True)
              figure(num=None, figsize=(10, 8), dpi=100, facecolor='w', edgecolor='k')
              plt.step(plot_input["left_time_boundary"]/mu*gen, (1/plot_input["lambda"])/(2*mu), label="%s" %(short_results[short_index]), color="black")
              plt.ylim(5000,200000)
              plt.xlabel("years ago");
              plt.ylabel("effective population size");
              plt.gca().set_xscale('log')
              plt.legend(loc=0)
              os.chdir("/data/home/users/m.ruscheweyh/MSMCresults/pyplots/sim_replots")
              plt.savefig(str(short_results[short_index])+ ".png", bbox_inches='tight')
              list_index += 1
              short_index += 1
              continue