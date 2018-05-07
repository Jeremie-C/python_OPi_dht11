#!/usr/bin/env python
# -*- coding: utf-8 -*-

from OPi import gpio
from dht11 import dht11

import time
import datetime

# initialize GPIO
PIN11 = gpio.PIN11
gpio.init()

# read data using pin 11
instance = dht11.DHT11(pin=PIN11)

while True:
  result = instance.read()
  if result.is_valid():
    print("Last valid input: " + str(datetime.datetime.now()))
    print("Temperature: {0:0.2f} C".format(result.temperature))
    print("Humidity: {0:0.1f} %".format(result.humidity))

  time.sleep(1)
