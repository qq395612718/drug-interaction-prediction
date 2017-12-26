# -*- coding:utf-8 -*-
import  urllib.request
from bs4 import BeautifulSoup
import re
import pymysql

con = pymysql.connect(host='localhost', port = 3306, user='root', passwd='123456', db ='drug_data')
cur=con.cursor()
f=open("drug_url4-3.txt")
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
                        
            
            
            
        drug_interaction=soup.find('table',id='drug-interactions').find_all('a',href=re.compile('/drugs'))
        drug_interaction_drug=[]
        for x in drug_interaction:
            drug_interaction_drug.append(x.get_text())  #Add all interacting drugs to the drug_interaction_drug list
        
        
        drug_name=[]
        p=0
        while(p<len(drug_interaction_drug)):         #Create a list of 'len' drug names for correspondence
            drug_name.append(drug.get('Name'))
            p+=1
        
        aList=list(zip(drug_name,drug_interaction_drug))
        
        
                
                    
        for m in aList:
            try:
                cur.execute('INSERT INTO drug_interaction_drug(drug,drug_interaction) values( %s, %s)', m)   #写入mysql数据库
                
            except Exception as e:    
                
                print("no")
        print('success')
    except Exception as e:    
        print("fail")
                
    print(number)

con.commit()
cur.close()
con.close()