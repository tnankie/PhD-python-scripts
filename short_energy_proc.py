import re
import os
with open('run_01_lie.xvg') as raw:
    with open('run_01_lie.csv','wt') as proc:
        count = 0
        for line in raw:
            full = line
            ready = full.strip()
            ready = ready+"\n"
            ready=re.sub(r" ",',',ready)
            final=re.sub(r",+", ',',ready)
            proc.write(final)         
        proc.close()
with open('run_02_lie.xvg') as raw:
    with open('run_02_lie.csv','wt') as proc:
        count = 0
        for line in raw:
            full = line
            ready = full.strip()
            ready = ready+"\n"
            ready=re.sub(r" ",',',ready)
            final=re.sub(r",+", ',',ready)
            proc.write(final)         
        proc.close()
with open('run_03_lie.xvg') as raw:
    with open('run_03_lie.csv','wt') as proc:
        count = 0
        for line in raw:
            full = line
            ready = full.strip()
            ready = ready+"\n"
            ready=re.sub(r" ",',',ready)
            final=re.sub(r",+", ',',ready)
            proc.write(final)         
        proc.close()
with open('run_04_lie.xvg') as raw:
    with open('run_04_lie.csv','wt') as proc:
        count = 0
        for line in raw:
            full = line
            ready = full.strip()
            ready = ready+"\n"
            ready=re.sub(r" ",',',ready)
            final=re.sub(r",+", ',',ready)
            proc.write(final)         
        proc.close()
with open('run_05_lie.xvg') as raw:
    with open('run_05_lie.csv','wt') as proc:
        count = 0
        for line in raw:
            full = line
            ready = full.strip()
            ready = ready+"\n"
            ready=re.sub(r" ",',',ready)
            final=re.sub(r",+", ',',ready)
            proc.write(final)         
        proc.close()
with open('run_06_lie.xvg') as raw:
    with open('run_06_lie.csv','wt') as proc:
        count = 0
        for line in raw:
            full = line
            ready = full.strip()
            ready = ready+"\n"
            ready=re.sub(r" ",',',ready)
            final=re.sub(r",+", ',',ready)
            proc.write(final)         
        proc.close()
with open('run_07_lie.xvg') as raw:
    with open('run_07_lie.csv','wt') as proc:
        count = 0
        for line in raw:
            full = line
            ready = full.strip()
            ready = ready+"\n"
            ready=re.sub(r" ",',',ready)
            final=re.sub(r",+", ',',ready)
            proc.write(final)         
        proc.close()
with open('run_08_lie.xvg') as raw:
    with open('run_08_lie.csv','wt') as proc:
        count = 0
        for line in raw:
            full = line
            ready = full.strip()
            ready = ready+"\n"
            ready=re.sub(r" ",',',ready)
            final=re.sub(r",+", ',',ready)
            proc.write(final)         
        proc.close()
with open('run_09_lie.xvg') as raw:
    with open('run_09_lie.csv','wt') as proc:
        count = 0
        for line in raw:
            full = line
            ready = full.strip()
            ready = ready+"\n"
            ready=re.sub(r" ",',',ready)
            final=re.sub(r",+", ',',ready)
            proc.write(final)         
        proc.close()
with open('run_10_lie.xvg') as raw:
    with open('run_10_lie.csv','wt') as proc:
        count = 0
        for line in raw:
            full = line
            ready = full.strip()
            ready = ready+"\n"
            ready=re.sub(r" ",',',ready)
            final=re.sub(r",+", ',',ready)
            proc.write(final)         
        proc.close()
