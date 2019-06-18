import os
import re

with open('sum_energy_qual_all.csv','r') as input:
    with open('e_q__end_s1.csv','w') as set1:
        with open('e_q__end_s2.csv','w') as set2:
            with open('e_q__end_s3.csv','w') as set3:
                with open('e_q__end_s4.csv','w') as set4:
                    with open('e_q__end_s5.csv','w') as set5:
                        set1.write('time,run_01,run_02\n')
                        set2.write('time,run_03,run_04\n')
                        set3.write('time,run_05,run_06\n')
                        set4.write('time,run_07,run_08\n')
                        set5.write('time,run_09,run_10\n')
                        for line in input:
                            line = re.split(',',line)
                            ls1 = str(line[0]) + ',' +str(line[1]) +',' +str(line[2]) +'\n'
                            set1.write(ls1)
                            ls2 = str(line[0]) + ',' +str(line[3]) +',' +str(line[4]) +'\n'
                            set2.write(ls2)
                            ls3 = str(line[0]) + ',' +str(line[5]) +',' +str(line[6]) +'\n'
                            set3.write(ls3)
                            ls4 = str(line[0]) + ',' +str(line[7]) +',' +str(line[8]) +'\n'
                            set4.write(ls4)
                            ls5 = str(line[0]) + ',' +str(line[9]) +',' +str(line[10]) +'\n'
                            set5.write(ls5)
        
        
        
        
        
