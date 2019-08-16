# Run task summary module

# import system libraries
import datetime
import os
import traceback
import json

# import Modules
from Lib import Module_TaskSummary

# Read json config
with open("Config.json") as json_data_file:
    data=json.load(json_data_file)

# Variable assignment
Tasks_folder_path=data["Tasks_folder_path"]
group_column=data["group_column"]
status_column=data["status_column"]
missing_data_path=data["missing_data_path"]
task_summary_path=data["task_summary_path"]

if not os.path.exists("Output"):
    os.mkdir("Output")

try:
    # check output tasks folder path is exists
    if not os.path.exists(Tasks_folder_path):
        raise Exception(Tasks_folder_path, "tasks folder path does not exist, please check tasks dataset in output folder")

    # get names of the tasks files
    file_names=Module_TaskSummary.read_filenames(Tasks_folder_path)
    print(file_names)
    
    # get consolidated tasks in dataframe
    consolidate_tasks=Module_TaskSummary.consolidate_tasks(Tasks_folder_path,file_names)
    print(consolidate_tasks)
    
    # output the missing task status of each departments
    Module_TaskSummary.missing_task_status(consolidate_tasks,
                                            missing_data_path,
                                            group_column,
                                            status_column)
    
    # output the task summary of each department and save graph image
    Module_TaskSummary.task_summary(consolidate_tasks,
                                    task_summary_path,
                                    group_column,
                                    status_column)

except Exception as e:
    if not os.path.isfile("ErrorLog.txt"):
        open("ErrorLog.txt","x")
    with open("ErrorLog.txt","a") as log:
        log.write(str(datetime.datetime.now())+"-"+str(e)+"\n")
        log.write(str(traceback.format_exc())+"\n")
        log.write("---------------------------------\n")
