# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 12:59:27 2016

@author: ahada
"""

"""
Your task in this exercise has two steps:

- audit the OSMFILE and change the variable 'mapping' to reflect the changes needed to fix 
    the unexpected street types to the appropriate ones in the expected list.
    You have to add mappings only for the actual problems you find in this OSMFILE,
    not a generalized solution, since that may and will depend on the particular area you are auditing.
- write the update_name function, to actually fix the street name.
    The function takes a string with street name as an argument and should return the fixed name
    We have provided a simple test so that you see what exactly is expected
"""
import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

osmfile = "data/austin_texas.osm"

street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE) #pulls out or matches the very last word in street name

expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", "Lane", "Road", 
            "Trail", "Parkway", "Commons", "View", "Trace", "Point", "Plaza", "Meadows", "Creek", 
            "Chase", "Canyon", "Bluff", "Way", "Walk", "Terrace", "Run", "Ridge", "Path", "Pass",
            "Loop", "Hollow", "Hill", "Highway", "Crossing", "Cove", "Circle", "Bend"]


# UPDATE THIS VARIABLE
mapping = {"N":"North",
           "N.":"North",
           "E":"East",
           "E.":"East",
           "W":"West",
           "W.":"West",
           "S":"South",
           "S.":"South",
           "I":"Interstate",
           "H":"Highway",
           "IH":"Interstate Highway",
           "I35": "Interstate 35",
           "I-35": "Interstate 35",
           "IH35": "Interstate Highway 35",
           "IH-35": "Interstate Highway 35",
           "Ave":"Avenue",
           "Ave.":"Avenue",
           "Bldg.":"Building",
           "Blvd":"Boulevard",
            "Blvd.":"Boulevard",
            "Ct":"Court",
           "Cv":"Cove",
           "Dr":"Drive",
           "Dr.":"Drive",
           "Drive/Rd":"Drive",
           "Hwy":"Highway",
           "HWY":"Highway",
           "Ln":"Lane",
           "Pkwy":"Parkway",
          "Rd":"Road",
          "Rd.":"Road",
           "st": "Street",
           "St": "Street",
            "St.": "Street",
            "Ste.":"Suit",
            "Ste":"Suit",
            "ste":"Suit",
            "ste.":"Suit",
            "street":"Street",
            "suite":"Suite",
          "Tr":"Trail",
          "Trl":"Trail",
          "U.S.":"US"}


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
    
def update(name, mapping):
    words = name.split()
    for w in range(len(words)):
        if words[w] in mapping:
            if words[w-1].lower() not in ['suite', 'ste.', 'ste', 'avenue', 'ave']: # For example, don't update 'Suite E' to 'Suite East'
                words[w] = mapping[words[w]]
    name = " ".join(words)
    return name

austin_st_types = audit(osmfile)
# pprint.pprint(dict(austin_st_types)) 

for st_type, ways in austin_st_types.iteritems():
    for name in ways:
        better_name = update(name, mapping)
        print name, "=>", better_name

