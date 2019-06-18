import re
import os
count = 1
while count <= 10:
    strcount = str(count)
    if count <= 9:
        strcount ="0" + str(count)
    command = "g_energy -sum -f run_2_"+strcount+".edr -o lig_enr_"+strcount+" < lig_edr.txt"
    os.system(command)
    count = count + 1
