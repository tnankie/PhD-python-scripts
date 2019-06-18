import re
import os
import sys
##animals = ['pig', 'cow', 'bat']
##birds = ['seagull', 'rooster', 'wren']
##creatures = [animals, birds]
##print(len(creatures), len(animals), len(birds))
##print(animals[1])
##print(creatures[0] [1])


##print(os.listdir('..'))
def print_dir(dir_path):
    for name in os.listdir(dir_path):
        print(os.path.join(dir_path, name))
##print_dir(".")

def print_tree(dir_path):
    for name in os.listdir(dir_path):
        full_path = os.path.join(dir_path, name)
        print(full_path)
        if os.path.isdir(full_path):
            print_tree(full_path)


##print_tree(sys.path[0])    //probably wrong/wouldn't work has slashes in both directions
def csv_build(target_path):
    print(os.getcwd())
    current_dir_contents = os.listdir(target_path)
    current_dir_files = []
    current_dir_data = []
    for entry in current_dir_contents:
        if os.path.isfile(entry):
            current_dir_files.append(entry)
    data_check = re.compile(r'run_2_.*\.xvg')
    for entry in current_dir_files:
        if data_check.search(entry):
            current_dir_data.append(entry)
    ##print(current_dir_contents)
    ##print("new line :)")
    ##print(current_dir_files)
    ##print("another new line :)")
    ##print(current_dir_data)
    my_names = []
    for entry in current_dir_data:
        my_names.append(os.path.splitext(entry)[0])
    ##print(my_names[6])
    for entry in my_names:
        xvg = target_path+entry+".xvg"
        csv = target_path+entry+".csv"
        print("xvg is ", xvg, " Csv is ", csv)
##        with open(xvg) as raw:
##            with open(csv,'wt') as proc:
##                count = 0
##                for line in raw:
##                    full = line
##                    ready = full.strip()
##                    ready = ready+"\n"
##                    ready=re.sub(r" ",',',ready)
##                    final=re.sub(r",+", ',',ready)
##                    proc.write(final)         
##                proc.close()
current_dir_contents = os.listdir(os.getcwd())
current_dir_dir = []
for entry in current_dir_contents:
    if os.path.isdir(entry):
        target = os.path.join(os.getcwd(),entry)
        csv_build(target)
        
        
        

