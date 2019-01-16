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

for file in os.listdir(input_directory):
    if fnmatch.fnmatch(file, "*madeira*.vcf.gz"):
              outputprefix = str(madeira_samps[0])[42:55]   
              call (["./plink","--threads 8", "--make-bed","--allow-extra-chr","--chr 1-5","--vcf","%s" %(madeira_samps[0]), "--out","%s" %(outputprefix)])
              outputprefix = str(madeira_samps[1])[42:55]
              call (["./plink","--threads 8", "--make-bed","--allow-extra-chr","--chr 1-5","--vcf","%s" %(madeira_samps[1]), "--out","%s" %(outputprefix)])
              outputprefix = str(madeira_samps[2])[42:55]
              call (["./plink","--threads 8", "--make-bed","--allow-extra-chr","--chr 1-5","--vcf","%s" %(madeira_samps[2]), "--out","%s" %(outputprefix)])
              outputprefix = str(madeira_samps[3])[42:55]
              call (["./plink","--threads 8", "--make-bed","--allow-extra-chr","--chr 1-5","--vcf","%s" %(madeira_samps[3]), "--out","%s" %(outputprefix)])
              outputprefix = str(madeira_samps[4])[42:55]
              call (["./plink","--threads 8", "--make-bed","--allow-extra-chr","--chr 1-5","--vcf","%s" %(madeira_samps[4]), "--out","%s" %(outputprefix)])
              outputprefix = str(madeira_samps[5])[42:55]
              call (["./plink","--threads 8", "--make-bed","--allow-extra-chr","--chr 1-5","--vcf","%s" %(madeira_samps[5]), "--out","%s" %(outputprefix)])
              outputprefix = str(madeira_samps[6])[42:55]
              call (["./plink","--threads 8", "--make-bed","--allow-extra-chr","--chr 1-5","--vcf","%s" %(madeira_samps[6]), "--out","%s" %(outputprefix)])
              outputprefix = str(madeira_samps[7])[42:55]
              call (["./plink","--threads 8", "--make-bed","--allow-extra-chr","--chr 1-5","--vcf","%s" %(madeira_samps[7]), "--out","%s" %(outputprefix)])
              outputprefix = str(madeira_samps[8])[42:55]
              call (["./plink","--threads 8", "--make-bed","--allow-extra-chr","--chr 1-5","--vcf","%s" %(madeira_samps[8]), "--out","%s" %(outputprefix)])
              outputprefix = str(madeira_samps[9])[42:55]
              call (["./plink","--threads 8", "--make-bed","--allow-extra-chr","--chr 1-5","--vcf","%s" %(madeira_samps[9]), "--out","%s" %(outputprefix)])
              outputprefix = str(madeira_samps[10])[42:55]
              call (["./plink","--threads 8", "--make-bed","--allow-extra-chr","--chr 1-5","--vcf","%s" %(madeira_samps[10]), "--out","%s" %(outputprefix)])
              outputprefix = str(madeira_samps[11])[42:55]
              call (["./plink","--threads 8", "--make-bed","--allow-extra-chr","--chr 1-5","--vcf","%s" %(madeira_samps[11]), "--out","%s" %(outputprefix)])
              outputprefix = str(madeira_samps[12])[42:55]
              call (["./plink","--threads 8", "--make-bed","--allow-extra-chr","--chr 1-5","--vcf","%s" %(madeira_samps[12]), "--out","%s" %(outputprefix)])
              outputprefix = str(madeira_samps[13])[42:55]
              call (["./plink","--threads 8", "--make-bed","--allow-extra-chr","--chr 1-5","--vcf","%s" %(madeira_samps[13]), "--out","%s" %(outputprefix)])