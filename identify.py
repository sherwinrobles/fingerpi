#!/usr/bin/env python2

import fingerpi as fp
# from fingerpi import base

# import struct
import time
# import matplotlib.pyplot as plt
import pickle


def printByteArray(arr):
    return map(hex, list(arr))

f = fp.FingerPi()

print 'Opening connection...'
f.Open(extra_info = True, check_baudrate = True)

print 'Changing baudrate...'
f.ChangeBaudrate(115200)
# f.CmosLed(False)

while True:
    print 'Place the finger on the scanner and press <Enter>'
    _ = raw_input()
    f.CmosLed(True)
    # response = f.IsPressFinger()
    response = f.CaptureFinger()
    if response[0]['ACK']:
        break
    f.CmosLed(False)
    if response[0]['Parameter'] != 'NACK_FINGER_IS_NOT_PRESSED':
        print 'Unknown Error occured', response[0]['Parameter']
        
# print f.UsbInternalCheck()
        
print 'Image captured!'
f.CmosLed(False)

response = f.Identify()
if response[0]['ACK']:
    # screen.addstr(3, 2, 'ID in use!')
    # screen.clrtoeol()
    print 'ID {0:d} identified'.format(response[0]['Parameter'])
else:
    print response[0]['Parameter']

# print raw_img[0]['ACK'],
# print raw_img[1]['Checksum']


print 'Closing connection...'
f.Close()


# f = figure()
# f.imshow()
