# athalianamsmc
scripts for MSMC analysis of A.thaliana populations

currently WIP

features up until now:
- includes default fixedRecombination,-rhoOverMu,and -rhoOverMu+ fixedRecombination scenarios
- template for all chromosome runs
- read input files from destination / store filenames
- run MSMC/MSMC2 on .multihetsep.txt files and _reduced.multihetsep.txt files
- fixed time segmenting pattern for single chromosome runs
- counts runs and appends a number to the output
- iterates over up to 28 haplotypes in the input (2,4,6,8 haplotypes with fixed recombination)

ToDo:
- implement all chromosome runs into the final script
- general strategy : one big script with this approach or multiple smaller ones that can be run together in a batch job file ?!
