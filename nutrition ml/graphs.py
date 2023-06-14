import pandas 
import os
import inspect
import matplotlib.pyplot as plt
current_file_path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
os.chdir(current_file_path)
columns_to_read=["name "]
data=pandas.read_csv("dataset.csv",usecols=columns_to_read,sep=",")
column_names = data.columns.tolist()
print(type(data))

