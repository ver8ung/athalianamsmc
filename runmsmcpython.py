#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 11:26:54 2018

@author: m.ruscheweyh
"""
import os
path = "//home/data/users/m.ruscheweyh/msmc"
os.getcwd()
from subprocess import call
os.chdir("msmc")
indir = "home/data/users/m.ruscheweyh/msmc"
outdir = "home/data/users/m.ruscheweyh/msmc/script_output"
fixed = "-R"
call (["msmc_1.0.0._linux64bit", "-o outdir", "indir","fixed"])
   
    