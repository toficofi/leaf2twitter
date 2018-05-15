#!/usr/bin/python

import pycarwings2
import twitter
import os

# Grab carwings auth from env var
username = os.environ['CARWINGS_USERNAME']
password = os.environ['CARWINGS_PASSWORD']

# Initiate carwings session and grab battery status
s = pycarwings2.Session(username, password , "NE")
l = s.get_leaf()
leaf_info = l.get_latest_battery_status()

# Grab Twitter app keys from env vars
consumer_key = os.environ['TWITTER_CONSUMER_KEY']
consumer_secret = os.environ['TWITTER_CONSUMER_SECRET']
access_token_key = os.environ['TWITTER_ACCESS_TOKEN_KEY']
access_token_secret = os.environ['TWITTER_ACCESS_TOKEN_SECRET']


# Initiate Twitter API
api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token_key,
                  access_token_secret=access_token_secret)


pluggedInText = 'Plugged in ' if leaf_info.is_charging else 'Unplugged'
chargingText = "Not charging"

if leaf_info.is_charging:
    chargingText = "Slow charging"

if leaf_info.is_quick_charging:
    chargingText = "Rapid charging"

# Convert the km to miles because that's how I like it
kilometers = leaf_info.cruising_range_ac_off_km
conversion_factor = 0.62137119

miles = kilometers * conversion_factor

capacityText = str(int(leaf_info.battery_percent)) + "% (" + str(int(miles)) + " miles)"

print pluggedInText
print chargingText
print capacityText

# Some fun emoji
text = u'\U0001F50C' + " " + pluggedInText + "\n" +u'\U000026A1' + " " + chargingText + "\n" +u'\U000026FD' + " " + capacityText + "\n" 

# Tweet that shit
api.PostUpdate(text)