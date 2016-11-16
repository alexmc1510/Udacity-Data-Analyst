# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 10:52:54 2016

@author: ahada
"""
import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

osmfile = "data/sample.osm"

street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE) #pulls out or matches the very last word in street name

expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", "Lane", "Road", 
            "Trail", "Parkway", "Commons", "View", "Trace", "Point", "Plaza", "Meadows", "Creek", 
            "Chase", "Canyon", "Bluff", "Way", "Walk", "Terrace", "Run", "Ridge", "Path", "Pass",
            "Loop", "Hollow", "Hill", "Highway", "Crossing", "Cove", "Circle", "Bend"]



def audit_street_type(street_types, street_name):
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group() #Call the group() method of the match object
        if street_type not in expected:
            street_types[street_type].add(street_name)


def is_street_name(elem):
    return (elem.attrib['k'] == "addr:street")


def audit(osmfile):
    osm_file = open(osmfile, "r")
    street_types = defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"): #return all the subtags named "tag" nested within this element
                if is_street_name(tag):
                    audit_street_type(street_types, tag.attrib['v'])
    osm_file.close()
    return street_types
    
austin_st_types = audit(osmfile)
pprint.pprint(dict(austin_st_types)) 

