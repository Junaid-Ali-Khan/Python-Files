# API result confirmation
""" import requests,json
import pandas as pd 

lat = "24.798316"
lon = "67.053109"

params = { 
    'format' : 'jsonv2',
    'lat' : lat ,
    'lon' : lon
}

r = requests.get('https://beta-geocoder-2057693861.eu-west-1.elb.amazonaws.com/nominatim/reverse', params=params , verify=False)
j = json.loads(r.text)
# df = pd.DataFrame(j['routes'])
# output = df[['duration' , 'distance']]
print(j)
# parameter.append(params)
# print(output )
# NB.append(output)  
"""

# Multithreading Function For Calling NB API #
import requests
import json
import pandas as pd
import pprint
import concurrent.futures as confu
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def request(i, obj):
    try:

        obj = {
            # 'place_id' : '',
            # 'osm_type' : '',
            # 'osm_id' : '',
            'Google Address' : BQ_data.loc[i, 'address'], 
            'lat' : BQ_data.loc[i, 'lat'],
            'lon': BQ_data.loc[i, 'lon'],
            'Address' : {},    
            # 'place_rank' : '',
            # 'category' : '' ,
            # 'type' : '',
            'display_name' : ''
        }

        params = { 
            'format' : 'jsonv2',
            'lat' : obj['lat'] ,
            'lon' : obj['lon']
        }

        r = requests.get('https://beta-geocoder-2057693861.eu-west-1.elb.amazonaws.com/nominatim/reverse', params=params , verify=False)
        j = json.loads(r.text)

        # obj['place_id']     = j['place_id']    
        # obj['osm_type']     = j['osm_type']      
        # obj['osm_id']       = j['osm_id']      
        obj['lat']           = j['lat']           
        obj['lon']          = j['lon'] 
        # obj['place_rank']   = j['place_rank']   
        obj['category']     = j['category']   
        obj['type']         = j['type']        
        # obj['drop address'] = obj['drop address']
        # obj['Google Address'] = obj['address']
        obj['display_name'] = j['display_name']  
        obj['Address'] = j['address']

        print("iterator" , i) 

    except Exception as e: 
        print('Exception' , e)
    
    return obj

BQ_data = pd.read_csv('/home/junaid/Downloads/Bykea Technologies/NB and Google/ATA_analysis/Geocoding/Testing Folder/LahoreFile2.csv')

Array = []
count=0
pprint.pprint("here")
with confu.ThreadPoolExecutor(100) as executor:
    future = {executor.submit(request,i,BQ_data) for i in range(len(BQ_data))}
    
    for f in confu.as_completed(future):
        try:
            Array.append(f.result())
            # print('result' , f.result())
        except Exception as e:
            print(e)
    
    import numpy as np

    class NpEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, np.integer):
                return int(obj)
            elif isinstance(obj, np.floating):
                return float(obj)
            elif isinstance(obj, np.ndarray):
                return obj.tolist()
            else:
                return super(NpEncoder, self).default(obj)

    with open('/home/junaid/Downloads/Bykea Technologies/NB and Google/ATA_analysis/Geocoding/Testing Folder/LahoreOutput2.json' , 'w' , encoding='utf-8' ) as write:
        json.dump(Array , write  , cls=NpEncoder, indent=4 , ensure_ascii=False )
    
    # print(df.head())
    # print(df.shape)
    # df.to_csv('/home/junaid/Downloads/Bykea Technologies/NB and Google/ATA_analysis/Geocoding/Lahore/khiOutput.csv')

""" import pandas as pd 

df = pd.read_csv('/home/junaid/Downloads/Bykea Technologies/NB and Google/ATA_analysis/Geocoding/Lahore/rwpOutputFile.csv')
df2 = pd.read_csv('/home/junaid/Downloads/Bykea Technologies/NB and Google/ATA_analysis/Geocoding/Lahore/rwpOutputFile2.csv')
# df3 = pd.read_csv('/home/junaid/Downloads/Bykea Technologies/NB and Google/ATA_analysis/Geocoding/Lahore/rwpOutputFile3.csv')
df4 = pd.read_csv('/home/junaid/Downloads/Bykea Technologies/NB and Google/ATA_analysis/Geocoding/Lahore/rwpOutputFile4.csv')
df5 = pd.read_csv('/home/junaid/Downloads/Bykea Technologies/NB and Google/ATA_analysis/Geocoding/Lahore/rwpOutputFile5.csv')
df6 = pd.read_csv('/home/junaid/Downloads/Bykea Technologies/NB and Google/ATA_analysis/Geocoding/Lahore/rwpOutputFile6.csv')
df7 = pd.read_csv('/home/junaid/Downloads/Bykea Technologies/NB and Google/ATA_analysis/Geocoding/Lahore/rwpOutputFile7.csv')
df8 = pd.read_csv('/home/junaid/Downloads/Bykea Technologies/NB and Google/ATA_analysis/Geocoding/Lahore/rwpOutputFile8.csv')

concate = pd.concat([df, df2 , df4 , df5, df6, df7, df8])

concate.to_csv('/home/junaid/Downloads/Bykea Technologies/NB and Google/ATA_analysis/Geocoding/Lahore/rwpCombineOutput.csv')
print(concate.shape) """
