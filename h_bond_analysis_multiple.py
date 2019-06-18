import os
import re
import sys
import fileinput

def extract(name):
    count = 0
    numbers = []
    go = 'no'
    with open(name) as data:
        for line in data:
            if go =='yup':
                line = line.strip()
                line = re.sub('\s+',',',line)
                line = re.split(',',line)
                largest = 0
                int_line = []
                for i in line:
                    inte = int(i)
                    int_line.append(inte)
                sorted(int_line)
                numbers.append(int_line[1])              
                
                        
                
            if go == 'no' and re.match('\[ hbonds',line):
                go = 'yup'
                print('switch')
                offset = count
            count = count + 1
            
##    print(numbers) # this is the list of all h-bonds referenced in the .ndx file that form with the ligand need to get the appropriate water numbers then link them to bond with the protein then go to the maatrix file to x ref if any of those combinations form.
    count = 0
    m = 0
    short = []
    numbers.sort()
    for i in numbers:
        if int(i) != m:
            short.append(i)
        m = int(i)
    print('------------------',len(short))
    print(short)
    matrixline = []
    go ='no'
    print(name)
    elsename = name[:-5] +'c' + name[-4:]
    
    print(elsename)
    lig_mat_name = name[:-8] +'m_Bd.xpm' 
    prot_mat_name = name[:-8] +'m_Bc.xpm'
    print(lig_mat_name)
    print(prot_mat_name)
    bridged = 0
    for wats in short:
        lig_mat = []
        prot_mat = []
        go = 'no'
        lig_val = []
        prot_val = []
        with open(elsename) as data:
            for line in data:
                if go =='yup':
                    line = line.strip()
                    line = re.sub('\s+',',',line)
                    line = re.split(',',line)
                    
                    
                    for val in line:
                        if int(val) == int(wats):

                            prot_mat.append(count-offset -1)
                    
                if go == 'no' and re.match('\[ hbonds',line):
                    go = 'yup'
##                    print('switch 2')
                    offset = count
                count = count + 1
        go ='no'        
        with open(name) as data:
            for line in data:
                if go =='yup':
                    line = line.strip()
                    line = re.sub('\s+',',',line)
                    line = re.split(',',line)
                    
                    
                    for val in line:
                        if int(val) == int(wats):

                            lig_mat.append(count-offset -1)
                    
                if go == 'no' and re.match('\[ hbonds',line):
                    go = 'yup'
##                    print('switch 2')
                    offset = count
                count = count + 1
##        print('ligand matrix lines')
##        print(lig_mat)
##        print('----------------')
##        print('protein matrix lines')
##        print(prot_mat)
##        
##        print('++++++++++++++++++++++++++++++++++')
        with open(lig_mat_name) as mat_1:
            index = 0
            maxn = len(lig_mat)
            start = 'no'
            for line in mat_1:
                if line[0:4] == '/* y' and start == 'no':
                    start = 'yes'
##                    print('switch 3')
                    count = 0
                if line[0] == '"' and start == 'yes':
                    if index < maxn:
                        if count == int(lig_mat[index]):
                            lig_val.append(line[1:501])
                            index = index + 1
                    count = count + 1
        with open(prot_mat_name) as mat_1:
            index = 0
            maxn = len(prot_mat)
            start = 'no'
            for line in mat_1:
                if line[0:4] == '/* y' and start == 'no':
                    start = 'yes'
##                    print('switch 3')
                    count = 0
                if line[0] == '"' and start == 'yes':
                    if index < maxn:
                        if count == int(prot_mat[index]):
                            prot_val.append(line[1:501])
                            index = index + 1
                    count = count + 1
##        print('+++++++++++++++++++')
##        print(len(lig_val))
##        print(len(prot_val))
##        print('+++++++++++++++++++')
        j =  0
        il = 0
        ip = 0
        step = []
        bond = 'no'
        bridge = 'no'
        occupancy = 0
        while j < len(lig_val[0]):
            for i in lig_val:
                if i[j] == 'o':
                    bond = 'yes'
                    
            for i in prot_val:
                if i[j] == 'o' and bond =='yes':
                    bridge = 'yes'
            
            if bridge == 'yes':
                occupancy = occupancy + 1
##                print('A bridge is formed in step ',j,'? ',bridge)
            bond = 'no'
            bridge = 'no'
            j = j + 1
        print('in water ',wats,' the number of steps with a water bridge is ', occupancy)
        bridged = bridged + occupancy    
        
                
    print('in all timesteps there were ',bridged,' brigdes')
    return(short)



array = ['01', '02','03','04','05','06','07','08','09','10'] 
target='hbn_Bd'
t2 = 'hbn_Bc'
files = os.listdir()
files = sorted(files)
big_f =[]
count = 0
waters = []
more_w = []
for run in array:
    name = 'hbond_pro_run_'+run+'_hbn_Bd.ndx'
    print(name)
    waters = extract(name)
    


