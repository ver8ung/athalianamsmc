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

crosscoal_Mad_Spain_1ind_1 = pd.read_csv("mad_spain_combined_1ind_1.msmc2.final.txt", delim_whitespace=True)
crosscoal_Mad_Spain_1ind_2 = pd.read_csv("mad_spain_combined_1ind_2.msmc2.final.txt", delim_whitespace=True)
crosscoal_Mad_Spain_2ind_1 = pd.read_csv("mad_spain_combined_2ind_1.msmc2.final.txt", delim_whitespace=True)
crosscoal_Mad_Spain_2ind_2 = pd.read_csv("mad_spain_combined_2ind_2.msmc2.final.txt", delim_whitespace=True)

crosscoal_Spain_Tub_1ind_1 = pd.read_csv("spain_tübingen_combined_1ind_1.msmc2.final.txt", delim_whitespace=True)
crosscoal_Spain_Tub_1ind_2 = pd.read_csv("spain_tübingen_combined_1ind_2.msmc2.final.txt", delim_whitespace=True)
crosscoal_Spain_Tub_2ind_1 = pd.read_csv("spain_tübingen_combined_2ind_1.msmc2.final.txt", delim_whitespace=True)
crosscoal_Spain_Tub_2ind_2 = pd.read_csv("spain_tübingen_combined_2ind_2.msmc2.final.txt", delim_whitespace=True)

crosscoal_Tub_Swe_1ind_1 = pd.read_csv("tübingen_swe_combined_1ind_1.msmc2.final.txt", delim_whitespace=True)
crosscoal_Tub_Swe_1ind_2 = pd.read_csv("tübingen_swe_combined_1ind_2.msmc2.final.txt", delim_whitespace=True)
crosscoal_Tub_Swe_2ind_1 = pd.read_csv("tübingen_swe_combined_2ind_1.msmc2.final.txt", delim_whitespace=True)
crosscoal_Tub_Swe_2ind_2 = pd.read_csv("tübingen_swe_combined_2ind_2.msmc2.final.txt", delim_whitespace=True)


figure(num=None, figsize=(10, 8), dpi=100, facecolor='w', edgecolor='k')
plt.step(crosscoal_Mad_Spain_1ind_1["left_time_boundary"]/mu*gen, 2 * crosscoal_Mad_Spain_1ind_1["lambda_01"] / (crosscoal_Mad_Spain_1ind_1["lambda_00"] + crosscoal_Mad_Spain_1ind_1["lambda_11"]), label="Mad_Spain_2ind_1")
plt.step(crosscoal_Mad_Spain_1ind_2["left_time_boundary"]/mu*gen, 2 * crosscoal_Mad_Spain_1ind_2["lambda_01"] / (crosscoal_Mad_Spain_1ind_2["lambda_00"] + crosscoal_Mad_Spain_1ind_2["lambda_11"]), label="Mad_Spain_2ind_2")
plt.step(crosscoal_Mad_Spain_2ind_1["left_time_boundary"]/mu*gen, 2 * crosscoal_Mad_Spain_1ind_1["lambda_01"] / (crosscoal_Mad_Spain_2ind_1["lambda_00"] + crosscoal_Mad_Spain_2ind_1["lambda_11"]), label="Mad_Spain_4ind_1")
plt.step(crosscoal_Mad_Spain_2ind_2["left_time_boundary"]/mu*gen, 2 * crosscoal_Mad_Spain_2ind_1["lambda_01"] / (crosscoal_Mad_Spain_2ind_2["lambda_00"] + crosscoal_Mad_Spain_2ind_2["lambda_11"]), label="Mad_Spain_4ind_2")

plt.step(crosscoal_Spain_Tub_1ind_1["left_time_boundary"]/mu*gen, 2 * crosscoal_Spain_Tub_1ind_1["lambda_01"] / (crosscoal_Spain_Tub_1ind_1["lambda_00"] + crosscoal_Spain_Tub_1ind_1["lambda_11"]), label="Spain_Tub_2ind_1")
plt.step(crosscoal_Spain_Tub_1ind_2["left_time_boundary"]/mu*gen, 2 * crosscoal_Spain_Tub_2ind_1["lambda_01"] / (crosscoal_Spain_Tub_1ind_2["lambda_00"] + crosscoal_Spain_Tub_1ind_2["lambda_11"]), label="Spain_Tub_2ind_2")
plt.step(crosscoal_Spain_Tub_2ind_1["left_time_boundary"]/mu*gen, 2 * crosscoal_Spain_Tub_1ind_1["lambda_01"] / (crosscoal_Spain_Tub_2ind_1["lambda_00"] + crosscoal_Spain_Tub_2ind_1["lambda_11"]), label="Spain_Tub_4ind_1")
plt.step(crosscoal_Spain_Tub_2ind_2["left_time_boundary"]/mu*gen, 2 * crosscoal_Spain_Tub_2ind_1["lambda_01"] / (crosscoal_Spain_Tub_2ind_2["lambda_00"] + crosscoal_Spain_Tub_2ind_2["lambda_11"]), label="Spain_Tub_4ind_2")

plt.step(crosscoal_Tub_Swe_1ind_1["left_time_boundary"]/mu*gen, 2 * crosscoal_Tub_Swe_1ind_1["lambda_01"] / (crosscoal_Tub_Swe_1ind_1["lambda_00"] + crosscoal_Tub_Swe_1ind_1["lambda_11"]), label="Tub_Swe_2ind_1")
plt.step(crosscoal_Tub_Swe_1ind_2["left_time_boundary"]/mu*gen, 2 * crosscoal_Tub_Swe_2ind_1["lambda_01"] / (crosscoal_Tub_Swe_1ind_2["lambda_00"] + crosscoal_Tub_Swe_1ind_2["lambda_11"]), label="Tub_Swe_2ind_2")
plt.step(crosscoal_Tub_Swe_2ind_1["left_time_boundary"]/mu*gen, 2 * crosscoal_Tub_Swe_1ind_1["lambda_01"] / (crosscoal_Tub_Swe_2ind_1["lambda_00"] + crosscoal_Tub_Swe_2ind_1["lambda_11"]), label="Tub_Swe_4ind_1")
plt.step(crosscoal_Tub_Swe_2ind_2["left_time_boundary"]/mu*gen, 2 * crosscoal_Tub_Swe_2ind_1["lambda_01"] / (crosscoal_Tub_Swe_2ind_2["lambda_00"] + crosscoal_Tub_Swe_2ind_2["lambda_11"]), label="Tub_Swe_4ind_2")

plt.xlim(1000,500000)
plt.ylim(0,1.2)
plt.xlabel("years ago");
plt.ylabel("relative cross coalescence rate");
plt.gca().set_xscale('log')
plt.legend(loc=0)

os.chdir("/data/home/users/m.ruscheweyh/MSMCresults/pyplots/CCR")
plt.savefig("CCR_Mad_Spain_complete.png")
