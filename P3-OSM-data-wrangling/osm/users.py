# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 10:51:05 2016

@author: ahada
"""

import xml.etree.cElementTree as ET
import pprint

"""
Your task is to explore the data a bit more.
The first task is a fun one - find out how many unique users
have contributed to the map in this particular area!

The function process_map should return a set of unique user IDs ("uid")
"""

def process_map(filename):
    users = set()
    for _, element in ET.iterparse(filename):
        if "uid" in element.attrib:
            users.add(element.get("uid"))
    return users


users = process_map('data/sample.osm')
pprint.pprint(users)
  
