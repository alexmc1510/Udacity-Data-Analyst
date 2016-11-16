# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 08:26:18 2016

@author: ahada
"""

import phonenumbers

def update_phonenumber(phonenumber):
    '''fix and standardize phone numbers using phonenumbers module'''
    matches = [match.number for match in phonenumbers.PhoneNumberMatcher(phonenumber, "US")]
    updated_matches = [phonenumbers.format_number(match,phonenumbers.PhoneNumberFormat.NATIONAL)
        for match in matches]
    phonenumber = ';'.join(updated_matches)
    return phonenumber
   