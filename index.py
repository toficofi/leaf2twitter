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

print "get_latest_battery_status"
leaf_info = l.get_latest_battery_status()
print "date %s" % leaf_info.answer["BatteryStatusRecords"]["OperationDateAndTime"]
print "date %s" % leaf_info.answer["BatteryStatusRecords"]["NotificationDateAndTime"]
print "battery_capacity2 %s" % leaf_info.answer["BatteryStatusRecords"]["BatteryStatus"]["BatteryCapacity"]

print "battery_capacity %s" % leaf_info.battery_capacity
print "charging_status %s" % leaf_info.charging_status
print "battery_capacity %s" % leaf_info.battery_capacity
print "battery_remaining_amount %s" % leaf_info.battery_remaining_amount
print "charging_status %s" % leaf_info.charging_status
print "is_charging %s" % leaf_info.is_charging
print "is_quick_charging %s" % leaf_info.is_quick_charging
print "plugin_state %s" % leaf_info.plugin_state
print "is_connected %s" % leaf_info.is_connected
print "is_connected_to_quick_charger %s" % leaf_info.is_connected_to_quick_charger
print "time_to_full_trickle %s" % leaf_info.time_to_full_trickle
print "time_to_full_l2 %s" % leaf_info.time_to_full_l2
print "time_to_full_l2_6kw %s" % leaf_info.time_to_full_l2_6kw
print "leaf_info.battery_percent %s" % leaf_info.battery_percent
print "leaf_info.state_of_charge %s" % leaf_info.state_of_charge