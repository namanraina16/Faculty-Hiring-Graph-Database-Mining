import numpy as np
import copy,os,random
#os.system("cls")
institutions = dict()
adj_matrix = np.diag(np.full(205,-1.00))
final = open("C://Users//naman//.Neo4jDesktop//relate-data//dbmss//dbms-fbcbd002-c40a-4e7d-a2f1-c4075d1e1ac4//import//main_new_data.csv","r")
v = open("C://Users//naman//Downloads//1400005_datasets//Dataset 4. ComputerScience_vertexlist.txt","r")
ct  = 0
for vertices in v.readlines():
    if (vertices.split("\t")[-1].replace("\n","") != "institution" and vertices.split("\t")[-1].replace("\n","") != "All others" ):
        institutions[vertices.split("\t")[-1].replace('\n','').replace(",","")] =  vertices.split("\t")[0]
for lines in final.readlines():
    if (lines.split(",")[0] != "U" and lines.split(",")[0] != "All others" ):
        adj_matrix[int(institutions[lines.split(",")[0]])-1][int(institutions[lines.split(",")[2]])-1] +=1
adj_matrix[adj_matrix == -1] = 0

def pagerank(adj_matrix,  epsilon, max_iterations,damping_factor=0.85):
    n = adj_matrix.shape[0]
    adj_matrix = adj_matrix / adj_matrix.sum(axis=0, keepdims=True)  # Normalize the adjacency matrix
    normalized_array_one_over_N = np.ones(n) / n 

    # Initialize PageRank vector
    pagerank_vector = np.ones(n) / n

    for iteration in range(max_iterations):
        new_pagerank_vector = (1 - damping_factor) * normalized_array_one_over_N + damping_factor * np.dot(adj_matrix, pagerank_vector)
        if np.linalg.norm(new_pagerank_vector - pagerank_vector) < epsilon:
            break
        pagerank_vector = new_pagerank_vector
    return pagerank_vector
ranking_scores = pagerank(adj_matrix,1e-10,1000)
ranking = np.argsort(ranking_scores)[::-1]
print(ranking)
write_to_page_rank_data = open("C://Users//naman//OneDrive//Desktop//task_3_page_rank_results.csv","w+")
write_to_page_rank_data.write("Institution"+","+"Rank" + ","+ "Page Rank Score\n")
for insts in institutions.keys():
    write_to_page_rank_data.write(insts + "," + str(np.where(ranking==(int(institutions[insts])-1))[0][0] + 1) + "," + str(ranking_scores[(int(institutions[insts])-1)])+ "\n" )
write_to_page_rank_data.close()
