import os
import re
import sys
import fileinput

target='_ndx.ndx'
def merge(name):
    count = 0
    numbers = []
    with open(name) as data:
        for line in data:
            line = line.strip()
            if re.match('[^\[\s]', line):
                
                line = re.sub('\s+',',',line)
                line = re.split(',',line)
                
                for i in line:
                    if i is not None:
                        numbers.append(int(i))
                
                
            count = count + 1
    numbers = sorted(numbers)
    short = []
    m = 0
    count = 0
    for i in numbers:
        if i != m:
            short.append(numbers[count])
        
        
##        if count < 15:
##            print('i is ',i)
##            print('i is ',numbers[count])
##            print('m is ',m)
        m = numbers[count]
        count = count + 1
##    print(numbers[0:100])
##    print(short[0:100])
##    with open('merge_'+name,'w') as out:
##        out.write('[Ball]\n')
##        for i in short:
##            out.write(str(i)+'\n')
    return short
           

files = os.listdir()
files = sorted(files)
big_f =[]
count = 0
total = []
for run in files:
    
    if re.search(target,run):
        print(run)
        total = total + merge(run)
print(len(total))
total = sorted(total)
m = 0
sub_tot = []
count = 0
for i in total:
    if i != m:
        sub_tot.append(total[count])
    m = total[count]
    count = count + 1
print(len(sub_tot))
with open ('ball_sum.ndx','w+') as out:
    out.write('[Ball]\n')
    for i in sub_tot:
        out.write(str(i)+' ')
        
        
        

