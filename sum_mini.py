import re
import os

def stuff(name):
    with open(name,'r') as data:
        new_name = 'sum_mini' + name[:-3] 
        goodies = []
        count = 0
        for lines in data:
            lines = re.split(',',lines)
            if lines[5] != '0.0':
                goodies.append(lines[5])
            count += 1
        
       
        return(goodies)


rel_data = re.compile('stuff')
interest = re.compile('bl_av_minirun_2_\d\d_CE.csv')
dire = os.listdir()
dire.sort()
sumsum = []
new_name = ''
for files in dire:
    if re.search(interest, files):
        content = stuff(files)
        sumsum.append(content)
        new_name = 'sum_block' + files[2:-3] + 'csv'
    else:
        print(files + ' is not interesting')
##print(sumsum, ' is sumsum')
##print(sumsum[0], ' is sumsum[0]')
##print(sumsum[0][0],' is sumsum[0][0]')

    
for a in range(0,len(sumsum)):
    sumsum[a][0] = re.sub('\n', '',sumsum[a][0])
    print(sumsum[a][0], ' is the sumsum[a][0]. oh and a is ', a)
        
with open(new_name,'wt') as output:
    for lines in sumsum:
        bits = ''
        for ele in lines:
            bits = bits + ele + ','
        bits = bits + '\n'
            
        output.write(str(bits))

with open('sum_block_av_minirun_2_10_CE.csv', 'r') as stuff:
    with open('sumsum.csv','wt') as output:
        master =[]
        filler = []
        temp =[]
        for lines in stuff:
            lines = re.split(',',lines)
            gap = 1
            count = 0
            for ele in lines:
                
                if ele == 'phi' and count == gap:
                    output.write(',\n')
                
                    
                if ele == '£':
                    count = count + 1
                    
                else:
                    if count == gap:
                        output.write(str(ele) + ',')

       
                    
