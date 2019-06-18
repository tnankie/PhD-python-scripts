import os
import re
import sys
import fileinput

def tidy_xvg(input_file,row):
    whole_file =[]
    output_file = "cleaned_" + input_file[:-3] + "csv"
    with open(input_file,'r') as name:
        with open(output_file,'wt') as new_file:
            for line in name:
                full = line
                ready = full.strip()
                ready = ready + "\n"
                ready=re.sub(r" ",',',ready)
                final=re.sub(r",+", ',',ready)
                new_file.write(final)         
            new_file.close()

dir_cont = os.listdir(".")
run_files = re.compile('lig_sum_[0-1][0-9].xvg')
for given_file in dir_cont:
    if run_files.search(given_file):
        tidy_xvg(given_file,24)
        print(given_file + " has been processed")

