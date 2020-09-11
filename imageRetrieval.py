""" import requests
import json
import pandas as pd
import pprint
import concurrent.futures as confu
import numpy as np
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def request(i, obj):
    
    try:
        # image API parameters
        params = { 
            '_id' : BQ_data.loc[i,'driver_id'] ,
            'img_id' : BQ_data.loc[i,'img_id']
        }

        # License API parameters
        # params = {
        #     'driver_id' : BQ_data.loc[i,'driver_id'], 
        #     'license_expiry' : BQ_data.loc[i,'license_expiry'],
        #     'status' : BQ_data.loc[i,'status']
        #     }

        print(i)
        
        token = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6Im5iLmFpIn0.eyJleHAiOjE2MDYwNDExODAuNDc5NTksImF1ZCI6WyJieWtlYSJdLCJjaWQiOiJieWtlYSJ9.HVBMrjk0GeIn6KjdxIKYkNNtVusMyZbfkozOhzqPYilxfUpiHFGEqrSEDMTgTdNiPeP2TePnL0WnYb_RgHK845dbZEUrhimd920gz5UTjfi-Xez2hUk7QLpOfzXpUHu2FI8ikJJhaUj0LwmlF_Cvh0rPy75d7ok40inA5q9hh42RUHjs91VKdUVH8_i1yBxT_913a6uwm-6AEQtf7Q1hEE862hsOb-2xKkcGmdYbR4LVviAQzhHNNPyPu8EGvMn4549NWoNlKktKp460qodsZnjq_o6q--2Wb2e6Sgd1WnKQdBkuBmADuOlhERLAyx4GhK4NyMXRk7aGL3M1Yp89aw"
    
        headers = { 'Authorization' : token }

        r = requests.get('https://bykea.nextbillion.io/directions/json', params=params, headers=headers)
        result = json.loads(r.text)

        if result['status'] == 'Ok':  

            print("iterator" , i) 

        else:
            pass 
    except Exception as e : 
        print(e)
    
    return result

loc = "drivers.csv"
 """
# Images API request

""" df = pd.read_csv(loc) 

conversion = df['driver'].apply(json.loads).apply(pd.io.json.json_normalize).pipe(lambda x: pd.concat(x.values))
conversion['driver_id'] = df['driver_id']

conversion.to_csv('drivers2.csv')

BQ_data = pd.read_csv('drivers2.csv') """
 

# License API request
# BQ_data = pd.read_excel('license expired_2020.xlsx')

""" Array = []
count=0
pprint.pprint("here")
with confu.ThreadPoolExecutor(100) as executor:
    future = {executor.submit(request,i,BQ_data) for i in range(len(BQ_data))}
    for f in confu.as_completed(future):
        try:
            Array.append(f.result())
        except Exception as e:
            print(e) """

