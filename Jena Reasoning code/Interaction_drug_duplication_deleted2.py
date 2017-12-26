# -*- coding:utf-8 -*-
import csv

with open("456-4.txt","w") as f:
# Delete duplicate pairs of interacting drug pairs in order to reduce the data dimension
    
    drug_interaction=csv.reader(open('456-4.csv',encoding='utf-8'))
    drug_interaction_list=[]
    for line in drug_interaction:
        drug_interaction_list.append(line)
    
        
    a=len(drug_interaction_list)
    print(a)


    for i in range(a):
        if drug_interaction_list[i][0]==drug_interaction_list[i][1]:
            drug_interaction_list[i]=''
            
    b=len(drug_interaction_list)
    print(b)
    for i in drug_interaction_list:
        f.write(str(i)+'\n')
        
    
    
    
                
            
        
        

    
    
    
    
        




