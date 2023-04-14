# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 09:47:07 2023

@author: almusawiaf
BSON file
"""

import bson
import json
from bson import json_util
# Load the BSON file
with open("Data/measures.bson", "rb") as f:
    bson_data = f.read()

# Decode the BSON data to a Python object
bson_obj = bson.loads(bson_data)

# Serialize the BSON object to a JSON string
json_str = json_util.dumps(bson_obj)

# Save the dictionary to a JSON file
with open("Data/measures.json", "w") as f:
    f.write(json_str)

