import pandas as pd
import os
import csv
import json


Lung_QMs = ['QualityMeasure1','QualityMeasure10','QualityMeasure11','QualityMeasure12','QualityMeasure13','QualityMeasure14','QualityMeasure15','QualityMeasure15Chemo','QualityMeasure15RT','QualityMeasure15Surgery','QualityMeasure16','QualityMeasure17','QualityMeasure18','QualityMeasure19','QualityMeasure19_color','QualityMeasure2','QualityMeasure20','QualityMeasure21A','QualityMeasure21B','QualityMeasure22','QualityMeasure23','QualityMeasure24','QualityMeasure27','QualityMeasure3','QualityMeasure4','QualityMeasure5','QualityMeasure6','QualityMeasure7','QualityMeasure8A','QualityMeasure8B','QualityMeasure9']
Prostate_QMs = ['QualityMeasure1','QualityMeasure10','QualityMeasure11','QualityMeasure12','QualityMeasure13','QualityMeasure14','QualityMeasure15','QualityMeasure15_color','QualityMeasure16','QualityMeasure17A','QualityMeasure17B','QualityMeasure18','QualityMeasure19','QualityMeasure2','QualityMeasure24','QualityMeasure3','QualityMeasure4','QualityMeasure5','QualityMeasure6','QualityMeasure7','QualityMeasure8','QualityMeasure9']
QMs = [Lung_QMs, Prostate_QMs]


DB_lung = ["temp-lung-dvh",
            "washu_measures_lung_all",
            "washu_measures_lung_all_dvh_flag",
            "washu_measures_lung_all_dvh_value"]
DB_prostate = ["temp-prostate-dvh",
                "washu_measures_prostate_all",
                "washu_measures_prostate_all_dvh_flag",
                "washu_measures_prostate_all_dvh_value"]

files = ['Lung', 'Prostate']

def saving(h):
    '''aim: read features of the tables and save them'''
    file = files[h]
    subfiles = []
    for filename in os.listdir(f'Data/{file}'):
        if filename.endswith('.csv'):
            subfiles.append(filename)
    # read csv file into dataframe
    Data = [pd.read_csv(f'Data/{file}/{f}') for f in subfiles]
    
    features = []
    types = []
    for df in Data:
        for i in df:
            if i not in QMs[h] and i not in features:
                features.append(i)
                types.append(df[i].dtype)
    
    pd.DataFrame({'feature': features, 'type': types}).to_csv(f'Data/{file}/features.csv')
    pd.DataFrame({'QualityMeasures': QMs[h]}).to_csv(f'Data/{file}/QualityMeasures.csv')


def extract_values(data, key):
    values = []
    if isinstance(data, dict):
        for k, v in data.items():
            if k == key:
                values.append(v)
            else:
                values += extract_values(v, key)
    elif isinstance(data, list):
        for item in data:
            values += extract_values(item, key)
    return values


def find_feature(obj, feature):
    """
    Recursively search for a feature in a JSON object.
    """
    
    print(obj)
    _=input('press any key...')
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key == feature:
                return value
            else:
                result = find_feature(value, feature)
                if result is not None:
                    return result
    elif isinstance(obj, list):
        for item in obj:
            my_items = []
            result = find_feature(item, feature)
            if result is not None:
                my_items.append(result)
                # return result
        return my_items
    return None

def date_features(features):
    '''given a set of features, extract list of features 
    that has date word in it'''
    dates = []
    for i in features:
        if 'date' in i.lower():
            dates.append(i)
    return dates


def extract_features(data):
    '''return all features of the given data.json'''
    features = []
    if isinstance(data, dict):
        for key, value in data.items():
            features.append(key)
            features += extract_features(value)
    elif isinstance(data, list):
        for item in data:
            features += extract_features(item)
    return sorted(list(set(features)))

            
def last_date(dates):
    # Combine all dates into a single list
    all_dates = []
    for key in dates:
        all_dates.extend(dates[key])
    
    # Pick the most recent date
    if all_dates:
        most_recent_date = max(all_dates)
        first_visit = min(all_dates)
    else:
        # Handle the case when there are no dates
        most_recent_date = None
    return first_visit, most_recent_date
    
    

def survival():
    '''finding those who passed away (1) and those who are alive (0)'''
    with open('Data/data.json', 'r') as f:
        data = json.load(f)
    
    features = extract_features(data)
    dates = date_features(features)
    # print(dates)
    # _=input('press any key...\n')
    patients = [i['caseId'] for i in data]
    
    Dates = {} # all values for all dates in the record of the patient
    for rec in data:
        patientID = rec['caseId']
        results = {}
        for f in dates:
            temp = extract_values(rec, f)
            results[f] = temp
        Dates[patientID] = results
    
    surv= {}
    PID, state, lastVisit, firstVisit = [],[],[],[]
    
    for p in patients:
        f,l = last_date(Dates[p])
        firstVisit.append(f)
        lastVisit.append(l)
        PID.append(p)
        # print(Dates[p])
        # _=input('press any key to contineu...')
        if Dates[p]['dateOfDeath']!=[]:
            state.append(1)
        else:
            state.append(0)
    
    surv['PID'] = PID
    surv['state'] = state
    surv['firstVisit'] = firstVisit
    surv['lastVisit'] = lastVisit
    df = pd.DataFrame(surv)
    df.to_csv('Data/survival.csv', index=False)
    pd.DataFrame({'data': features}).to_csv('Data/features.csv', index=False)
    
    
    
    



















