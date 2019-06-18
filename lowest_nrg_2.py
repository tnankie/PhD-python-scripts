import re
import os
target = 'sum_all'
def itera(name):
    with open(name,'r') as data:
        record = []
        results = []
        for line in data:
            
            if re.match('[^#@]', line):
                line = line.strip()
                line = re.sub('\s+',',',line)
                line_a = re.split(',', line)
                if float(line_a[0]) > 949:
                    record.append(line_a)
                    
        print(record[5][0])
        print('in function call ', name )
        for runs in range(1,11):
            m = 0
            mi = 0
            for i in range(len(record)):
                if float(m) > float(record[i][runs]):
                    m = record[i][runs]
                    mi = i
            finding = [record[mi][runs],record[mi][0]]
            results.append(finding)
        return(results)

files = os.listdir('./')
files = sorted(files)
summary = []
for run in files:
    if re.search(target,run):
        print('pre function call ',run)
        mins = itera(run)
        runy = [run, 'ignore']
        summary.append(runy)
        summary.append(mins)

with open('all_min_'+target[3:]+'.csv', 'wt') as output:
    for lines in summary:

        for i in range(len(lines)):
            newline = ''
            for val in lines[i]:
                newline = newline + str(val) + ','
            ready = newline + '\n'
            output.write(ready)
            
            
            
    
