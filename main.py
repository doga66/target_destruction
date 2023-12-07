import cv2
from pySerialTransfer import pySerialTransfer as txfer
import numpy as np
import time
import math





class struct(object):
    RollS = 0
    PitchS = 0
    HeadingS = 0
    frontLidarS = 0
    leftLidarS = 0
    rightLidarS = 0
    altitudeS = 0
    data1S = 0
    data2S = 0
    data3S = 0
    data4S = 0
    data5S = 0

class struct1(object):
    arac_ileri_degeri = 0
    arac_x_degeri = 0
    arac_y_degeri = 0
    arac_yengec_degeri = 0
    degree = 0


rovDataTx = struct1 # gönderilen
rovDataRx = struct # alınan

cam = cv2.VideoCapture(0)
width1 = int(cam.set(cv2.CAP_PROP_FRAME_WIDTH,640))
height1 = int(cam.set(cv2.CAP_PROP_FRAME_HEIGHT,480))

height,width = 480 , 640


link = txfer.SerialTransfer('/dev/ttyACM0')
link.open()

time.sleep(2) # allow some time for the Arduino to completely reset


while True:

    pass



    
    sendSize = 0
    sendSize = link.tx_obj(rovDataTx.arac_ileri_degeri, start_pos=sendSize)
    sendSize = link.tx_obj(rovDataTx.arac_y_degeri, start_pos=sendSize)
    sendSize = link.tx_obj(rovDataTx.arac_x_degeri, start_pos=sendSize)
    sendSize = link.tx_obj(rovDataTx.arac_yengec_degeri, start_pos=sendSize)
    sendSize = link.tx_obj(rovDataTx.degree, start_pos=sendSize)

    link.send(sendSize)
    time.sleep(0.3)

    if not link.available():
        # print("if'a girdi")
        if link.status < 0:
            if link.status == txfer.CRC_ERROR:
                print('ERROR: CRC_ERROR')
            elif link.status == txfer.PAYLOAD_ERROR:
                print('ERROR: PAYLOAD_ERROR')
            elif link.status == txfer.STOP_BYTE_ERROR:
                print('ERROR: STOP_BYTE_ERROR')
            else:
                    print('ERROR: {}'.format(link.status))