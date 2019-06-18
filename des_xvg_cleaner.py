import os
import re
import sys
import fileinput

def tidy_xvg(input_file,row):
    whole_file =[]
    output_file = "cleaned_" + input_file[:-3] + "csv"
    with open(input_file,'r') as name:
        count = 0
        for line in name:
            if count > row:
                cleaned = line.lstrip()
    ##            print(line)
    ##            print(cleaned)
                cleaned = re.sub('[ ]+',',',cleaned)
                two_part = re.split(',',cleaned)
##                print(two_part[0])
##                print(two_part[1])
                two_part[0] = "w_" + str((int(two_part[0])-50)/2)
##                print(two_part[0])
                whole = two_part[0] + "," + two_part[1]
##                print(whole)
                whole_file.append(whole)
            count = count + 1
##    whole_file.sort()
    with open(output_file,'wt') as new_file:
        for line in whole_file:
            line = line[2:]
            new_file.write(line)

dir_cont = os.listdir(".")
run_files = re.compile('des_run_[0-1][0-9]_clid.xvg')
for given_file in dir_cont:
    if run_files.search(given_file):
        tidy_xvg(given_file,14)
        print(given_file + " has been processed")

