import re
import os
target = 'sum_lig'
def itera(name):
    with open(name,'r') as data:
        record = []
        results = []
        for line in data:
            
            if re.match('[^#@]', line):
                line = line.strip()
                line = re.sub('\s+',',',line)
                line_a = re.split(',', line)
                if float(line_a[0]) > 50:
                    record.append(line_a)
                    
        print(len(record))
        print('in function call ', name )
        run_count = 1
        res = []
        for runs in range(1,11):
            entry = [0,0]
            experi = [entry[:]] * len(record)
            m = 0
            mi = 0
            
            for i in range(len(record)):
                entry[0] = record[i][runs]
                entry[1] = record[i][0]
                experi[i] = entry[:]       
            
            s_experi = sorted(experi, key=lambda peri: peri[0])
            results = ['run' + str(run_count),s_experi[426],s_experi[427],s_experi[428]]
            print(results)
            res.append(results[:])
            run_count = run_count + 1
##                if float(m) > float(record[i][runs]):
##                    m = record[i][runs]
##                    mi = i
##            finding = [record[mi][runs],record[mi][0]]
##            results.append(finding)
        return(res)

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

with open('all_min_90'+target[3:]+'.csv', 'wt') as output:
    for lines in summary:

        for i in range(len(lines)):
            newline = ''
            for val in lines[i]:
                newline = newline + str(val) + ','
            newline=re.sub('[[\]\']','',newline)
            if re.match('run',newline) == None:
                newline=re.sub(',','',newline)
            ready = newline + '\n'
            output.write(ready)
            
            
            
    
