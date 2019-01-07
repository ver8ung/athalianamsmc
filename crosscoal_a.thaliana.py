#!/usr/bin/env python
# -*- coding: utf-8 -*-
#$ -N python_MSMC2_fixedRecombination_singlechr
#$ -M max.ruscheweyh@tum.de
#$-cwd
"""
Created on Mon Jan  7 10:07:21 2019
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
