import csv

with open('123.txt','w') as f:
    csv_reader=csv.reader(open('0-0.05.csv',encoding='utf-8'))
    num=0
    for line in csv_reader:
        f.write('<owl:NamedIndividual rdf:about="http://www.owl-ontologies.com/drug_action.owl#%s">'%line[0]+'\n')
        f.write('    <rdf:type rdf:resource="http://www.owl-ontologies.com/drug_action.owl#Drug"/>'+'\n')
        f.write('    <Similar rdf:resource="http://www.owl-ontologies.com/drug_action.owl#%s"/>'%line[1]+'\n')
        f.write('</owl:NamedIndividual>'+'\n')
        num+=1
        print(num)
        
