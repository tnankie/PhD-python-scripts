import re
import os

def run_stats(file_name):
    trial  = []
    output = [["Cluster ID", "Count", "weight"]]
    stats=[0,0.0,0.0,0,0.0,0.0]
    dummy=[40,0,0,69,0,0]
    cluster_id=[stats,stats,stats,stats,stats,stats,stats,stats,stats,stats,\
                stats,stats,stats,stats,stats,stats,stats,stats,stats,stats,stats,\
                stats,stats,stats,stats,stats,stats,stats,stats,stats,stats,stats,\
                stats,stats,stats,stats,stats,stats,stats,stats,stats,stats,stats,\
                stats,stats,stats,stats,stats,stats,stats,stats,stats,stats,stats,\
                stats,stats,stats,stats,stats,stats,stats,stats,stats,stats,stats,\
                stats,stats,stats,stats,stats,stats,stats,stats,stats,stats,stats]
    with open(file_name,'r') as data:
        print("Stats for " + str(file_name))
        count =0
        for line in data:
            if count >0:
                array = re.split(",",line)
                array[0] = int(array[0])
                array[1] = int(array[1])
                array[2] = float(array[2])
                trial.append(array)
            count = count +1
    for clusters in trial:
        clust_num = clusters[1]
        old_count = cluster_id[clust_num][0]
        new_count = old_count + 1
        old_sum = cluster_id[clust_num][1]
        new_sum = old_sum + clusters[2]
        average = new_sum / new_count
        cl_min = cluster_id[clust_num][3]
        cl_max = cluster_id[clust_num][4]
        if cl_min == 0:
            cl_min = clusters[2]
        if clusters[2] < cl_min:
            cl_min = clusters[2]
        if clusters[2] > cl_max:
            cl_max = clusters[2]
        stats = [new_count,new_sum,average,cl_min,cl_max,0] 
        cluster_id[clust_num]=stats
    count = 0
    total_weight = 0
    print("cluster count  weight   average    min    max ")
    for cl_id in cluster_id:
        if cl_id[0] != 0:
            text ="  " + '{:>2}'.format(count) + "  :  " + '{:>3}'.format(cl_id[0]) + " : " \
            + '{:>6.3f}'.format(cl_id[2]*cl_id[0]/len(trial)) + " :" + '{:>7.1f}'.format(cl_id[2]) \
            + " :" + '{:>6.1f}'.format(cl_id[3]) + " :" + '{:>6.1f}'.format(cl_id[4])
            print(text)
            mini_out = [count, cl_id[0], cl_id[2]*cl_id[0]/len(trial)]
            output.append(mini_out)
            total_weight = total_weight + mini_out[2]
        count = count + 1
    print("Total score for " + file_name + " is " + '{:5>2f}'.format(total_weight)+ "\n \n ------------ \n")
    return(output)

store = []
runs = re.compile('cleaned_des_run_[0-1][0-9]_clid.csv')
dir_cont = os.listdir(".")
for hits in dir_cont:
    if runs.search(hits):
        keepies = run_stats(hits)
        store.append(keepies)
for keep in store:
    w_sum = 0
    count = 0 
    for weights in keep:
        if count > 0:
            float_weight = float(weights[2])
            w_sum = w_sum + float_weight
        count = count + 1
    print(w_sum)
    

