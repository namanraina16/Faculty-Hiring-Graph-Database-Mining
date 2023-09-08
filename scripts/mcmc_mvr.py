import numpy as np
import pandas as pd
import math,random,copy,os,datetime,statistics
current_time = datetime.datetime.now()
os.system("cls")
def init():
    mapping,pi = dict(),[]
    pi.append(-1)
    adj_matix = np.diag(np.full(205,-1))
    final = open("C://Users//naman//.Neo4jDesktop//relate-data//dbmss//dbms-fbcbd002-c40a-4e7d-a2f1-c4075d1e1ac4//import//main_new_data.csv","r")
    v = open("C://Users//naman//Downloads//1400005_datasets//Dataset 4. ComputerScience_vertexlist.txt","r")
    ct  = 0
    for vertices in v.readlines():
        if (vertices.split("\t")[-1].replace("\n","") != "institution" and vertices.split("\t")[-1].replace("\n","") != "All others" ):
            mapping[vertices.split("\t")[-1].replace('\n','').replace(",","")] =  vertices.split("\t")[0]
            pi.append(ct+1.00)
            ct+=1.00
    for lines in final.readlines():
        if (lines.split(",")[0] != "U" and lines.split(",")[0] != "All others" ):
            adj_matix[int(mapping[lines.split(",")[0]])-1][int(mapping[lines.split(",")[2]])-1] +=1
    adj_matix[adj_matix == -1] = 0
    return adj_matix,pi,mapping

def calc_total_weight(adj,pi_list):
    total = 0
    for u in range(adj.shape[0]):
        for v in range(adj.shape[1]):
            if (u!=v):
                total += adj[u][v]*math.copysign(1,pi_list[v+1]-pi_list[u+1])
    return total

def mvr_mcmc(max_iters):
    adj,current_pi,map_colleges = init()
    weighted=[]
    pi_all_vals = [[] for i in range(205)]
    current_best = calc_total_weight(adj,current_pi)
    avg_vals = np.zeros(len(current_pi)-1)
    new_pi = copy.deepcopy(current_pi)
    for i in range(max_iters):
        n1,n2 = random.randint(1,205),random.randint(1,205)
        #swap
        new_pi[n1],new_pi[n2] = new_pi[n2],new_pi[n1]
        new_best = calc_total_weight(adj,new_pi)
        if (new_best >= current_best):
            current_best = new_best
            current_pi = copy.deepcopy(new_pi)
        else:
            if np.exp((new_best - current_best)) > np.random.uniform():
                current_pi = copy.deepcopy(new_pi)
                current_best = new_best
            else:
               new_pi[n1],new_pi[n2] = new_pi[n2],new_pi[n1] 
        for j in range(1, len(current_pi)):
            avg_vals[j - 1] += current_pi[j]
            pi_all_vals[j-1].append(current_pi[j])
        avg_vals/=max_iters
        weighted.append(current_best)
        new = 1 + (avg_vals - np.min(avg_vals)) * (205 - 1) / (np.max(avg_vals) - np.min(avg_vals))
    return new,sum(weighted)/len(weighted),map_colleges,pi_all_vals,weighted
pi_l,weighted_total,maps,pi_all_nums,weighted_list = mvr_mcmc(500)
ct = 0
results = open("C://Users//naman//OneDrive//Desktop//task_3_results.csv","w+")
weights = open("C://Users//naman//OneDrive//Desktop//task_3_weights.csv","w+")
results.write("Insitution" + "," + "MVR_MCMC_Rank" + "," + "Uncertainty for Rank\n" )
weights.write("Iteration" + "," + "Total\n")
for j in range(len(weighted_list)):
    weights.write(str(j) + "," + str(weighted_list[j]) + "\n")
for insts in maps.keys():
    std_pi = statistics.stdev(pi_all_nums[ct])
    maps[insts] = [pi_l[ct],std_pi]
    results.write(insts + "," + str(maps[insts][0]) +  "," + str(maps[insts][1]) + "\n" )
    ct+=1
now = datetime.datetime.now()
print(now  - current_time)
results.close()
weights.close()