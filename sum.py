import re
import os

def stuff(name):
    with open(name,'r') as data:
        new_name = 'sum_' + name[:-3] 
        goodies = []
        count = 0
        for lines in data:
            lines = re.split(',',lines)
                      
            if count < 501:
                
                goodies.append(lines[1])
            count += 1
        
       
        return(goodies)


rel_data = re.compile('stuff')
interest = re.compile('raw_run_2_\d\d_CE.csv')
dire = os.listdir()
sumsum = []
new_name = ''
for files in dire:
    if re.search(interest, files):
        content = stuff(files)
        sumsum.append(content)
        new_name = 'sum_' + files[:-3] + 'csv'
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
