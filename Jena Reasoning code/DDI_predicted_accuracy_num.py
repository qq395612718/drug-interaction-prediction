# -*- coding:utf-8 -*-
import csv

drug_interaction=csv.reader(open('drug_interaction_drug.csv',encoding='utf-8'))
drug_interaction_predict=csv.reader(open('456-4.csv',encoding='utf-8'))
drug_interaction_list=[]
drug_interaction_predict_list=[]

for line in drug_interaction:
    drug_interaction_list.append(line)
    
for line in drug_interaction_predict:
    drug_interaction_predict_list.append(line)

for i in drug_interaction_list:
    i.sort()

for j in drug_interaction_predict_list:
    j.sort()

num=0
n=0
for line in drug_interaction_predict_list:
    if line in drug_interaction_list:
        num+=1
    n+=1
    print(n)

print(num)
    
