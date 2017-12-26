    "Data Crawler code" is used to crawl the data from DrugBank,which including 4 python files to 
crawl differnt types of data and 5 txt files contain related drugs url.Finaly,we can get the raw 
data！！drug.csv,drug_enzyme.csv,drug_interaction_drug.csv,drug_target.csv,drug_transporter.csv

    "Drug similarity calculation and Separation interval" contains drug similarity calculation code
that is drug_similarity.py and drug_similarity separation intervals.

    "ontology construction code" is used to convert csv to owl��and finally we can get "DIO ontology"
, which including 20 owl files and ontology reasoning rules file！！test.rules

    "Jena Reasoning code" is used to infer drug-drug interactions based on similarity and PK mechanism,
which including 4 java files,and finally based on reasoning results and drug_interaction_drug.csv,we can 
calculate the accuracy and recall rate,Interaction_drug_duplication_deleted.py and Interaction_drug_duplication_deleted2.py
are used to delete deduplication reasoning result data;DDI_predicted_accuracy_num.py is used to calculate
the exact predicted number of DDIs.