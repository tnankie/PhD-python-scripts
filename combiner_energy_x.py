import re
import os

target ='3is9_hbond'
def itera(name):
    with open(name) as data:
##        print(name)
        count = 0
        for line in data:
            if re.match('[^#@]', line):
##                print(line)
                line = line.strip()
##                print(line)
                line = re.sub('\s+',',',line)
##                print(line)
                lit_f = re.split(',', line)
##                print(lit_f)
##                print(big_f[count])
                big_f[count].append(lit_f[1])
##                print(big_f[count])
##                print(line[1])
                count = count + 1
        
files = os.listdir("./")
files = sorted(files)
big_f =[]
count = 0
print(files)
print('\n', "blank")
for run in files:
    
    if re.match(target,run):
##        print(count)
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
                    
                        big_f.append(lines)
##            print(big_f)
        if count > 1:
            itera(run)
          
with open('sum_' + target + '.csv', 'w') as output:
    for lines in big_f:
        
        newline = ''
        for val in lines:
            newline = newline + str(val) + ','
        ready = newline + '\n'
        output.write(ready)
    
