import os
import re
with open('run_01_lie.csv','r') as raw:
    with open ('summary_lie.csv','wt') as summary:
        for line in raw:
            summary.write(line)
if os.path.isfile('old.csv') == True:
    os.remove("old.csv")
os.rename('summary_lie.csv', 'old.csv')
with open('run_02_lie.csv','r') as raw:
    with open('old.csv','r') as old:
        with open ('summary_lie.csv','wt+') as summary:
            for line in raw:
                line2 = old.readline()
                com=False
                count=0
                mod=line2[0:-1]
                while com==False:
                    if line[count]==',':
                        com=True
                    else:
                        count = count + 1
                newline=mod+line[count:-1]+'\n'
                summary.write(newline)
if os.path.isfile('old.csv') == True:
    os.remove("old.csv")
os.rename('summary_lie.csv', 'old.csv')
with open('run_03_lie.csv','r') as raw:
    with open('old.csv','r') as old:
        with open ('summary_lie.csv','wt+') as summary:
            for line in raw:
                line2 = old.readline()
                com=False
                count=0
                mod=line2[0:-1]
                while com==False:
                    if line[count]==',':
                        com=True
                    else:
                        count = count + 1
                newline=mod+line[count:-1]+'\n'
                summary.write(newline)
if os.path.isfile('old.csv') == True:
    os.remove("old.csv")
os.rename('summary_lie.csv', 'old.csv')
with open('run_04_lie.csv','r') as raw:
    with open('old.csv','r') as old:
        with open ('summary_lie.csv','wt+') as summary:
            for line in raw:
                line2 = old.readline()
                com=False
                count=0
                mod=line2[0:-1]
                while com==False:
                    if line[count]==',':
                        com=True
                    else:
                        count = count + 1
                newline=mod+line[count:-1]+'\n'
                summary.write(newline)
if os.path.isfile('old.csv') == True:
    os.remove("old.csv")
os.rename('summary_lie.csv', 'old.csv')
print('ping')
with open('run_05_lie.csv','r') as raw:
    with open('old.csv','r') as old:
        with open ('summary_lie.csv','wt+') as summary:
            for line in raw:
                line2 = old.readline()
                com=False
                count=0
                mod=line2[0:-1]
                while com==False:
                    if line[count]==',':
                        com=True
                    else:
                        count = count + 1
                newline=mod+line[count:-1]+'\n'
                summary.write(newline)
if os.path.isfile('old.csv') == True:
    os.remove("old.csv")
os.rename('summary_lie.csv', 'old.csv')
print('ping')
with open('run_06_lie.csv','r') as raw:
    with open('old.csv','r') as old:
        with open ('summary_lie.csv','wt+') as summary:
            for line in raw:
                line2 = old.readline()
                com=False
                count=0
                mod=line2[0:-1]
                while com==False:
                    if line[count]==',':
                        com=True
                    else:
                        count = count + 1
                newline=mod+line[count:-1]+'\n'
                summary.write(newline)
if os.path.isfile('old.csv') == True:
    os.remove("old.csv")
os.rename('summary_lie.csv', 'old.csv')
print('ping')
with open('run_07_lie.csv','r') as raw:
    with open('old.csv','r') as old:
        with open ('summary_lie.csv','wt+') as summary:
            for line in raw:
                line2 = old.readline()
                com=False
                count=0
                mod=line2[0:-1]
                while com==False:
                    if line[count]==',':
                        com=True
                    else:
                        count = count + 1
                newline=mod+line[count:-1]+'\n'
                summary.write(newline)
if os.path.isfile('old.csv') == True:
    os.remove("old.csv")
os.rename('summary_lie.csv', 'old.csv')
with open('run_08_lie.csv','r') as raw:
    with open('old.csv','r') as old:
        with open ('summary_lie.csv','wt+') as summary:
            for line in raw:
                line2 = old.readline()
                com=False
                count=0
                mod=line2[0:-1]
                while com==False:
                    if line[count]==',':
                        com=True
                    else:
                        count = count + 1
                newline=mod+line[count:-1]+'\n'
                summary.write(newline)
if os.path.isfile('old.csv') == True:
    os.remove("old.csv")
os.rename('summary_lie.csv', 'old.csv')
print('ping')
with open('run_09_lie.csv','r') as raw:
    with open('old.csv','r') as old:
        with open ('summary_lie.csv','wt+') as summary:
            for line in raw:
                line2 = old.readline()
                com=False
                count=0
                mod=line2[0:-1]
                while com==False:
                    if line[count]==',':
                        com=True
                    else:
                        count = count + 1
                newline=mod+line[count:-1]+'\n'
                summary.write(newline)
if os.path.isfile('old.csv') == True:
    os.remove("old.csv")
os.rename('summary_lie.csv', 'old.csv')
print('ping')
with open('run_10_lie.csv','r') as raw:
    with open('old.csv','r') as old:
        with open ('summary_lie.csv','wt+') as summary:
            for line in raw:
                line2 = old.readline()
                com=False
                count=0
                mod=line2[0:-1]
                while com==False:
                    if line[count]==',':
                        com=True
                    else:
                        count = count + 1
                newline=mod+line[count:-1]+'\n'
                summary.write(newline)
if os.path.isfile('old.csv') == True:
    os.remove("old.csv")
print('done')

