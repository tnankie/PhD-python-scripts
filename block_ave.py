##this is supposed to be about block averaging
import re
import os



first = 0    #first time step to use
last = 1000  #last time step to use
splits = 1   #number of sub blocks to analyse
#def average(data, block)


def block(data,n):
    ntot=len(data)
    pair=divmod(ntot, n)
    nnew=int(pair[0])
##    print(ntot, ' ntot', pair, ' pair', nnew, ' nnew')
    # print(data)
    x = []
##    print(x)
    y= []
    summy = 0
    ite = 0
    count = 0
##    print(data[0], len(data), len(data[0]))
    
    for vals in data:
        vals=float(vals[1])
        ite += 1
        if ite < (n):
##            print('types, summy then val ', type(summy), type(vals))
            summy= summy + vals
            
##            print('value of summy then ite ', summy, ite)
        else:
            summy= summy + vals
##            print('should be writing summy to x here ', summy/ite)
            x.append(summy/ite)
            summy=0
            ite =0

##    print('residuals are summy, ite, nnew ', summy, ite, nnew)
    ite = 0
    count = 0
    summy =0 
##    for vals in data:
##        vals = float(vals[1])
##        ite += 1
##        if ite < n:
##            summy = ((vals - x[count])**2) + summy
##        else:
####            print(ite, n, ' is ite and n')
##            summy = ((vals - x[count])**2) + summy
##            y.append((summy/ite)**0.5)
##            count += 1
##            ite = 0
##            summy = 0
####    print('is this wrong y? ', y)
##    if ite != (nnew-1) and ite !=0:
##        y.append((summy/ite)**0.5)
##    print('this is y ',y)

          
##        y[i]=sum(data[1][(i*n):((i+1)*n)])/float(n)
##    print(x, ' value of x')
    return x

def go_time(name):
    print(name)
    with open(name,'r') as data:
        new_name = 'bl_av_' + name[:-3] + 'csv'
        with open(new_name, 'wt') as output:
            struct = []
            for lines in data:
                lines = lines.strip()
                if not re.match(rel_data, lines):
                    lines = re.sub('\s+',',',lines)
                    lines = re.split(',', lines)
                    struct.append(lines)
                    #print(struct[-1][-1])
            #print(len(struct))
            #print(len(struct[0]))
            #print(struct[0][0])
            blocks =[1]
            biggest = 2
##            while biggest < len(struct):
##                blocks.append(biggest)
##                if biggest < len(struct):
##                    print(biggest, len(struct))
##                    biggest = biggest * 2
####            print(blocks)
            averages=[]
            varia = []
            index = 0
##            orig_struct = struct.copy()
##            print('checking reverse pre', struct[0], orig_struct[0])
            struct.reverse() # reverse the order so that we can discard from the begining (unequilibrated) not the end.
##            print('checking reverse post', struct[0], orig_struct[0])
            

            
            header = 'ave,ag,var,stdev,count \n'
            output.write(header)
            for i in range(1,100):
##                print(i, ' value of i')
                line = (block(struct,i))
                summy = 0
                for ii in line:
                    summy = summy + ii
                ave = summy/len(line)
                ag = 0
                for ii in line:
                    ag = ag + ((ii - ave)**2)
                stdev = (ag / len(line))**0.5
                var = stdev ** 2

##                print(ag, stdev, var, ' is ag, stdev, var respectively')
                csv = str(ave) + ',' + str(ag) + ',' + str(var) + ',' + str(stdev) + ',' + str(len(line))
                print(csv)
                for elem in line:
                    csv = csv + ',' + str(elem)
                csv =csv + '\n'
                
                output.write(csv)
            
                
            

rel_data = re.compile('#|@')
intrest =re.compile('run_2_\d\d_CE.xvg')
dire = os.listdir()
for files in dire:
    if re.search(intrest, files):
        go_time(files)
    else:
        print(files + ' is the wrong file type')
    
