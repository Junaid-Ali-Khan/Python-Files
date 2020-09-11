import geopandas as gpd
import pandas as pd 
import json 
import matplotlib.pyplot as plt


df = gpd.read_file("/home/junaid/Downloads/Bykea Technologies/liveJson Files/zone_rwp_geojson.json")

geometry_types = df.groupby("Type")

pointFeature = geometry_types.get_group("POINT")
polygonFeature = geometry_types.get_group("POLYGON")

pointLevels = pointFeature.groupby("Level")
polygonLevels = polygonFeature.groupby("Level")

print(pointLevels.head(4) , "pointLevels")

pointLevelOne = pointLevels.get_group(1)
pointLevelTwo = pointLevels.get_group(2)

polygonLevelOne = polygonLevels.get_group(1)
polygonLevelTwo = polygonLevels.get_group(2)

Features = []
Zones = []

# print(type(polygonLevelOne))

# Features.append([pointLevelOne , pointLevelTwo , polygonLevelOne , polygonLevelTwo ])



# for i in Features:
    

""" for i in polygonLevelOne:
    obj = {
            'zone' : ['polygonLevelOne]['properties']
    }
    print(obj , i ,'iterator')

 """


""" polygonGeometry = gpd.sjoin(polygonFeature , pointFeature , how="left", op='contains')
pointGeometry = gpd.sjoin(pointFeature , polygonFeature, how="left" , op='contains')

mergeFeatures = pd.merge( pointGeometry , polygonGeometry , how='outer', left_on=['Zone' , 'Level'], right_on=['Zone','Level'],
          sort=True, suffixes=('_x', '_y'))

features -= mergeFeatures[['' , '' , '' , '']]

file2 = pd.DataFrame(mergeFeatures)

file2.to_json("/home/junaid/Downloads/Bykea Technologies/liveJson Files/mergerGeojsonNew.json" , orient='records' , indent=6 , default_handler=str) """