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

sample_list = glob.glob("/data/home/users/m.ruscheweyh/plink/input/*.vcf.gz")
item_counter = 0

for file in os.listdir(input_directory):        
         if fnmatch.fnmatch(file, "Spain*.vcf.gz"):
            while item_counter < len(sample_list):
              outputprefix = str(sample_list[item_counter])[42:52]   
              call (["./plink","--threads","8","--make-bed","--allow-extra-chr","--chr","1-5","--vcf","%s" %(sample_list[item_counter]), "--out","%s/%s" %(outdir,outputprefix)])
              item_counter +=1
              continue
         else:
            continue
        
         if fnmatch.fnmatch(file, "Sweden*.vcf.gz"):
                while item_counter < len(sample_list):
                    outputprefix = str(sample_list[item_counter])[42:55]
                    call (["./plink","--threads","8","--make-bed","--allow-extra-chr","--chr","1-5","--vcf","%s" %(sample_list[item_counter]), "--out","%s/%s" %(outdir,outputprefix)])
                    item_counter +=1
                    continue
         else: 
            continue
        
         if fnmatch.fnmatch(file, "Tübingen*.vcf.gz"):
                while item_counter < len(sample_list):
                    outputprefix = str(sample_list[item_counter])[42:62]
                    call (["./plink","--threads","8","--make-bed","--allow-extra-chr","--chr","1-5","--vcf","%s" %(sample_list[item_counter]), "--out","%s/%s" %(outdir,outputprefix)])
                    item_counter +=1
                    continue
                
         if fnmatch.fnmatch(file, "madeira*.vcf.gz"):
            while item_counter < len(sample_list):
              outputprefix = str(sample_list[item_counter])[42:59]   
              call (["./plink","--threads","8","--make-bed","--allow-extra-chr","--chr","1-5","--vcf","%s" %(sample_list[item_counter]), "--out","%s/%s" %(outdir,outputprefix)])
              item_counter +=1
              continue
         else:
            continue
