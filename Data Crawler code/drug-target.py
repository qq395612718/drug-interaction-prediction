# -*- coding:utf-8 -*-
import  urllib.request
from bs4 import BeautifulSoup
import pymysql

con = pymysql.connect(host='localhost', port = 3306, user='root', passwd='123456', db ='drug_data')
cur=con.cursor()

f=open("drug_url4.txt")
List=[]
for line in f:
    List.append(line)
number=0
for x in List:
    number+=1
    try:
        response=urllib.request.urlopen(x)
        html_doc=response.read()
        soup=BeautifulSoup(html_doc,'html.parser')
        
        drug_type=soup.find('div',class_='card-content px-md-4 px-sm-2 pb-md-4 pb-sm-2').find_all('dt')
        drug_data=soup.find('div',class_='card-content px-md-4 px-sm-2 pb-md-4 pb-sm-2').find_all('dd')
        drug_type_list=[]    
        for i in drug_type:
            drug_type_list.append(i.get_text())
        drug_data_list=[]       
        for i in drug_data:
            drug_data_list.append(i.get_text())
        drug=dict(zip(drug_type_list,drug_data_list))    
        
        drug_target=soup.find('div',class_='bond-list-container targets').find_all('strong')
        drug_actions=soup.find('div',class_='bond-list-container targets').find_all('dt')
        drug_actions_data=soup.find('div',class_='bond-list-container targets').find_all('dd')
        
        drug_name_list=[]
        drug_target_list=[]
        drug_actions_list=[]
        
        q=0
        while(q<len(drug_target)):   
            drug_name_list.append(drug.get('Name'))
            q+=1
            
        for k in drug_target:    
            drug_target_list.append(k.find('a').get_text())
            
        for i,m in enumerate(drug_actions):  
            if m.text=="Actions":
                num=i
                for j,n in enumerate(drug_actions_data):
                    if j==num:
                        drug_actions_list.append(n.text)
                            
        List=list(zip(drug_name_list,drug_target_list,drug_actions_list))   
        for i in List:
            try:
                cur.execute('INSERT INTO drug_target(drug,target,action) values( %s, %s, %s)', i)  
                print("yes")
            except Exception as e:    
                print("no")
        print('success')
    except Exception as e:    
        print("fail")
    print(number)
con.commit()
cur.close()
con.close()








