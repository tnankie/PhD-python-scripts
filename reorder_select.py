import re 
import fileinput
import os
A_offset = 0
B_offset = -1
C_offset = -564
def reorder(name):
    with open(name) as original:
        alpha = re.compile('{A-Z] A[ 0-9]{4}')
        beta = re.compile('[A-Z] B[ 0-9]{4}')
        gama = re.compile('MODEL ')
        delta = re.compile('[A-Z] C[ 0-9]{4}')
        output = "reord_"+name
        print(output)
        with open(output,'wt') as renumbered:
            for line in original:
                a_chain = alpha.search(line)
                b_chain = beta.search(line)
                c_chain = delta.search(line)
                model = gama.search(line)
                if a_chain:
                    begin=line[0:21]
                    ending=line[22:]
                    residue=line[21:22]
                    residue="C"
                    newstring=begin+residue+ending
                    renumbered.write(newstring)
                elif b_chain:
                    begin=line[0:21]
                    ending=line[22:]
                    residue=line[21:22]
                    residue="A"
                    newstring=begin+residue+ending
                    renumbered.write(newstring)
                elif c_chain:
                    begin=line[0:21]
                    ending=line[22:]
                    residue=line[21:22]
                    residue="B"
                    newstring=begin+residue+ending
                    renumbered.write(newstring)
                elif model:
                    pass
                else:
                    renumbered.write(line)
        print(name," has been processed and reord_",name,"has been written to the directory.")
contents = os.listdir(".")
runfiles = re.compile(r"^des_run.*\.pdb$")
print(len(contents),"there are that many files in directory")
counts = 0
not_runfiles = 0
for entry in contents:
    hit = runfiles.search(entry)
    if hit:
        counts = counts + 1
        reorder(entry)
    else:
        not_runfiles = not_runfiles + 1
files = not_runfiles + counts
print("there were ",files," files, and there were ",counts," renumbered minimised files and "
      ,not_runfiles," other files")

      
        
    
    
    

