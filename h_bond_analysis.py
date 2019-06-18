import os
import re
import sys
import fileinput


def extract(name):
    count = 0
    numbers = []
    go = 'no'
    acceptors =[5,14,16,23,24,27]
    with open(name) as data:
        for line in data:
            if go =='yup':
                line = line.strip()
                line = re.sub('\s+',',',line)
                line = re.split(',',line)
                
                for i in acceptors:
##                    if count > 5440:
##                        print(line)
##                        print(i)
##                        print(line[2])
                    if int(line[2]) == i:
                        numbers.append(line[0])
                        
                
            if go == 'no' and re.match('\[ hbonds',line):
                go = 'yup'
                print('switch')
                offset = count
            count = count + 1
    print(numbers) # this is the list of all h-bonds referenced in the .ndx file that form with the ligand need to get the appropriate water numbers then link them to bond with the protein then go to the maatrix file to x ref if any of those combinations form.
    count = 0
    m = 0
    short = []
    
    for i in numbers:
        if int(i) != m:
            short.append(i)
        m = int(i)
   
    return(short)

def h_bonds(name,water):
    count = 0
    numbers = []
    go = 'no'
    with open(name) as data:
        for line in data:
            if go =='yup':
                line = line.strip()
                line = re.sub('\s+',',',line)
                line = re.split(',',line)
                
                for i in water:
##                    if int(line[2]) == 5:
##                        print(line)
##                        print(i)
##                        print(line[0])
                    if int(line[0]) == int(i):
##                        print('hit')
                        print(line)
                        numbers.append(count-offset +1)
                
            if go == 'no' and re.match('\[ hbonds',line):
                go = 'yup'
                print('switch 2')
                offset = count
            count = count + 1
        print(numbers)
    ghastly = []
    with open('hbond_pro_run_01_hbm_B.xpm') as matrix:
        index = 0
        maxn = len(numbers)
        print(maxn)
        start ='no'
        for line in matrix:
            
            
            if line[0:4] == '/* y' and start == 'no':
                
                start = 'yes'
                print('switch 3')
                count = 0
##            while index < maxn:
            if line[0] == '"' and start == 'yes':
##                print(count,' c..... ', int(numbers[index]), '.....number')
                if index < maxn:
                    if count == int(numbers[index]):
##                        print(line)
                        ghastly.append(line[1:501])
##                        print(line[501])
##                        print(line[502])
##                        print(line[503])
##                        print(line[504])
##                        print('gap-------------------------')
                        
                        index =  index + 1
                count = count + 1
        print(len(ghastly))
        i = 0
        choices = []
        store = []
        m=0
        while i < len(numbers):
            
            if numbers[i] - numbers[i-1] > 1:
                store = m,i-1
                choices.append(store[:])
                m = i
                
##                print(numbers[i],' - ',numbers[i-1])
            i = i +1
        store = m+1,len(numbers)-1  #final values
        choices.append(store[:])
        print(choices)

            
        
        i = 0
        watnum = 1
        for water in choices:
            i = water[0]
            j=0
            step = []
            bond = 'no'
            bridge = 'no'
            occupancy = 0
            while j < len(ghastly[0]):
                while i < water[1]:
                    if ghastly[i][j] == 'o':
                        
                        if bond == 'yes':
                            bridge = 'yes'
##                            print('bridge to ',i)
                        bond = 'yes'
    ##                    print('bond from ',i)
                    i = i +1
                if bridge == 'yes':
                    occupancy = occupancy + 1
                    
    ##            print('step ',j,' has a bond? ',bond)
##                    print('step ',j,' has a bridge? ',bridge)
                bond = 'no'
                bridge = 'no'
    ##            print('------')
                i = water[0]
                j = j + 1
            print('in water ',watnum,' the number of steps with a water bridge is ', occupancy)
            watnum = watnum + 1
            
                
                
                
                
    
                
target='hbn_B'
t2 = 'hbm_B'
files = os.listdir()
files = sorted(files)
big_f =[]
count = 0
for run in files:
    if re.search(target,run):
        print(run)
        waters = extract(run)
        
        h_bonds(run,waters)
