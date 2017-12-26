# -*- coding:utf-8 -*-
import  urllib.request
from bs4 import BeautifulSoup
import pymysql

con = pymysql.connect(host='localhost', port = 3306, user='root', passwd='123456', db ='drug_data')
cur=con.cursor()

with open("456-4.txt","w") as qwe:   #Writes a url that did not successfully read data to the 456.txt text
    f=open("456.txt")
    List=[]
    for line in f:
        List.append(line)
    number=0
    for i in List:
        number+=1
        try:
            response=urllib.request.urlopen(i)
            html_doc=response.read()
            soup=BeautifulSoup(html_doc,'html.parser')
            drug_type=soup.find('div',class_='card-content px-md-4 px-sm-2 pb-md-4 pb-sm-2').find_all('dt')
            drug_data=soup.find('div',class_='card-content px-md-4 px-sm-2 pb-md-4 pb-sm-2').find_all('dd')
                        
            drug_type_list=[]     #drugbank data type
            for j in drug_type:
                drug_type_list.append(j.get_text())
            drug_data_list=[]       #drugbank data
            for k in drug_data:
                drug_data_list.append(k.get_text())
            
            drug=dict(zip(drug_type_list,drug_data_list))     #dictionary corresponds to type and data
                
            drug_name=[]
            drug_toxicity=[]
            drug_smiles=[]
            drug_name.append(drug.get('Name'))    #Add drug name attribute
            drug_smiles.append(drug.get('SMILES'))     #Add drug smiles chemical structure properties
            drug_toxicity.append(drug.get('Toxicity'))     #Add drug toxicity properties
            aList=list(zip(drug_name,drug_smiles,drug_toxicity))
            
                
            for m in aList:
                try:
                    cur.execute('INSERT INTO drug_property(name,smiles,toxicity) values( %s, %s, %s)', m)   #写入mysql数据库
                    
                except Exception as e:    
                    qwe.write(i)
                    print("no")
            print('success')
        except Exception as e:
            print('fail')
                
        print(number)

con.commit()
cur.close()
con.close()
