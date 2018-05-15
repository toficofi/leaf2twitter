#!/usr/bin/python

import pycarwings2
import os

# Grab carwings auth from env var
username = os.environ['CARWINGS_USERNAME']
password = os.environ['CARWINGS_PASSWORD']

# Initiate carwings session and grab battery status
s = pycarwings2.Session(username, password , "NE")
l = s.get_leaf()
l.request_update()

print "Requested update from vehicle"