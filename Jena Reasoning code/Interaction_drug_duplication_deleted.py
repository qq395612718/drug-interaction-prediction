# -*- coding:utf-8 -*-
import csv

with open("456-4.txt","w") as f:
# Delete duplicate pairs of interacting drug pairs in order to reduce the data dimension
    
    drug_interaction=csv.reader(open('1.csv',encoding='utf-8'))
    drug_interaction_list=[]
    for line in drug_interaction:
        drug_interaction_list.append(line)
    
        
    a=len(drug_interaction_list)
    print(a)

    
    for i in range(a):
        drug_interaction_list[i].sort()

    for i in range(10):
        print(drug_interaction_list[i])
    
    List=[]
    num=1
    for j in drug_interaction_list:
        if not j in List:
            List.append(j)
        print(num)
        num+=1
    
    
    for i in List:
        f.write(i[0]+','+i[1]+'\n')
        
    
    
    
                
            
        
        

    
    
    
    
        




