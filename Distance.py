# NB API calling function 
""" import requests,json
import pandas as pd 

BQ_data = pd.read_csv('/home/junaid/Downloads/Bykea Technologies/NB and Google/ATA_analysis/ATAtrips.csv')
Array = []

for i in range(len(BQ_data)):
 
    obj = {
    "Trip ID" : BQ_data.loc[i,'_id'],
    "Origin" : BQ_data.loc[i,'Pick_Up'],
    "Destination" : BQ_data.loc[i,'Drop_Off'],
    "Actual Distance" : BQ_data.loc[i,'Actual_distance'],
    "Actual Time" : BQ_data.loc[i,'Actual_time'],
    "Estimated Distance" : BQ_data.loc[i,'Estimated_Distance'],
    "Estimated Time" : BQ_data.loc[i,'Estimated_Distance'],
    "NB Distance" : "",
    "NB Time" : ""
    }

    params = { 
        'origin' : obj['Origin'] ,
        'destination' : obj['Destination']
    }

    token = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6Im5iLmFpIn0.eyJleHAiOjE1OTczMTUyNDQuNzMyNjE3NCwiYXVkIjpbImJ5a2VhIl0sImNpZCI6ImJ5a2VhIn0.Z5wHUuK5yyRf6Nf9atioKE_n4tLBloy_aPSXSutB0-5XKu4AEWd2NNCehu8U7j9MP9yf9oRFeo622Fpvkkyj4rB8az_q0MBhd9AAonYDDBj7nOQ-jCeEOxXDJIr-YGSqQ8FUzht_n60ci6BOCspfURVAHhFDAbOvjwYDzW-y8I8GMUC1sxDuhnhSxedwreXK3SRk_Iyn0A62TT5U__p0vANeWhN9nGLpWlf8xMN1wu8U_VGj0pVYKkcz6NH44a7-DxckJo93X0Cw_uQRA4oyGZ9_sQN2f-gFztCbwt7edzGsHzsEVyNv4JQUIDPTfyjsSRW-cSoOc-tRuKbbpTIIkg"

    headers = { 'Authorization' : token }

    r = requests.get('https://bykea.nextbillion.io/directions/json', params=params, headers=headers)
    j = json.loads(r.text)

    if j['status'] == 'Ok':
    
        obj['NB Distance'] = j['routes'][0]['distance']
        obj['NB Time'] = j['routes'][0]['duration'] 
        
        Array.append(obj)
    
    else:
        pass
    
    df = pd.DataFrame(Array)

df.to_csv('/home/junaid/Downloads/Bykea Technologies/manualFile.csv')
 """

# API result confirmation
""" import requests,json
import pandas as pd 

origin = ""
destination = "31.512411904634064,74.284471347928047"
params = { 
    'origin' : origin ,
    'destination' : destination
}
token = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6Im5iLmFpIn0.eyJleHAiOjE1OTczMTUyNDQuNzMyNjE3NCwiYXVkIjpbImJ5a2VhIl0sImNpZCI6ImJ5a2VhIn0.Z5wHUuK5yyRf6Nf9atioKE_n4tLBloy_aPSXSutB0-5XKu4AEWd2NNCehu8U7j9MP9yf9oRFeo622Fpvkkyj4rB8az_q0MBhd9AAonYDDBj7nOQ-jCeEOxXDJIr-YGSqQ8FUzht_n60ci6BOCspfURVAHhFDAbOvjwYDzW-y8I8GMUC1sxDuhnhSxedwreXK3SRk_Iyn0A62TT5U__p0vANeWhN9nGLpWlf8xMN1wu8U_VGj0pVYKkcz6NH44a7-DxckJo93X0Cw_uQRA4oyGZ9_sQN2f-gFztCbwt7edzGsHzsEVyNv4JQUIDPTfyjsSRW-cSoOc-tRuKbbpTIIkg"
headers = { 'Authorization' : token }
r = requests.get('https://bykea.nextbillion.io/directions/json', params=params, headers=headers)
j = json.loads(r.text)
# df = pd.DataFrame(j['routes'])
# output = df[['duration' , 'distance']]
print(j)
# parameter.append(params)
# print(output )
# NB.append(output)  
 """
# Multithreading Function For Calling NB API #
""" import requests
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

BQ_data = pd.read_csv('/home/junaid/Downloads/Bykea Technologies/NB and Google/ATA_analysis/NB Updated API/inputFile3.csv')


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
    df.to_csv('/home/junaid/Downloads/Bykea Technologies/NB and Google/ATA_analysis/NB Updated API/outputFile3.csv')
"""

# Analysis
import pandas as pd 

df = pd.read_csv('/home/junaid/Downloads/Bykea Technologies/NB and Google/ATA_analysis/NB Updated API/outputFile.csv')
df2 = pd.read_csv('/home/junaid/Downloads/Bykea Technologies/NB and Google/ATA_analysis/NB Updated API/outputFile2.csv')
df3 = pd.read_csv('/home/junaid/Downloads/Bykea Technologies/NB and Google/ATA_analysis/NB Updated API/outputFile3.csv')
df4 = pd.read_csv('/home/junaid/Downloads/Bykea Technologies/NB and Google/ATA_analysis/NB Updated API/outputFile4.csv')

frame = pd.concat([df,df2,df3,df4])
print(frame.shape , 'dimensions' , frame.columns)

frame['NB New Distance'] = frame['NB New Distance'] / 1000
frame['NB New Time'] = frame['NB New Time'] / 60

frame['Distance Difference'] = frame['NB Prev Distance'] - frame['NB New Distance'] 
frame['Time Difference'] = frame['NB Prev Time'] - frame['NB New Time']

frame.drop(['Unnamed: 0'], axis=1)

frame.to_csv("/home/junaid/Downloads/Bykea Technologies/NB and Google/ATA_analysis/NB Updated API/combineOutput.csv")

# frame['Distance Difference'] = frame['Distance Difference'].abs()
# frame['Time Difference'] = frame['Time Difference'].abs()

# summary = frame.describe()
# corr = frame.corr()
# print("\t\t ****** Correlation ******\n" , corr.iloc[:,2:8])
# print("\t\t ****** Summary ******\n" , summary.iloc[:,3:10])
