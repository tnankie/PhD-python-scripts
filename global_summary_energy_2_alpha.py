import re
import os
import sys

file_type_a = re.compile(r'run.*_2_.*energy.*\.csv')
file_type_b = re.compile(r'run.*energy.*_2_.*\.csv')
summary_name = "energy_2_summary.csv"
def summary(target_path):
    job_l = []
    dir_cont = os.listdir(target_path)
    dir_data = []
    for entry in dir_cont:
        if file_type_a.search(entry) or file_type_b.search(entry):
            dir_data.append(entry)
    sorted(dir_data)
    for entry in dir_data:
        print(entry)
        target = os.path.join(target_path, entry)
        print(target)
        with open(target) as run:
            titles = ["time,","coul,","vdw,"]
            run_l = []
            run_l.append(titles)
            for line in run:
                raw_d = line[:-1]
                ele_l = re.split(r",",raw_d)
                run_l.append(ele_l)
            job_l.append(run_l)
    length_run = len(job_l)
    length_time = 0
    count_point = 0
    for points in job_l[:]:
        time = len(job_l[count_point])
        if time > length_time:
            length_time = time
        count_point = count_point + 1
    count_time = 0
    print("runs:",length_run,"\n","Timepoints:",length_time)
    file_name = os.path.join(target_path, summary_name)
    with open(file_name, 'wt') as output:
        while count_time < length_time:
            line =[]
            count_run = 0
            while count_run < length_run:
                if count_run == 0:
                    line = job_l[count_run][count_time]
                else:
                    line.append(job_l[count_run][count_time][1:])
                count_run = count_run + 1
            if count_time == 0:
                line.extend(dir_data)
            raw = str(line)
            ready = raw+"\n"
            ready=re.sub(r"[ ,'\[\]]",',',ready)
            final=re.sub(r",+", ',',ready)
            output.write(final)
            count_time = count_time + 1
        output.close()
        
summary(".")
