# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 09:50:18 2016

@author: ahada
"""

"""
Your task is to use the iterative parsing to process the map file and
find out not only what tags are there, but also how many, to get the
feeling on how much of which data you can expect to have in the map.
Fill out the count_tags function. It should return a dictionary with the 
tag name as the key and number of times this tag can be encountered in 
the map as value.

Note that your code will be tested with a different data file than the 'example.osm'
"""
import xml.etree.cElementTree as ET
import pprint

def count_tags(filename):
    tags = {}
    for event, elem in ET.iterparse(filename): #iterable that returns a stream of (event, element) tuples
        tag = elem.tag
        tags[tag] = tags.get(tag, 0) + 1
        
    return tags



tags = count_tags('data/austin_texas.osm')
pprint.pprint(tags)
   

