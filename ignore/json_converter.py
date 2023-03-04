import json
d = {}
with open("one.json", "r") as file:
    d = json.load(file)


def search_feature(json_obj, feature_name):
    # Check if the current object is a dictionary
    if isinstance(json_obj, dict):
        # Iterate over the keys and values of the dictionary
        for key, value in json_obj.items():
            # If the key is the feature name, return the value
            if key == feature_name:
                return value
            # If the value is another object, recurse into it
            elif isinstance(value, (dict, list)):
                result = search_feature(value, feature_name)
                if result is not None:
                    return result
    # If the current object is a list, iterate over its items and recurse into them
    elif isinstance(json_obj, list):
        for item in json_obj:
            result = search_feature(item, feature_name)
            if result is not None:
                return result
    # If the current object is not a dictionary or list, return None
    else:
        return None



x = search_feature(d, "pastMedicalHistory")
print(x)