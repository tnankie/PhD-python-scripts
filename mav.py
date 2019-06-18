import re
import os

def block(data, n):
    ntot=len(data)
    mav = 1
    return(mav)

def go_time(name):
    print(name, ' is da shizz')
    with open(name, 'r')  as data:
        new_name = 'mav_' + name[:-3] + 'csv'
        with open(new_name, 'wt') as output:
            struct = []
            for lines in data:
                lines = lines.strip()
                if not re.match(rel_data, lines):
                    lines = re.sub('\s+',',',lines)
                    lines = re.split(',', lines)
                    struct.append(lines)
            print(struct[1][2])
            struct.reverse()
            count = 0
            mav = []
##            for lines in struct:
##                if count > 1 and count < 498:
##                    temp =
            slope = ['n/a']
            for i in range(2,499):
                temp = 0
                for b in range(i-2,i+2):
                    temp = float(struct[b][2]) + temp
                temp = temp/5
                mav.append(temp)
            for i in range(1,len(mav)-1):
                temp = mav[i-1] - mav[i+1]
                temp = temp/2
                slope.append(temp)
            slope.append('n/a')
            print(len(mav), len(slope), ' mav slope')
            for i in range(0,len(slope)):
                lines = str(mav[i]) + ',' + str(slope[i]) + ',\n'
                output.write(lines)
            with open('raw_' + name[:-3] +'csv','wt') as raw:
                for i in struct:
                    temp = ''
                    for bits in i:
                        temp = temp + str(bits) + ','
                    temp = temp + '\n'
                    raw.write(temp)
                        
            
                
                
            
##            for lines in mav:
##                lines = str(lines) +',\n'
##                output.write(lines)
rel_data = re.compile('#|@')
intrest =re.compile('run_2_\d\d_CE.xvg')
dire = os.listdir()
for files in dire:
    if re.search(intrest, files):
        go_time(files)
    else:
        print(files + ' is the wrong file type')
    
