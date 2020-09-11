import geopandas as gpd 
import json 
import pandas as pd
import matplotlib.pyplot as plt

gdf = gpd.read_file("/home/junaid/Downloads/Bykea Technologies/zone_rwp_geojson.json")
# print(gdf.columns)

levels = gdf.groupby("Level")
geometry_types = gdf.groupby("Type")

# Groups of levels and types
# print(levels.first());
# print(geometry_types.first());

Points = geometry_types.get_group("POINT")
Polygons = geometry_types.get_group("POLYGON")

merge = Polygons.merge(Points , on="Zone" )
print(type(merge), 'merge')
merge.to_json('/home/junaid/Downloads/Bykea Technologies/mergeFeatures.json', orient='records' , indent=4 , default_handler=str)

# print(merge.columns)
# mergeLevel = merge.groupby("Level_x")

# print(mergeLevel.first())
# print(mergeLevel.get_group(2))


#Complete Dataframe 
new_df = merge[['name_x' , 'City_x', 'marker-color_x', 'Zone', 'zone_ur_x', 'zone_ur_y' , 'Level_y',
        'Type_x', 'geometry_x','Type_y', 'geometry_y']]

Properties = new_df.iloc[:,0:7]
polyFeatures = new_df.iloc[:,7:9]
pointFeatures = new_df.iloc[:,9:11]

for key in Properties.keys():
    print(key , 'key')

# List of Objects 
""" print(type(Properties),'properties')
print(Properties.columns)

print(type(Polygons),'Polygons')
print(Polygons.columns)

PropertiesObject = Properties.to_dict()
print(type(PropertiesObject))

PolygonsObject = Polygons.to_dict()
print(type(PolygonsObject))

PointsObject = Points.to_dict()
print(type(PointsObject))

Features = []
Features.append(PropertiesObject)
Features.append(PolygonsObject)
Features.append(PointsObject) """


# for obj in Features:
#     print(obj.name)

# print(type(Features),'Features List')
# with open('/home/junaid/Downloads/Bykea Technologies/jsonFile.json', 'w') as write_file: 
    # json.dump(Features , write_file , indent=4)
# features = list.extend(PropertiesObject ,  , PointsObject)
# print(type(features), 'Features List')

# for key in PointsObject.keys():
#     print(key)
# print(PropertiesObject.columns)



""" print(type(new_df))
new_df.to_json('/home/junaid/Downloads/Bykea Technologies/level2.json', orient='records' , indent=4 , default_handler=str )
print(new_df.columns) """
# new_df.plot()
# plt.show()

""" 
join = gpd.sjoin(Polygons , Points , how="inner", op='contains')
print(join['geometry'])
print(Points['geometry'])
Points.plot()
plt.show()
join.plot()
plt.show()


for k in join.keys():
    print(k, 'keys')

df = pd.DataFrame(join)
print(df.column)
print(join.head(5))
join.to_file('/home/junaid/Downloads/Bykea Technologies/joinFeatures1.json' , driver='GeoJSON')

with open('/home/junaid/Downloads/Bykea Technologies/joinFeatures1.json', 'r') as read_file, open('/home/junaid/Downloads/Bykea Technologies/indentFeatures.json', 'w') as write_file:
    jsonFile = json.load(read_file)
    json.dump(jsonFile, write_file ,  indent=4)
with open( "/home/junaid/Downloads/Bykea Technologies/live_jsonfeatures.json" , 'r') as read_file , open( "/home/junaid/Downloads/Bykea Technologies/live_json.json", "w+") as write_file:
    jsonfile = json.load(read_file)
    # json.dump(jsonfile , write_file ,  indent=4) 
    print(type(jsonfile))
    for key, value in jsonfile.items():
        if key == "features":
            features = jsonfile[key]
            for features in features:
                for key in list(features.keys()):
                    if key == "type":
                        del features[key]
                    json.dump(features , write_file ,  indent=4)
    print("Success")






print(join.columns)
print(join[['Zone_left', 'Type_left' , 'Type_right' , 'index_right']])

join.plot(column='fill_right')
plt.show()
print(join[['geometry','Type_left','Type_right']])
print(append.columns)
print(json.dumps(append) , Indent=4)
print(type(append))
print(append.columns)
print(append.head(5))
append.plot()
plt.show()

print(levels.first())
print(geometry_types.first())



print(append.columns)
print(append[['name_x' , 'City_x' , 'geometry_x' , 'geometry_y']])
table= append[['name_x' , 'City_x' , 'geometry_x' , 'geometry_y']]
table.plot(column="Level_left")
plt.show()

with open("/home/junaid/Downloads/Bykea Technologies/live_jsonfeatures.json", "r+") as write_file:
    table2 = json.load(write_file)
    jsonFile = json.dumps(table2 , indent=4)

gdf.plot(column='fill' , cmap='OrRd' , scheme='quantiles')
plt.show()



 """