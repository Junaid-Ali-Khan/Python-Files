#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import json 
import os , sys
from shapely.geometry import shape , Point


with open("/home/junaid/Downloads/Bykea Technologies/liveJson Files/map (6).geojson" , 'r+' , encoding="utf-8") as read_file:
    load = json.load(read_file)
    Features = load['features']
    
     
    Polygon = []
    PointLevelOne = []
    PointLevelTwo =  []

    ObjLevelOne = {}
    ObjLevelTwo = {}

    obj2 = []

    for keys in Features:
        
        oldJson = keys

        for key in Features:
            
            if(oldJson['properties']['name'] == key['properties']['name'] and key['geometry']['type'] == 'Polygon'):
                Polygon.append(key)
                # print(key['properties']['name'])
            elif(oldJson['properties']['name'] == key['properties']['name'] and key['geometry']['type'] == 'Point' and key['properties']['Level'] == 1 ):
                PointLevelOne.append(key)
                
            elif(oldJson['properties']['name'] == key['properties']['name'] and key['geometry']['type'] == 'Point' and key['properties']['Level'] == 2 ):
                PointLevelTwo.append(key)       

    
    Polygon = [i for n, i in enumerate(Polygon) if i not in Polygon[:n]]
    PointLevelOne = [i for n, i in enumerate(PointLevelOne) if i not in PointLevelOne[:n]]
    PointLevelTwo = [i for n, i in enumerate(PointLevelTwo) if i not in PointLevelTwo[:n]]


    for keys in Polygon:
        oldJson = keys

        obj = {
                "zone" : oldJson['properties']['name'] ,
                "urdu_text" : oldJson['properties']['Name_ur'],
                "city" : oldJson['properties']['City'],
                "zone_order" : int(oldJson['properties']['zone_order']),
                "loc" : {},
                "polygon" : oldJson["geometry"],
                "areas" :  []
            }

        polygon = shape(oldJson['geometry'])

        for key in PointLevelOne:
            pointObjOne = key
            
            if polygon.contains(Point(tuple(pointObjOne['geometry']['coordinates']))) == True:

                print(pointObjOne , 'level One')
                obj['loc'] = pointObjOne['geometry']
                

                ObjLevelOne = {
                "urdu" : pointObjOne['properties']['Name_ur'],
                "name" : pointObjOne['properties']['name'],
                "loc" : pointObjOne['geometry']['coordinates']
                }

                obj['areas'].append(ObjLevelOne)
        for key in PointLevelTwo:
            pointObjTwo = key
            if polygon.contains(Point(tuple(pointObjTwo['geometry']['coordinates']))) == True:  
                print(pointObjTwo , 'Level Two')
                
                # obj['loc'] = pointObjTwo['geometry']
                
                ObjLevelTwo = {
                "urdu" : pointObjTwo['properties']['Name_ur'],
                "name" : pointObjTwo['properties']['name'],
                "loc" : pointObjTwo['geometry']['coordinates']
                }

                obj['areas'].append(ObjLevelTwo)
        
        obj2.append(obj)
    
    with open("/home/junaid/Downloads/Bykea Technologies/liveJson Files/Zones.json" , 'w' , encoding='utf-8' ) as write:
        json.dump(obj2 , write  , indent=4 , ensure_ascii=False , encoding='utf-8') 