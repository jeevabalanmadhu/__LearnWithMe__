# Group the data set by department and create csv file for every department

# Import system libraries
import pandas as pd
import os

def splitting_depts(input_file_path,column_name_grouping,tasks_folder_path):
    # get the dataset
    df_tasks=pd.read_csv(input_file_path)
    
    # Grouping the data set and save in a folder
    group_by_dept=df_tasks.groupby(column_name_grouping)
    
    for name, group in group_by_dept:
            if not os.path.exists(tasks_folder_path):
                os.mkdir(tasks_folder_path)
            group.to_csv(tasks_folder_path+name+".csv")