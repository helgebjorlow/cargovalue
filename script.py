import pandas as pd
from pandas.io.json import json_normalize
import json
import os



def flatten_json(nested_json):
    """
        Flatten json object with nested keys into a single level.
        Args:
            nested_json: A nested json object.
        Returns:
            The flattened json object if successful, None otherwise.
    """
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + ' ')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + ' ')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(nested_json)
    return out

basepath = os.getcwd() + '/Blue Energy/18/'
keylist = []
with open(basepath + os.listdir(basepath)[0]) as f:
    sample = json.load(f)
sample = flatten_json(sample)
for key in sample.keys():
    keylist.append(key)
print(keylist[6])



# this finds our json files
path_to_json = os.getcwd() + '/Blue Energy/18/'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]

# here I define my pandas Dataframe with the columns I want to get from the json
jsons_data = pd.DataFrame(columns=keylist)
jsons_data.to_csv('out.csv', encoding='utf-8', index=False)
dataframe = ''
# we need both the json and an index number so use enumerate()
for index, js in enumerate(json_files):
    with open(os.path.join(path_to_json, js)) as json_file:
        json_text = flatten_json(json.load(json_file))
        # here you need to know the layout of your json and each json has to have
        # the same structure 
        # here I push a list of data into a pandas DataFrame at row given by 'index'
        for attr_num in range(len(json_text)):
            if keylist[attr_num] in json_text:
                jsons_data.loc[index] = json_text[keylist[index]]

jsons_data.to_csv('out.csv', encoding='utf-8', index=False)
# now that we have the pertinent json data in our DataFrame let's look at it







