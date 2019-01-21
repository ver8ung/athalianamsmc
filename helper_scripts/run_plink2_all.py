#!/usr/bin/env python2
# -*- encoding: iso-8859-15 -*-
"""
Created on Wed Jan 16 15:08:47 2019
@author: m.ruscheweyh
"""

import os, glob
from subprocess import call

input_directory = "/data/home/users/m.ruscheweyh/plink2/input"
outdir = "/data/home/users/m.ruscheweyh/plink2/output"
sample_list = sorted(glob.glob("/data/home/users/m.ruscheweyh/plink2/input/*.vcf.gz"))
sample_string = str(sample_list)
range_spain = sample_string.count('Spain') 
range_sweden = sample_string.count('Sweden')
range_tubingen = sample_string.count('Tubingen')
range_madeira = sample_string.count('madeira')

range_1 = range_spain
range_2 = range_spain + range_sweden
range_3 = range_spain + range_sweden + range_tubingen


Madeira = 'madeira'
Spain = 'Spain'
Sweden = 'Sweden'
Tubingen = 'Tübingen'
item_counter = 0
sample_list.count('Spain')

while item_counter < len(sample_list):
    for Spain in os.listdir(input_directory): 
        while item_counter < range_1:
            spain_name = str(sample_list[item_counter][43:53])
            call (["./plink2","--threads","8","--make-bed","--allow-extra-chr","--chr","1-5","--vcf","%s" %(sample_list[item_counter]),"--max-alleles","2","--memory","12000","--out","%s/%s" %(outdir,spain_name)])
            item_counter += 1
            continue
        
    for Sweden in os.listdir(input_directory):
        while item_counter < range_2:
            sweden_name = str(sample_list[item_counter][43:54])
            call (["./plink2","--threads","8","--make-bed","--allow-extra-chr","--chr","1-5","--vcf","%s" %(sample_list[item_counter]),"--max-alleles","2","--memory","12000","--out","%s/%s" %(outdir,sweden_name)])
            item_counter += 1
            continue
        
    for Tubingen in os.listdir(input_directory): 
        while item_counter < range_3:
            tubingen_name = str(sample_list[item_counter][43:57])
            call (["./plink2","--threads","8","--make-bed","--allow-extra-chr","--chr","1-5","--vcf","%s" %(sample_list[item_counter]),"--max-alleles","2","--memory","12000","--out","%s/%s" %(outdir,tubingen_name)])
            item_counter += 1
            continue
        
    for Madeira in os.listdir(input_directory): 
        while item_counter < len(sample_list):
            madeira_name = str(sample_list[item_counter][43:57])
            call (["./plink2","--threads","8","--make-bed","--allow-extra-chr","--chr","1-5","--vcf","%s" %(sample_list[item_counter]),"--max-alleles","2","--memory","12000","--out","%s/%s" %(outdir,madeira_name)])
            item_counter += 1
            continue
    else:
        break