#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 15:28:09 2019

@author: m.ruscheweyh
"""

import os
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.pyplot import figure

#Parameters for Arabidopsis thaliana
mu = 7e-9
gen = 1
####################################

os.chdir("/data/home/users/m.ruscheweyh/msmc/crosscoal/results/combined")
###################################
#plotting##########################

crosscoal_Spain_Mad = pd.read_csv("spain_mad_combined.txt", delim_whitespace=True)
crosscoal_Spain_Tub = pd.read_csv("spain_tub_combined.txt", delim_whitespace=True)
crosscoal_Tub_Swe = pd.read_csv("spain_tub_combined.txt", delim_whitespace=True)

figure(num=None, figsize=(10, 8), dpi=100, facecolor='w', edgecolor='k')
plt.step(crosscoal_Spain_Mad["left_time_boundary"]/mu*gen, 2 * crosscoal_Spain_Mad["lambda_01"] / (crosscoal_Spain_Mad["lambda_00"] + crosscoal_Spain_Mad["lambda_11"]))
plt.step(crosscoal_Spain_Tub["left_time_boundary"]/mu*gen, 2 * crosscoal_Spain_Mad["lambda_01"] / (crosscoal_Spain_Tub["lambda_00"] + crosscoal_Spain_Mad["lambda_11"]))
plt.step(crosscoal_Tub_Swe["left_time_boundary"]/mu*gen, 2 * crosscoal_Tub_Swe["lambda_01"] / (crosscoal_Tub_Swe["lambda_00"] + crosscoal_Spain_Mad["lambda_11"]))
plt.xlim(1000,500000)
plt.xlabel("years ago");
plt.ylabel("relative cross coalescence rate");
plt.gca().set_xscale('log')
plt.legend()
plt.savefig("foo.png")