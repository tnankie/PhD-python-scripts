import re
import os
count = 1
while count <= 10:
    strcount = str(count)
    if count <= 9:
        strcount ="0" + str(count)
    nice = str(count - 5)
    command = "nohup mdrun -rerun *run_"+strcount+".xtc -s all_rf.tpr -deffnm run_3_"+strcount+" -nice "+nice+" &" 
    print(command)
    os.system(command)
    count = count + 1
