import re 
import fileinput
import os
A_offset = 0
B_offset = -1
C_offset = -564
def renumber(name):
    with open(name) as original:
        alpha = re.compile(' A [ 0-9]+')
        beta = re.compile(' B [ 0-9]+')
        gama = re.compile('MODEL ')
        delta = re.compile(' C [ 0-9]+')
        output = "re_"+name
        print(output)
        with open(output,'wt') as renumbered:
            for line in original:
                a_chain = alpha.search(line)
                b_chain = beta.search(line)
                c_chain = delta.search(line)
                model = gama.search(line)
                if a_chain:
                    begin=line[0:22]
                    ending=line[26:]
                    residue=line[22:26]
                    residue_num=int(residue)
                    A_init=residue_num + A_offset
                    if A_init<0:
                        modified="  "+str(A_init)
                    elif A_init<10:
                        modified="   "+str(A_init)
                    elif A_init<100:
                        modified="  "+str(A_init)
                    elif A_init<1000:
                        modified=" "+str(A_init)
                    elif A_init<10000:
                        modified=""+str(A_init)
                    else:
                        break             
                    newstring=begin+modified+ending
                    renumbered.write(newstring)
                elif b_chain:
                    begin=line[0:22]
                    ending=line[26:]
                    residue=line[22:26]
                    residue_num=int(residue)
                    B_init=residue_num + B_offset 
                    if B_init<0:
                        modified="  "+str(B_init)
                    elif B_init<10:
                        modified="   "+str(B_init)
                    elif B_init<100:
                        modified="  "+str(B_init)
                    elif B_init<1000:
                        modified=" "+str(B_init)
                    elif B_init<10000:
                        modified=""+str(B_init)
                    else:
                        break             
                    newstring=begin+modified+ending
                    renumbered.write(newstring)
                elif c_chain:
                    begin=line[0:22]
                    ending=line[26:]
                    residue=line[22:26]
                    residue_num=int(residue)
                    C_init=residue_num + C_offset 
                    if C_init<0:
                        modified="  "+str(C_init)
                    elif C_init<10:
                        modified="   "+str(C_init)
                    elif C_init<100:
                        modified="  "+str(C_init)
                    elif C_init<1000:
                        modified=" "+str(C_init)
                    elif C_init<10000:
                        modified=""+str(C_init)
                    else:
                        break             
                    newstring=begin+modified+ending
                    renumbered.write(newstring)
                elif model:
                    pass
                else:
                    renumbered.write(line)
        print(name," has been processed and re_",name,"has been written to the directory.")
contents = os.listdir(".")
runfiles = re.compile(r"^run.*min\.pdb$")
print(len(contents),"there are that many files in directory")
counts = 0
not_runfiles = 0
for entry in contents:
    hit = runfiles.search(entry)
    if hit:
        counts = counts + 1
        renumber(entry)
    else:
        not_runfiles = not_runfiles + 1
files = not_runfiles + counts
print("there were ",files," files, and there were ",counts," minimised files and "
      ,not_runfiles," other files")

      
        
    
    
    

