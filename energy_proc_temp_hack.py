import re
import os
with open('run_01_energy.xvg') as raw:
    with open('run_01_energy_proc.csv','wt') as proc:
        count = 0
        for line in raw:
            full = line
            ready = full.strip()
            ready = ready+"\n"
            ready=re.sub(r" ",',',ready)
            final=re.sub(r",+", ',',ready)
            proc.write(final)         
        proc.close()
with open('run_02_energy.xvg') as raw:
    with open('run_02_energy_proc.csv','wt') as proc:
        count = 0
        for line in raw:
            full = line
            ready = full.strip()
            ready = ready+"\n"
            ready=re.sub(r" ",',',ready)
            final=re.sub(r",+", ',',ready)
            proc.write(final)         
        proc.close()
with open('run_03_energy.xvg') as raw:
    with open('run_03_energy_proc.csv','wt') as proc:
        count = 0
        for line in raw:
            full = line
            ready = full.strip()
            ready = ready+"\n"
            ready=re.sub(r" ",',',ready)
            final=re.sub(r",+", ',',ready)
            proc.write(final)         
        proc.close()
with open('run_04_energy.xvg') as raw:
    with open('run_04_energy_proc.csv','wt') as proc:
        count = 0
        for line in raw:
            full = line
            ready = full.strip()
            ready = ready+"\n"
            ready=re.sub(r" ",',',ready)
            final=re.sub(r",+", ',',ready)
            proc.write(final)         
        proc.close()
with open('run_05_energy.xvg') as raw:
    with open('run_05_energy_proc.csv','wt') as proc:
        count = 0
        for line in raw:
            full = line
            ready = full.strip()
            ready = ready+"\n"
            ready=re.sub(r" ",',',ready)
            final=re.sub(r",+", ',',ready)
            proc.write(final)         
        proc.close()
with open('run_06_energy.xvg') as raw:
    with open('run_06_energy_proc.csv','wt') as proc:
        count = 0
        for line in raw:
            full = line
            ready = full.strip()
            ready = ready+"\n"
            ready=re.sub(r" ",',',ready)
            final=re.sub(r",+", ',',ready)
            proc.write(final)         
        proc.close()
with open('run_07_energy.xvg') as raw:
    with open('run_07_energy_proc.csv','wt') as proc:
        count = 0
        for line in raw:
            full = line
            ready = full.strip()
            ready = ready+"\n"
            ready=re.sub(r" ",',',ready)
            final=re.sub(r",+", ',',ready)
            proc.write(final)         
        proc.close()
with open('run_08_energy.xvg') as raw:
    with open('run_08_energy_proc.csv','wt') as proc:
        count = 0
        for line in raw:
            full = line
            ready = full.strip()
            ready = ready+"\n"
            ready=re.sub(r" ",',',ready)
            final=re.sub(r",+", ',',ready)
            proc.write(final)         
        proc.close()
with open('run_09_energy.xvg') as raw:
    with open('run_09_energy_proc.csv','wt') as proc:
        count = 0
        for line in raw:
            full = line
            ready = full.strip()
            ready = ready+"\n"
            ready=re.sub(r" ",',',ready)
            final=re.sub(r",+", ',',ready)
            proc.write(final)         
        proc.close()
with open('run_10_energy.xvg') as raw:
    with open('run_10_energy_proc.csv','wt') as proc:
        count = 0
        for line in raw:
            full = line
            ready = full.strip()
            ready = ready+"\n"
            ready=re.sub(r" ",',',ready)
            final=re.sub(r",+", ',',ready)
            proc.write(final)         
        proc.close()
with open('nvt_energy.xvg') as raw:
    with open('nvt_energy_proc.csv','wt') as proc:
        count = 0
        for line in raw:
            full = line
            ready = full.strip()
            ready = ready+"\n"
            ready=re.sub(r" ",',',ready)
            final=re.sub(r",+", ',',ready)
            proc.write(final)         
        proc.close()
with open('npt_energy.xvg') as raw:
    with open('npt_energy_proc.csv','wt') as proc:
        count = 0
        for line in raw:
            full = line
            ready = full.strip()
            ready = ready+"\n"
            ready=re.sub(r" ",',',ready)
            final=re.sub(r",+", ',',ready)
            proc.write(final)         
        proc.close()
with open('npt_extension_energy.xvg') as raw:
    with open('npt_extension_proc.csv','wt') as proc:
        count = 0
        for line in raw:
            full = line
            ready = full.strip()
            ready = ready+"\n"
            ready=re.sub(r" ",',',ready)
            final=re.sub(r",+", ',',ready)
            proc.write(final)         
        proc.close()
        
    
