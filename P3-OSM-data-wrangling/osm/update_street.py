# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 03:11:55 2016

@author: ahada
"""

"""
- audit the OSMFILE and change the variable 'mapping' to reflect the changes needed to fix 
    the unexpected street types to the appropriate ones in the expected list.
    You have to add mappings only for the actual problems you find in this OSMFILE,
    not a generalized solution, since that may and will depend on the particular area you are auditing.
- write the update function, to actually fix the street name.
    The function takes a string with street name as an argument and should return the fixed name
"""

import re

street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE) #pulls out or matches the very last word in street name (RE pattern)


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


def update(name):
    words = name.split()
    for w in range(len(words)):
        if words[w] in mapping:
            if words[w-1].lower() not in ['suite', 'ste.', 'ste', 'avenue', 'ave']: # For example, don't update 'Suite E' to 'Suite East'
                words[w] = mapping[words[w]]

    name = " ".join(words)
    return name
    

def audit_st_name(st_name):
    m = street_type_re.search(st_name)
    if m:
        st_type = m.group()
        if st_type not in expected:
            return update(st_name)
    return st_name