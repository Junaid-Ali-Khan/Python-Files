#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import json 
import os , sys
import numpy as np 
from shapely.geometry import shape , Point



with open("/home/junaid/Downloads/Bykea Technologies/liveJson Files/karachi_map/Polygon_Level_1.geojson" , 'r+' ,encoding="utf-8") as polygon , open("/home/junaid/Downloads/Bykea Technologies/liveJson Files/karachi_map/Point_Level_1.geojson" , 'r+' ,encoding="utf-8") as pointLevelOne , open("/home/junaid/Downloads/Bykea Technologies/liveJson Files/karachi_map/Point_Level_2.geojson" , 'r+' ,encoding="utf-8") as pointLevelTwo:
    load = json.load(polygon)
    load2 = json.load(pointLevelOne)
    load3 = json.load(pointLevelTwo)

    Polygon = load['features']
    PointLevelOne = load2['features']
    PointLevelTwo = load3['features']

    obj2 = []
    
    for keys in Polygon:
        oldJson = keys

        obj = {
                "zone" : oldJson['properties']['Name'] ,
                "urdu_text" : oldJson['properties']['name_ur'],
                "city" : oldJson['properties']['City'],
                "zone_order" : int(oldJson['properties']["zone_order"]),
                "loc" : {},
                "polygon" : oldJson["geometry"],
                "areas" :  []
            }

        for key in PointLevelOne:
            pointObjOne = key
            polygon = shape(oldJson['geometry'])
            if polygon.contains(Point(tuple(pointObjOne['geometry']['coordinates']))) == True:  
                obj['loc'] = pointObjOne['geometry']
                pointObject = {
                "urdu" : pointObjOne['properties']['Name'],
                "name" : pointObjOne['properties'][u'name_ur'],
                "loc" : pointObjOne['geometry']['coordinates']
                }

                obj['areas'].append(pointObject)

        for key in PointLevelTwo:
            pointObjTwo = key
            polygon = shape(oldJson['geometry'])
            if polygon.contains(Point(tuple(pointObjTwo['geometry']['coordinates']))) == True:  
                
                pointObject = {
                "urdu" : pointObjTwo['properties']['Name'],
                "name" : pointObjTwo['properties'][u'name_ur'],
                "loc" : pointObjTwo['geometry']['coordinates']
                }

                obj['areas'].append(pointObject)
        
        obj2.append(obj)
        
    print(obj2)
    with open("/home/junaid/Downloads/Bykea Technologies/liveJson Files/khiOutput.json" , 'w' , encoding='utf-8' ) as write:
        json.dump(obj2 , write  , indent=6 , ensure_ascii=False)