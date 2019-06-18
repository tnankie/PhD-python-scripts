import re
import os
sol_search = re.compile('.*.xvg')
run_search = re.compile('..*run_2.*energy.*xvg')
def proc_sol(name):
    data = re.compile('\A[,1]')
    with open(name) as file:
        print(name)
        new_name = "out_" + name[:-3] + "csv"
        with open(new_name,'w+') as output:
            count = 0
            for line in file:
                full = line
                ready = full.strip()
                ready = ready+"\n"
                ready=re.sub(r" ",',',ready)
                final=re.sub(r",+", ',',ready)
                output.write(final)
            output.close()
                
        
            
all_files = os.listdir()
count = 0
for line in all_files:
    if sol_search.search(line):
        proc_sol(line)
    
