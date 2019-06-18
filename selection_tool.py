import re
import os

num_a = []
atom_a =[]
with open('test_load_file.csv','r') as nums:
    count = 0
    for line in nums:
        if count > 0:
            line = line.strip()
            line = re.split(',',line)
            num_a.append(line)
            

        count = count + 1
        

with open('resnum.pdb','r') as atoms:
    count = 0
    for line in atoms:
        if count >3:
            line = line.strip()
            line = re.sub('\s+',',',line)
            line = re.split(',',line)
            atom_a.append(line)
        count = count + 1
    
count = 0
sup_set =[]
for vals in atom_a:
    if len(vals) >6:
        if vals[2] == 'CA':
##            print(vals)
            if int(vals[1]) < 9127:
                for sup_res in num_a:
                    if int(vals[5]) == int(sup_res[1]):
                        if sup_res[0] == 'A':
                            sup_set.append(vals)
            if int(vals[1]) > 9126:
                for sup_res in num_a:
                    if int(vals[5])-560 == int(sup_res[1]):
                        if sup_res[0] == 'B':
                            sup_set.append(vals)
                
                    
               
    count = count + 1
with open('supset_atoms.txt','w+') as output:
    for atoms in sup_set:
        output.write(str(atoms[1]) + ' ')
        print(atoms[1], atoms[3], atoms[4], atoms[5])
