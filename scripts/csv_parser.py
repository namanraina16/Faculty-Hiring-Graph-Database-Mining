e = open("C://Users//naman//Downloads//1400005_datasets//Dataset 3. ComputerScience_edgelist.txt","r")
v = open("C://Users//naman//Downloads//1400005_datasets//Dataset 4. ComputerScience_vertexlist.txt","r")
new = open("C://Users//naman//OneDrive//Desktop//data_task2_vertices.csv","w")
newer = open("C://Users//naman//OneDrive//Desktop//data_task2_edges.csv","w")
final = open("C://Users//naman//.Neo4jDesktop//relate-data//dbmss//dbms-5455d3d8-a9c9-41c9-ab63-3eff4a6427aa//import//main_new_data.csv","w")
u_l,v_l = [],[]
import subprocess,time
data = dict()
final.write("U,Region_u,u_pi,V,Region_v,v_pi,Rank,Gender,Type\n")
s = 0
for  vertices in v.readlines():
    vt_split = vertices.split("\t")
    data[vt_split[0]] = [vt_split[-1].replace('\n',''),vt_split[1],vt_split[-2]]
    dummy = vt_split[0]+","+vt_split[1]+','+vt_split[-1].replace(",","") 
    new.write(dummy)
for edges in e.readlines():
    ed_split = edges.split("\t")
    if (ed_split[0] != ed_split[1]):
        dummy = ed_split[0]+","+ed_split[1]
        newer.write(dummy+"\n")
        if (ed_split[0]!= '# u' and ed_split[1] != 'v'):
            row = (data[ed_split[0]][0]).replace(',','')+","+ (data[ed_split[0]][-1])+","+ str(data[ed_split[0]][1]) + "," + (data[ed_split[1]][0]).replace(",","")+','+ (data[ed_split[1]][-1])+"," + str(data[ed_split[1]][1]) + "," +ed_split[2]+','+ed_split[-1].replace('\n','') 
            #final.write(row+"\n")

            u_inst,v_inst = (data[ed_split[0]][0]).replace(',',''),(data[ed_split[1]][0]).replace(",","")

            if (u_inst not in v_l and v_inst not in u_l): 
                if (u_inst not in u_l):u_l.append(u_inst)
                if (v_inst not in v_l):v_l.append(v_inst)
                row+=","+"Type 1"
            else:
                if  (u_inst in v_l and v_inst not in u_l):
                    v_l.append(v_inst)
                    row+=","+"Type 3"
                elif (u_inst not in v_l and v_inst in u_l):
                    u_l.append(u_inst)
                    row+=","+"Type 3"
                elif(u_inst in v_l and v_inst in u_l):row+=","+"Type 2"
            final.write(row+"\n")
#subprocess.run("EXCEL "+"main_new_data.csv",shell=True)
print("Done Write... "+time.strftime("%Y-%m-%d %H:%M:%S")+"\n")