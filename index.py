#!/usr/bin/python

import pycarwings2
import time
from ConfigParser import SafeConfigParser
import logging
import sys
import pprint
import os

logging.basicConfig(stream=sys.stdout, level=logging.ERROR)

username = os.environ['CARWINGS_USERNAME']
password = os.environ['CARWINGS_PASSWORD']

logging.debug("login = %s , password = %s" % ( username , password)  )

print "Prepare Session"
s = pycarwings2.Session(username, password , "NE")
print "Login..."

l = s.get_leaf()
leaf_info = l.get_latest_battery_status()


print "is_charging %s" % leaf_info.is_charging
print "is_quick_charging %s" % leaf_info.is_quick_charging
print "is_connected %s" % leaf_info.is_connected
print "is_connected_to_quick_charger %s" % leaf_info.is_connected_to_quick_charger
print "leaf_info.battery_percent %s" % leaf_info.battery_percent
print "leaf_info.cruising_range_ac_off_km %s" % leaf_info.cruising_range_ac_off_km