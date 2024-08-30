# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 20:1 7:29 2022

@author: Alfonso Blanco
"""
######################################################################
# PARAMETERS
#####################################################################
######################################################

frame_width = 640
frame_height = 480
WindowFactor= 2/3

# videos from https://www.pexels.com/video/road-trip-4434242/
#dirVideo="4832679-uhd_3840_2160_30fps.mp4"
dirVideo="production_id_4606790 (2160p).mp4"

######################################################################
from paddleocr import PaddleOCR
# Paddleocr supports Chinese, English, French, German, Korean and Japanese.
# You can set the parameter `lang` as `ch`, `en`, `french`, `german`, `korean`, `japan`
# to switch the language model in order.
# https://pypi.org/project/paddleocr/
#
# supress anoysing logging messages parameter show_log = False
# https://github.com/PaddlePaddle/PaddleOCR/issues/2348
ocr = PaddleOCR(use_angle_cls=True, lang='en', show_log = False) # need to run only once to download and load model into memory

import cv2

import time

TimeIni=time.time()


def GetPaddleOcr(img):

       
    cv2.imwrite("gray.jpg",img)
    img_path = 'gray.jpg'

    licensePlate= ""
    accuracy=0.0
    
    results = ocr.ocr(img_path,  cls=True)
    # draw result
    #from PIL import Image
    #print("len(results) " + str(len(results)))
    for i in range(len(results)):
          result = results[i]
          #image = Image.open(img_path).convert('RGB')
          boxes = [line[0] for line in result]
    
          txts = [line[1][0] for line in result]
          scores = [line[1][1] for line in result]
    
    
          #print("RESULTADO  "+ str(txts))
          #print("confiabilidad  "+ str(scores))
          if len(txts) > 0:
             for j in range(len(txts)):
              licensePlate= licensePlate + " " +  txts[j]
             #accuracy=float(scores[0])
    #print(licensePlate)
    #print(accuracy)
      
    return licensePlate, accuracy
###########################################################
# MAIN
##########################################################

cap = cv2.VideoCapture(dirVideo)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)

while (cap.isOpened()):
    ret, image = cap.read()

    if ret != True: break

    else:
       
        image = cv2.resize(image, (frame_width, frame_height))
        imageDetect=image[0:int(WindowFactor*frame_height) , 0:frame_width]
        cv2.rectangle(image,(0,0),(frame_width ,int( WindowFactor*frame_height)),color=(255,0,0))
        text, Accuraccy = GetPaddleOcr(imageDetect)
        # if Accuraccy < AccuraccyMin:
        #     text=""
       
        if text != "":
           print(text)
        # show the output image
        cv2.imshow("Text Detection", image)
        cv2.waitKey(1)

        
cap.release()

cv2.destroyAllWindows()

print("")           
print( " Time in seconds "+ str(time.time()- TimeIni))
print("")           
