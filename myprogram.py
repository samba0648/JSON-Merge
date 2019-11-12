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

folder_path = input("Enter Folder path: ")
file_basename = input("Enter File Base Name: ")
output_file_name = input("Enter Output file base name: ")
try:
    max_file_size = int(input("Enter Max file size in Bytes:"))
    #Reading all the json files starts with given base file name and in the given folder
    all_files = all_folder(folder_path,file_basename)
    final = dict()
    #Reading all files data objects and adding them to a dictionary
    for file in all_files:
        new_list = list()
        #opening and reading the file
        with open(file,"r")as f:
            data = json.load(f)
        for j in data:
            if j in final.keys():
                value = data[j]
                li = final[j]
                for ele in value:
                    li.append(ele)
                final[j]=li

            else:
                for ele in data[j]:
                    new_list.append(ele)
                final[j] = new_list
    
    #writing the dictionary values into json files
    count = 1
    for j in final.items():
        di = dict()
        di[j[0]] = j[1]
        try:
            file = output_file_name+str(count)+".json"
            with open(file,"w") as output_file:
                json.dump(di,output_file,indent = 2,separators=(",",":"))
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


