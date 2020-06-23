import pandas as pd
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


path_to_json = os.getcwd() + '/Blue Energy/18/'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]


recordList = []
for index, js in enumerate(json_files):
    with open(os.path.join(path_to_json, js)) as json_file:
        json_text = flatten_json(json.load(json_file))
        recordList.append(json_text)


df = pd.DataFrame(recordList)
export = df.to_csv('out.csv')



