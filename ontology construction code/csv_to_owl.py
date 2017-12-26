import csv

with open('123.txt','w') as f:
    csv_reader=csv.reader(open('drug_target.csv',encoding='utf-8'))
    num=0
    for line in csv_reader:
        f.write('<rdf:Description rdf:about="http://%s">'%line[0]+'\n')
        f.write('    <s:%s>%s</s:%s>'%(str(line[2]),line[1],line[2])+'\n')
        f.write('</rdf:Description>'+'\n')
        num+=1
        print(num)
  
