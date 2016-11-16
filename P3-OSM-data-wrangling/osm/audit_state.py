# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 00:26:39 2016

@author: ahada
"""

import xml.etree.cElementTree as ET
#from collections import defaultdict


osmfile = "data/austin_texas.osm"

def audit_state(state_names, state):
    state_names[state] = state_names.get(state,0) + 1

def is_state(elem):
    return (elem.attrib['k'] == "addr:state")


def audit(osmfile):
    osm_file = open(osmfile, "r")
    state_names = {}
    for event, elem in ET.iterparse(osm_file, events=("start",)):

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"): #return all the subtags named "tag" nested within this element
                if is_state(tag):
                    audit_state(state_names, tag.attrib['v'])
    osm_file.close()
    return state_names
    
state_names = audit(osmfile)

