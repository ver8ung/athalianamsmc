#!/bin/bash
#assuming input file is tabix indexed and gzipped, iterate over files to extract chromosomes 1-5 using bcftools
#automatically index all select files

for file in /data/home/users/m.ruscheweyh/Africansamps/madeira*
        do
	        /data/proj/teaching/NGS_course/Softwares/bcftools-1.3/bin/bcftools index $file && echo indexed $file
                /data/proj/teaching/NGS_course/Softwares/bcftools-1.3/bin/bcftools view -I -Oz $file --regions 1 > $file.chr1.vcf.gz && echo extracted chromosome 1
		/data/proj/teaching/NGS_course/Softwares/bcftools-1.3/bin/bcftools view -I -Oz $file --regions 2 > $file.chr2.vcf.gz && echo extracted chromosome 2
		/data/proj/teaching/NGS_course/Softwares/bcftools-1.3/bin/bcftools view -I -Oz $file --regions 3 > $file.chr3.vcf.gz && echo extracted chromosome 3
		/data/proj/teaching/NGS_course/Softwares/bcftools-1.3/bin/bcftools view -I -Oz $file --regions 4 > $file.chr4.vcf.gz && echo extracted chromosome 4
		/data/proj/teaching/NGS_course/Softwares/bcftools-1.3/bin/bcftools view -I -Oz $file --regions 5 > $file.chr5.vcf.gz && echo extracted chromosome 5, moving on to next input file
done
