# JSON-Merge Using Python3
Algorithm:
I have read the all the inputs(folder path,file base name,output file base name,max file size)
I get the all the .json files uisng all_folder method and stored them.
Initialze variable final_dict(to store the final resultant json object)
Now I have read the data from the .json file one by one and stored them in data variable(type - dictionary) 
From the data I'm searching for object name and check whether it is exists in my final_dict dictionary or not.
		a)If exists then take the records from the data and append them to the key.
		b)If not then take the records from the data and stored them in dictionary with object name as key.
Now write the each item of dictionary into one output file.
Checking the outpur file size with the given max file size.
