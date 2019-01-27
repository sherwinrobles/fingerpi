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
ID = input('Please type ID to enroll and press <Enter> : ')

response = f.CheckEnrolled(int(ID))
if response[0]['ACK']:
    raise 'ID in use!' + response[0]['Parameter']


f.EnrollStart(int(ID))
print 'Enroll has been started...'

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

f.Enroll1()
print 'Enroll 1'

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


f.Enroll2()
print 'Enroll 2'

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

print 'Enroll 3'
response = f.Enroll3()
if response[0]['Parameter']:
    print 'Previously enrolled to ID: ', response[0]['Parameter']
else:
    print 'Transmitting image...'
    t = time.time()
    raw_img = f.GetImage()
    tx_time = time.time() - t
    # print raw_img[0]['ACK'],
    # print raw_img[1]['Checksum']
    print 'Time to transmit:', tx_time

    print 'Closing connection...'
    f.Close()

    with open('raw_img.pickle', 'w') as f:
        pickle.dump(raw_img, f)

    # f = figure()
    # f.imshow()
