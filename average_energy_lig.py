import re
import os

target ='_lig_enr_'
def itera(name):
    with open(name) as data:
##        print(name)
        count = 0
        record =[]
##        print(record,"should be blank")
        icount =0
        tom = [icount,icount]
        while icount < 10:
            record.append(tom)
            icount = icount +1
##        print(record,"should be uniform")
        for line in data:
            if re.match('[^#@]', line):
##                print(line)
                line = line.strip()
##                print(line)
                line = re.sub('\s+',',',line)
##                print(line)
                lit_f = re.split(',', line)
                
                if float(lit_f[0]) > 949:
                    print(record)
                    print(lit_f)
##                    print(lit_f[0])
                    itter = 1
                    newrecord = []
                    for item in record:
                        print(item)
                        print(float(lit_f[itter]))
                        if item[1] > float(lit_f[itter]):
                            item[0] = float(lit_f[0])
                            item[1] = float(lit_f[itter])
                        newrecord.append(item)
                        print(newrecord)
                        itter = itter + 1

                        
                        
                    record = newrecord
                        
##                print(lit_f)
##                print(big_f[count])
##                big_f[count].append(lit_f[1])
##                print(big_f[count])
##                print(line[1])
                count = count + 1
        print(record)
        
files = os.listdir("./")
files = sorted(files)

big_f =[]
count = 0
print(files)
print('\n', "blank")
for run in files:
##    print(target, run)
    if re.search(target,run):
        
        count = count + 1
##        print(count)
        print(run)
        if count == 1:
            with open(run) as init:
                print('init start')
                for lines in init:
                    if re.match('[^#@]', lines):
##                        print(lines)
                        lines = lines.strip()
##                        print(lines)
                        lines = re.sub('\s+',',',lines)
##                        print(lines)
                        lines = re.split(',', lines)
##                        print(lines)
##                        lines = lines + '\n'
##                        print(lines)
##                        print('did it')
                    
##                        big_f.append(lines)
##            print(big_f)
        if count > 1:
            itera(run)
            
          
with open('extract_' + target + '_all.csv', 'w') as output:
    for lines in big_f:
        
        newline = ''
        for val in lines:
            newline = newline + str(val) + ','
        ready = newline + '\n'
        output.write(ready)
    
