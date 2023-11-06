import json
import pandas as pd

annot_path = r"D:\Partition\PROJECTS\__Personal\utd_task\CV-Task\CV-Task\descriptions.csv"
output_path = r"D:\Partition\PROJECTS\__Personal\utd_task\CV-Task\CV-Task\descriptions.json"


df = pd.read_csv(annot_path)
df.head()

data_dict = {}
for index, row in df.iterrows():
    data_dict[row['file']] = row['description'].strip()

json.dump(data_dict, open(output_path,'w'), indent=4)