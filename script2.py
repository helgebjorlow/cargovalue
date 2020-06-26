import pandas as pd
import json
import os
import time
import array
import csv
start_time = time.time()

#function that recursively flattens json-data by calling a helper function(flatten) on each level of the json it encounters

def flatten_json(json_nested):  
    flat_json = {}

    def flatten(unflat, text=''):
        
        if type(unflat) is dict:
            for element in unflat:
                flatten(unflat[element], text + element + '_')
        
        elif type(unflat) is list:
            
            for element in unflat:
                flatten(element, text + '_')
                
        else: 
            
            flat_json[text] = unflat
    flatten(json_nested)
    return flat_json



path_to_json = os.getcwd() + '/Blue Energy/18/'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]

recordList = []
for index, js in enumerate(json_files):
    with open(os.path.join(path_to_json, js)) as json_file:
        json_text = flatten_json(json.load(json_file))
        recordList.append(json_text)


dictionary = {}
for record in recordList:
    dictionary.update(record)
keyList = [*dictionary.keys()]

rows, cols = (len(recordList), len(keyList))
arr = [[0]*cols]*rows
arr[0] = keyList
for record in recordList:
    i=1
    for key in range(len(keyList)):
        try:
            arr[i][key] = recordList[i][keyList[key]]
        except KeyError:
            arr[i][key] = ''
    i+=1



with open("out2.csv","w+") as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=',')
    csvWriter.writerows(arr)








#recordList_dict = Convert(recordList)
#
#print(type(recordList_dict))
#keyList = []
#for key, value in recordList_dict:
#    if recordList_dict[key] not in keyList:
#        keyList.append(recordList_dict[key])




df = pd.DataFrame(recordList)
export = df.to_csv('out.csv')

print("Process finished --- %s seconds ---" % (time.time() - start_time))

