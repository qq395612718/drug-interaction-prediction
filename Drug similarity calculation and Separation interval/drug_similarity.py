# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 14:24:48 2017

@author: dell
"""
import numpy as np
import pandas as pd

with open("456-4.txt","w") as qwe:
    header=['drug_name','target_name','rating']
    df=pd.read_csv('drug_similarity.csv',names=header)
    
    n_drugs = df.drug_name.unique().shape[0]     #Get the drug's unique value
    n_targets = df.target_name.unique().shape[0]     #Get the target's unique value
    #print ('Number of drugs = ' + str(n_drugs) + ' | Number of targets = ' + str(n_targets)) 
    
    from sklearn import cross_validation as cv
    train_data, test_data = cv.train_test_split(df, test_size=0)
    #Create a drug - target matrix
    drug_target_matrix=np.zeros((n_drugs,n_targets))
    for line in train_data.itertuples():
        drug_target_matrix[line[1]-1,line[2]-1]=line[3]
    
    def cos(vector1,vector2):   #Cosine similarity calculation function
        dot_product = 0.0;  
        normA = 0.0;  
        normB = 0.0;  
        for a,b in zip(vector1,vector2):  
            dot_product += a*b  
            normA += a**2  
            normB += b**2  
        if normA == 0.0 or normB==0.0:  
            return None  
        else:  
            return dot_product / ((normA*normB)**0.5)  
          
    drug_similarity_matrix=np.zeros((n_drugs,n_drugs))   #Drug similarity matrix
    for i in range(n_drugs):
        for j in range(n_drugs):
            drug_similarity_matrix[i][j]=cos(drug_target_matrix[i],drug_target_matrix[j])
            print(i,j)
            qwe.write(str(drug_similarity_matrix[i][j])+',')
        qwe.write('\n')
    


