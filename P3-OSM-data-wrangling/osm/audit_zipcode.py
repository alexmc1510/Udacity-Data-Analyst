# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 16:30:53 2016

@author: ahada
"""

import xml.etree.cElementTree as ET
#from collections import defaultdict


osmfile = "data/sample.osm"

def audit_zipcode(invalid_zipcodes, zipcode):
    first_two_digit = zipcode[:2]
    if len(zipcode)!= 5:
        invalid_zipcodes.append(zipcode)
    elif first_two_digit not in ['78', '76']:
        invalid_zipcodes.append(zipcode)
    elif not zipcode.isdigit():
        invalid_zipcodes.append(zipcode)
    

def is_zipcode(elem):
    return (elem.attrib['k'] == "addr:postcode")


def audit(osmfile):
    osm_file = open(osmfile, "r")
    invalid_zipcodes = []
    for event, elem in ET.iterparse(osm_file, events=("start",)):

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"): #return all the subtags named "tag" nested within this element
                if is_zipcode(tag):
                    audit_zipcode(invalid_zipcodes, tag.attrib['v'])
    osm_file.close()
    return invalid_zipcodes
    
invalid_zipcodes = audit(osmfile)