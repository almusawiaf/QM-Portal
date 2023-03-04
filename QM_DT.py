# -*- coding: utf-8 -*-
"""
QUALITY MEASURES - DECISION TREES
"""

import csv
import json


DB_lung = ["temp-lung-dvh",
            "washu_measures_lung_all",
            "washu_measures_lung_all_dvh_flag",
            "washu_measures_lung_all_dvh_value"]
DB_prostate = ["temp-prostate-dvh",
                "washu_measures_prostate_all",
                "washu_measures_prostate_all_dvh_flag",
                "washu_measures_prostate_all_dvh_value"]

sample = json.dumps({
                        'test_feature': 'chiefComplaint',
                        'success_features': ['Prostate cancer', 'Lung Cancer'],
                        'fail_features': '',
                        'yes_child': 'Pass',
                        'no_child': 'Exclude'
                    })

#-----------------------------------------------------------------------------

#                       New Implementation
#-----------------------------------------------------------------------------
class DTNode:
    def __init__(self, obj):
        self.test_feature  = obj['feature']
        self.success_features  = obj['success_features']
        self.yes_child  = obj['yes_child']
        self.no_child  = obj['no_child']
        self.next = ''
        

    def description(self):
        print(f'\t Feature = {self.feature}')
        print(f'\t Success Features = {self.success_features}')
        print(f'\t Yes child = {self.yes_child}')
        print(f'\t No child = {self.no_child}')
    
    # def isnotfinal(self):
    #     if self.next in ['pass', 'fail', 'exclude']:
    #         print('--------------final positive node------------')
    #         print(f'{self.name}')
    #         return True
    #     else:
    #         return False




    def processing(self, data):
        
        print('\nProcessing the data...')
        print(f'current feature = {self.test_feature}\nsuccess feature = {self.success_features}')
        r = self.find_feature(data, self.test_feature)
        print(r)
        print()
        if r != None:
            if r in self.success_features:
                return self.yes_child
            else:
                return self.no_child
        else:
            return None
        
        
        
        
    def find_feature(self, obj, feature):
        """
        Recursively search for a feature in a JSON object.
        """
        if isinstance(obj, dict):
            for key, value in obj.items():
                if key == feature:
                    return value
                else:
                    result = self.find_feature(value, feature)
                    if result is not None:
                        return result
        elif isinstance(obj, list):
            for item in obj:
                result = self.find_feature(item, feature)
                if result is not None:
                    return result
        return None


class DT:
    def __init__(self, dt_json, data):
        '''- Read a list of decision tree nodes as json
           - we create a list of DTNodes
           - we iterate through the ids and check...'''
           
        self.current_node = DTNode(dt_json[0])
        self.result = self.current_node.processing(data)
        
        while self.result not in ['pass', 'fail', 'exclude']:
            
            self.current_node = DTNode(self.get_next(self.result, dt_json))
            self.result = self.current_node.processing(data)
            
    def get_next(self, next_node, dt_json):
        '''search for the next item'''
        print('Next node is : ', next_node)
        for node_dict in dt_json:
            if node_dict['feature']==next_node:
                return node_dict




with open('decision_tree1.json', 'r') as f:
    dt2 = json.load(f)

# Open the CSV file for reading
with open(f'Data/{DB_lung[0]}.csv', 'r') as csv_file:
    # Read the CSV data using a DictReader
    csv_reader = csv.DictReader(csv_file)
    # Convert the CSV data to a list of dictionaries
    data = list(csv_reader)

json_data = json.loads(json.dumps(data))

results = {}
for patient in json_data:
    results[patient['vha_id']] = DT( dt2, patient).result
print(results)
        

