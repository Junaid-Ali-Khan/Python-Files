import pandas as pd 
# import requests
# import concurrent.futures as confu
import math




def calculate_distance(lat1, lon1 , lat2, lon2):

    try:
        delta = lon2 - lon1
        a = math.radians(lat1)
        b = math.radians(lat2)
        C = math.radians(delta)
        x = math.sin(a) * math.sin(b) + math.cos(a) * math.cos(b) * math.cos(C)
        distance = math.acos(x) # in radians
        distance  = math.degrees(distance) # in degrees
        distance  = distance * 60 # 60 nautical miles / lat degree
        distance = distance * 1852 / 1000 # conversion to meters
        distance  = round(distance,3)
        return distance
    except:
        return 0



lat1 = 24.867021478552957
lon1 = 67.01435018330811	
lat2 = 24.842584585498766
lon2 = 67.020900137722492

result = calculate_distance(lat1, lon1 , lat2, lon2)
print(result)

""" df = pd.read_csv('/home/junaid/Downloads/Bykea Technologies/NB and Google/ATA_analysis/production_poi.csv')

Array = []
for b in range(len(df)):
    lat1 = df.loc[b,'Latitude']
    lon1 = df.loc[b,'Longitude']
    for a in range(len(df)):
        lat2 = df.loc[a,'Latitude']
        lon2 = df.loc[a,'Longitude']
        result = calculate_distance(lat1, lon1 , lat2, lon2)
        if result < 10:
            obj = {
                'Ref Lat' : lat1,
                'Ref Lng' : lon1,
                'Ref Name' : df.loc[b,'Names'],
                'Ref Poi Address' : df.loc[b,'Poi Address'],
                'Ref Actual Address' : df.loc[b, 'Actual_Address'],
                'Name' : df.loc[a,'Names'],
                'Poi Address' : df.loc[a,'Poi Address'],
                'Actual Address' : df.loc[a, 'Actual_Address'],
                'Distance' : result
            }
            Array.append(obj)
            print('no of turns' , a)
        else:
            pass

    print(b , 'iterator')

output = pd.DataFrame(Array)
output.to_csv('/home/junaid/Downloads/Bykea Technologies/NB and Google/ATA_analysis/poiOutput.csv')

df = pd.read_csv('/home/junaid/Downloads/Bykea Technologies/NB and Google/ATA_analysis/poiOutput.csv')

df.groupby(['Names' , ''])
 """