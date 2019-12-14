# -*- coding: utf-8 -*-
# inspired by the topic of https://www.raspberrypi.org/forums/viewtopic.php?f=32&t=114401&sid=5801fd51b8646985597e09d62d31a06f
#  especially the post of https://www.raspberrypi.org/forums/viewtopic.php?t=114401#p782496
# 
# © Takeyuki UEDA 2019 -

import argparse

#import smbus
import smbus2 as smbus



bus = smbus.SMBus(1) # 1 indicates /dev/i2c-1

for device in range(128):

      try:
         bus.read_byte(device)
         print(hex(device))
      except: # exception if read_byte fails
         pass

if __name__ == '__main__':
