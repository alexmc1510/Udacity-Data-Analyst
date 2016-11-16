# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 23:02:41 2016

@author: ahada
"""

import re

def update_postcode(zipcode):
	"""Trims leading and trailing character from zipcode, returning only digits"""
	# d+ = matches 1 or more occurence of digits
    m = re.search(r'\d+', zipcode) #returns entire match
    if m:
        return m.group()
    else:
        return None
