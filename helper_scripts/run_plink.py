#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 15:08:47 2019

@author: m.ruscheweyh
"""

import os, glob, fnmatch
from subprocess import call

input_directory = "/data/home/users/m.ruscheweyh/plink/input"
outdir = "/data/home/users/m.ruscheweyh/plink/output"

madeira_samps = glob.glob("/data/home/users/m.ruscheweyh/plink/input/*madeira*.vcf.gz")
madeiran_loop = 0

for file in os.listdir(input_directory):
    if fnmatch.fnmatch(file, "*madeira*.vcf.gz"):
        while madeiran_loop < len(madeira_samps):
              outputprefix = str(madeira_samps[madeiran_loop])[42:55]   
              call (["./plink","--threads","8","--make-bed","--allow-extra-chr","--chr","1-5","--vcf","%s" %(madeira_samps[madeiran_loop]), "--out","%s/%s" %(outdir,outputprefix)])
              madeiran_loop +=1
              continue
