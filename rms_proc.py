import re
import os
with open('run_01_rms.xvg') as raw:
    with open('run_01_rms_proc.csv','wt') as proc:
        count = 0
        for line in raw:
            full = line
            ready = full.strip()
            ready = ready+"\n"
            final=re.sub('\s',',',ready,count=1)
            if count>12:
                proc.write(final)
            count = count + 1
            
        proc.close()
with open('run_01_rms.xvg') as raw:
    with open('run_01_rms_proc.csv','wt') as proc:
        count = 0
        for line in raw:
            full = line
            ready = full.strip()
            ready = ready+"\n"
            final=re.sub('\s',',',ready,count=1)
            if count>12:
                proc.write(final)
            count = count + 1
            
        proc.close()
with open('run_02_rms.xvg') as raw:
    with open('run_02_rms_proc.csv','wt') as proc:
        count = 0
        for line in raw:
            full = line
            ready = full.strip()
            ready = ready+"\n"
            final=re.sub('\s',',',ready,count=1)
            if count>12:
                proc.write(final)
            count = count + 1
            
        proc.close()
with open('run_03_rms.xvg') as raw:
    with open('run_03_rms_proc.csv','wt') as proc:
        count = 0
        for line in raw:
            full = line
            ready = full.strip()
            ready = ready+"\n"
            final=re.sub('\s',',',ready,count=1)
            if count>12:
                proc.write(final)
            count = count + 1
            
        proc.close()
with open('run_04_rms.xvg') as raw:
    with open('run_04_rms_proc.csv','wt') as proc:
        count = 0
        for line in raw:
            full = line
            ready = full.strip()
            ready = ready+"\n"
            final=re.sub('\s',',',ready,count=1)
            if count>12:
                proc.write(final)
            count = count + 1
            
        proc.close()
with open('run_05_rms.xvg') as raw:
    with open('run_05_rms_proc.csv','wt') as proc:
        count = 0
        for line in raw:
            full = line
            ready = full.strip()
            ready = ready+"\n"
            final=re.sub('\s',',',ready,count=1)
            if count>12:
                proc.write(final)
            count = count + 1
            
        proc.close()
with open('run_06_rms.xvg') as raw:
    with open('run_06_rms_proc.csv','wt') as proc:
        count = 0
        for line in raw:
            full = line
            ready = full.strip()
            ready = ready+"\n"
            final=re.sub('\s',',',ready,count=1)
            if count>12:
                proc.write(final)
            count = count + 1
            
        proc.close()
with open('run_07_rms.xvg') as raw:
    with open('run_07_rms_proc.csv','wt') as proc:
        count = 0
        for line in raw:
            full = line
            ready = full.strip()
            ready = ready+"\n"
            final=re.sub('\s',',',ready,count=1)
            if count>12:
                proc.write(final)
            count = count + 1
            
        proc.close()
with open('run_08_rms.xvg') as raw:
    with open('run_08_rms_proc.csv','wt') as proc:
        count = 0
        for line in raw:
            full = line
            ready = full.strip()
            ready = ready+"\n"
            final=re.sub('\s',',',ready,count=1)
            if count>12:
                proc.write(final)
            count = count + 1
            
        proc.close()
with open('run_09_rms.xvg') as raw:
    with open('run_09_rms_proc.csv','wt') as proc:
        count = 0
        for line in raw:
            full = line
            ready = full.strip()
            ready = ready+"\n"
            final=re.sub('\s',',',ready,count=1)
            if count>12:
                proc.write(final)
            count = count + 1
            
        proc.close()            
with open('run_10_rms.xvg') as raw:
    with open('run_10_rms_proc.csv','wt') as proc:
        count = 0
        for line in raw:
            full = line
            ready = full.strip()
            ready = ready+"\n"
            final=re.sub('\s',',',ready,count=1)
            if count>12:
                proc.write(final)
            count = count + 1
            
        proc.close()
with open('npt_extension_rms.xvg') as raw:
    with open('npt_extension_rms_proc.csv','wt') as proc:
        count = 0
        for line in raw:
            full = line
            ready = full.strip()
            ready = ready+"\n"
            final=re.sub('\s',',',ready,count=1)
            if count>12:
                proc.write(final)
            count = count + 1
            
        proc.close()
with open('nvt_rms.xvg') as raw:
    with open('nvt_rms_proc.csv','wt') as proc:
        count = 0
        for line in raw:
            full = line
            ready = full.strip()
            ready = ready+"\n"
            final=re.sub('\s',',',ready,count=1)
            if count>12:
                proc.write(final)
            count = count + 1
            
        proc.close()            
with open('npt_rms.xvg') as raw:
    with open('npt_rms_proc.csv','wt') as proc:
        count = 0
        for line in raw:
            full = line
            ready = full.strip()
            ready = ready+"\n"
            final=re.sub('\s',',',ready,count=1)
            if count>12:
                proc.write(final)
            count = count + 1
            
        proc.close()   
        
    
