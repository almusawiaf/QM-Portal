# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 21:04:35 2023

@author: Ahmad Al Musawi
"""
# Sample_Node = {
#   "node_name": "root",
#   "test_feature": "X",
#   "success_features": [1,2,3],
#   "fail_features": [4,5,6],
#   "yes_child": {},
#   "no_child": {}
#   }

import json

decision_tree_8_version1 = [
    {
  "node_name": "RT Consult",
  "test_feature": "X",
  "success_features": 'present',
  "fail_features": 'no',
  "yes_child": 'ICD-10',
  "no_child": 'exclude'
  },
    {
    "node_name": "ICD-10",
    "test_feature": "ICD-10",
    "success_features": ["Prostate cancer"],
    "fail_features": [],
    "yes_child": 'Risk level',
    "no_child": 'exclude'
  },
    {
    "node_name": "Risk level",
    "test_feature": "Risk",
    "success_features": ['very low', 'low', 'intermediate'],
    "fail_features": [],
    "yes_child": 'Active Surveillance',
    "no_child": 'fail'
  },
    {
    "node_name": "Active Surveillance",
    "test_feature": "X",
    "success_features": ['documented'],
    "fail_features": ['not documented'],
    "yes_child": 'Doc Date',
    "no_child": 'fail'
  },
    {
    "node_name": "Doc Date",
    "test_feature": "date",
    "success_features": '01/20/2022',
    "fail_features": '',
    "yes_child": 'pass',
    "no_child": 'fail'
  }]


decision_tree_8_version2 = {
  "node_name": "RT Consult",
  "test_feature": "X",
  "success_features": 'present',
  "fail_features": 'no',
  "yes_child": {
      "node_name": "ICD-10",
      "test_feature": "ICD-10",
      "success_features": ["Prostate cancer"],
      "fail_features": [],
      "yes_child": {
            "node_name": "Risk level",
            "test_feature": "Risk",
            "success_features": ['very low', 'low', 'intermediate'],
            "fail_features": [],
            "yes_child": {
                  "node_name": "Active Surveillance",
                  "test_feature": "X",
                  "success_features": ['documented'],
                  "fail_features": ['not documented'],
                  "yes_child": {
                        "node_name": "Doc Date",
                        "test_feature": "date",
                        "success_features": '01/20/2022',
                        "fail_features": '',
                        "yes_child": {
                            "node_name": "Pass",
                            "yes_child": None,
                            "no_child": None   
                        },
                        "no_child": {
                            "node_name": "Fail",
                            "yes_child": None,
                            "no_child": None   
                        }                      
                  },
                  "no_child": {
                            "node_name": "Fail",
                            "yes_child": None,
                            "no_child": None   
                            }    
            },
            "no_child": {
                "node_name": "Execlude",
                "yes_child": None,
                "no_child": None   

            }

      },
      "no_child": {
          "node_name": "Execlude",
          "yes_child": None,
          "no_child": None   
      }
  },
  "no_child": {
    "node_name": "Execlude",
    "yes_child": None,
    "no_child": None   

      }
  }


# Save the decision tree to a JSON file
with open('decision_tree1.json', 'w') as f:
    json.dump(decision_tree_8_version1, f)

with open('decision_tree2.json', 'w') as f:
    json.dump(decision_tree_8_version2, f)


with open('decision_tree1.json', 'r') as f:
    decision_tree = json.load(f)
