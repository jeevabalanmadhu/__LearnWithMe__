# Task summary report

# Import System Library
import pandas as pd
import os
from os import walk
from datetime import datetime
import matplotlib.pyplot as plt


# 1. read all tasks file name and assign into lists
def read_filenames(Tasks_folder_path):
    file_names=[]
    for (dirpath, dirnames, filenames) in walk(Tasks_folder_path):
        file_names.extend(filenames)
    return file_names

# 2. consolidate all tasks csv into one dataframe
def consolidate_tasks(Tasks_folder_path,file_names):
    consolidate_tasks=pd.DataFrame()
    for filename in file_names:
        temp_path=Tasks_folder_path+filename
        temp_df=pd.read_csv(temp_path)
        #consolidate_tasks=pd.concat([consolidate_tasks,temp_df])
        consolidate_tasks=consolidate_tasks.append(temp_df)
    return consolidate_tasks
    
# 3. Missing tasks statuses
def missing_task_status(consolidate_tasks,
                         missing_data_path,
                         group_column,
                         status_column):
    #total missing data
    print(consolidate_tasks[status_column].isnull().sum())
        
    group_dept=consolidate_tasks.groupby(group_column)
    
    list_missing_task_status=[]
    for name, group in group_dept:
        temp=(name,group[status_column].isnull().sum())
        list_missing_task_status.append(temp)
    
    # create temp data set of summary of missing data
    temp_df=pd.DataFrame(data=list_missing_task_status,columns=["Dept","MissingTasks"])
        
    # write to excel
    if not os.path.exists(missing_data_path):
        os.mkdir(missing_data_path)
    now=datetime.now()
    temp_df.to_excel(missing_data_path+"MissingTasks - "+now.strftime("%Y%m%d%H%M%S")+".xlsx",index=False)

# 4. Task summary
def task_summary(consolidate_tasks,task_summary_path,group_column,status_column):
    # Missing data handling
    consolidate_tasks[status_column]=consolidate_tasks[status_column].fillna(value="No")
    print("All missing task status are changed to No and now missind task status count: ",consolidate_tasks[status_column].isnull().sum())
    
    # Create task summarry report
    group_dept=consolidate_tasks.groupby([group_column])
    
    task_summary=[]
    
    for name, group in group_dept:
        dept_summary=[]
        dept_summary.append(name)
        status_groups=group.groupby(status_column)
        for status, status_group in status_groups:
            dept_summary.append(len(status_group))
        task_summary.append(dept_summary)
    
    # Create a data frame for task summary
    df_task_summary=pd.DataFrame(task_summary,columns=["Dept","TaskPending","TaskCompleted"])
    
    # Write to excel
    if not os.path.exists(task_summary_path):
        os.mkdir(task_summary_path)
    now=datetime.now()
    df_task_summary.to_excel(task_summary_path+"TaskSummary- "+now.strftime("%Y%m%d%H%M%S")+".xlsx",index=False)
    
    # Create graph for completed and pending tasks
    
    x=df_task_summary[group_column]
    fig, ax=plt.subplots()
    fig.set_size_inches(10,7)
    
    df_task_summary.plot.bar(ax=ax,stacked=True,color=["r","g"])
    ax.set_xticklabels(x)
    ax.set_title("Task Summary")
    ax.legend(loc='upper right')
    plt.tight_layout()
    fig.savefig(task_summary_path+"Summary_graph - "+now.strftime("%Y%m%d%H%M%S")+".png")


    
