import os
import re
import sys
import fileinput

def run_it_now(input_file):
    base = input_file[:-3]
    output_name = input_file[:-4]
    bash = "trjconv -f "+base+"xtc -o "+output_name+"_.pdb -s "+base+"tpr -pbc whole -b 50 -conect -sep -nzero 3 < not_water.txt"
    os.system(bash)
    print(bash)

dir_cont = os.listdir(".")
run_files = re.compile('run_[0-1][0-9].xtc')
for given_file in dir_cont:
    if run_files.search(given_file):
        run_it_now(given_file)
        print(given_file + " is elligible")



