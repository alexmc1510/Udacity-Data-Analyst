# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 00:26:39 2016

@author: ahada
"""
import re
import xml.etree.cElementTree as ET
#from collections import defaultdict


osmfile = "data/sample.osm"

def audit_housenumber(invalid_housenumber, housenumber):
    m = re.search(r'\D+', housenumber) #Matches any non-digit character
    if m:
        invalid_housenumber.append(housenumber)
    

def is_housenumber(elem):
    return (elem.attrib['k'] == "addr:housenumber")


def audit(osmfile):
    osm_file = open(osmfile, "r")
    invalid_housenumber = []
    for event, elem in ET.iterparse(osm_file, events=("start",)):

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"): #return all the subtags named "tag" nested within this element
                if is_housenumber(tag):
                    audit_housenumber(invalid_housenumber, tag.attrib['v'])
    osm_file.close()
    return invalid_housenumber
    
invalid_housenumbers = audit(osmfile)