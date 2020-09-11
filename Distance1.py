import requests
import json
import pandas as pd
import pprint
import concurrent.futures as confu


def request(i, obj):
    # print(obj.shape())
    try:

        obj = {
        "Trip ID": BQ_data.loc[i, 'Trip ID'],
        "Origin": BQ_data.loc[i, 'Origin'],
        "Destination": BQ_data.loc[i, 'Destination'],
        "Actual Distance": BQ_data.loc[i, 'Actual Distance'],
        "Actual Time": BQ_data.loc[i, 'Actual Time'],
        "NB Prev Distance": BQ_data.loc[i, 'NB Distance'],
        "NB Prev Time": BQ_data.loc[i, 'NB Time'],
        "NB New Distance" : "",
        "NB New Time" : ""
        }

        params = { 
            'origin' : obj['Origin'] ,
            'destination' : obj['Destination']
        }

        token = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6Im5iLmFpIn0.eyJleHAiOjE2MDYwNDExODAuNDc5NTksImF1ZCI6WyJieWtlYSJdLCJjaWQiOiJieWtlYSJ9.HVBMrjk0GeIn6KjdxIKYkNNtVusMyZbfkozOhzqPYilxfUpiHFGEqrSEDMTgTdNiPeP2TePnL0WnYb_RgHK845dbZEUrhimd920gz5UTjfi-Xez2hUk7QLpOfzXpUHu2FI8ikJJhaUj0LwmlF_Cvh0rPy75d7ok40inA5q9hh42RUHjs91VKdUVH8_i1yBxT_913a6uwm-6AEQtf7Q1hEE862hsOb-2xKkcGmdYbR4LVviAQzhHNNPyPu8EGvMn4549NWoNlKktKp460qodsZnjq_o6q--2Wb2e6Sgd1WnKQdBkuBmADuOlhERLAyx4GhK4NyMXRk7aGL3M1Yp89aw"
    
        headers = { 'Authorization' : token }

        r = requests.get('https://bykea.nextbillion.io/directions/json', params=params, headers=headers)
        j = json.loads(r.text)

        if j['status'] == 'Ok':
        
            obj['NB New Distance'] = j['routes'][0]['distance']
            obj['NB New Time'] = j['routes'][0]['duration']  

            print("iterator" , i) 

        else:
            pass
    except Exception as e : 
        print(e)
    
    return obj

BQ_data = pd.read_csv('/home/junaid/Downloads/Bykea Technologies/NB and Google/ATA_analysis/NB Updated API/inputFile4.csv')


Array = []
count=0
pprint.pprint("here")
with confu.ThreadPoolExecutor(100) as executor:
    future = {executor.submit(request,i,BQ_data) for i in range(len(BQ_data))}
    # data = confu.wait(futures.result(timeout=5))
    # Array.extend(data)
    for f in confu.as_completed(future):
        try:
            Array.append(f.result())
        except Exception as e:
            print(e)

    df = pd.DataFrame(Array) 
    print(df.head())
    print(df.shape)
    df.to_csv('/home/junaid/Downloads/Bykea Technologies/NB and Google/ATA_analysis/NB Updated API/outputFile4.csv')
