# This file will call Module_Group and complete its tasks

# Import System Libraries
import os
import datetime 
import traceback
import json

# Import Modules
from Lib import Module_Group

#Create output folder if its not exists
if not os.path.exists("Output"):
    os.mkdir("Output")

# Read json config
with open("Config.json") as json_data_file:
    data=json.load(json_data_file)

print(data)

# Variable assignment
input_file_path=data["input_file_path"]
column_name_grouping=data["group_column"]
tasks_folder_path=data["Tasks_folder_path"]

# Calling module

try:
    # check input dataset file path is exists
    if not os.path.isfile(input_file_path):
        raise Exception(input_file_path, "input file does not exist, please check input dataset in Input folder")

    # call splitting_depts module to group and save data sets seperatly
    Module_Group.splitting_depts(input_file_path,column_name_grouping,tasks_folder_path)
    
except Exception as e:
    if not os.path.isfile("ErrorLog.txt"):
        open("ErrorLog.txt","x")
    with open("ErrorLog.txt","a") as log:
        log.write(str(datetime.datetime.now())+"-"+str(e))
        log.write("\n"+str(traceback.format_exc())+"\n")
        log.write("\n--------------------------------------\n")



