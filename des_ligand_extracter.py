import re
import os
import sys

is_pdb = re.compile(r're_reord_des.*\.pdb')
current_dir_contents = os.listdir(os.getcwd())
for entry in current_dir_contents:
    if is_pdb.search(entry):
        with open(entry) as base:
            new_name = 'lig_' + entry[9:]
            print('this is a big fat blank')
            with open(new_name,'wt') as lig:
                count = 0
                for line in base:
                    if count <59:
                        formated = line[:-1]
                        lig.write(line)
                    count = count + 1
                    
                
