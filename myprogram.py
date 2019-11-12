import json
import os
from os import path
import glob

#function for reading all the json files starts with given file name
def all_folder(f_path,f_name):
    try:
        files = [f for f in glob.glob(f_path+f_name+"*.json",recursive = True)]
    except:
        print("folder not exists")
    return files

folder_path = input()
file_basename = input()
output_file_name = input()
try:
    max_file_size = int(input())
    #Reading all the json files starts with given base file name and in the given folder
    all_files = all_folder(folder_path,file_basename)
    final = dict()
    #Reading all files data objects and adding them to a dictionary
    for file in all_files:
        new_list = list()
        #opening and reading the file
        with open(file,"r")as f:
            data = json.load(f)
        obj=list(data.keys())[0]
        if obj in final.keys():
            value = data[obj]
            new_list = final[obj]
            for ele in value:
                new_list.append(ele)
            final[obj]=new_list
        else:
            for ele in data[obj]:
                new_list.append(ele)
            final[obj] = new_list
    
    #writing the dictionary values into json files
    count = 1
    for obj in final.items():
        my_dict = dict()
        my_dict[obj[0]] = obj[1]
        try:
            file = output_file_name+str(count)+".json"
            with open(file,"w") as output_file:
                json.dump(my_dict,output_file,indent = 2)
                count+=1
            #checking the file size of the file with given max file size
            try:
                file_info = os.stat(file)
                if(file_info.st_size>max_file_size):
                    print("file size is too high")
            except:
                print("Error in fetching file size")
        except:
            print("Unable to write the data into output file")
except:
    print("size should be an interger")


