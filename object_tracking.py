import cv2
import numpy as np
#from adafruit_servokit import ServoKit
import time
import os
import Adafruit_PCA9685
import time
pwm = Adafruit_PCA9685.PCA9685()
speed0 = int(input("Lutfen servo0 icin istediginiz hizi seciniz (Tavsiye edilen '3'): "))
speed1 = int(input("Lutfen servo1 icin istediginiz hizi seciniz (Tavsiye edilen '2'): "))

HAAR_CASCADE_XML_FILE_FACE = "/usr/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml"


def faceDetect():
    
    face_cascade = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")
    cap = cv2.VideoCapture(0)

    servo0=365
    servo1=365
    pwm.set_pwm(0, 0, servo0)
    pwm.set_pwm(1, 0, servo1) 
    if cap.isOpened():

        while True:
            ret, image = cap.read()
            
            

            img2shape=640/2
            img1shape=480/2
            
            
            if not ret:
                break
            grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            detected_faces = face_cascade.detectMultiScale(grayscale_image, 1.3, 5)
            cv2.rectangle(image, (int(img2shape-75), int(img1shape-75)), (int(img2shape+75), int(img1shape+75)),(255,0,0),2)
            
            for (x_pos, y_pos, width, height) in detected_faces:
                test=y_pos
                test=test-30
                cv2.putText(image, "Detected", (520,25),cv2.FONT_HERSHEY_SIMPLEX,0.75,(0,0,255),2)
                cv2.rectangle(image, (x_pos, y_pos), (x_pos + width, y_pos + height), (0, 255, 0), 2)
                yi=y_pos+height
                xx=x_pos/2
                yy=y_pos/2
                xc=x_pos+xx
                yc=y_pos+yy
                #if(xc>img2shape-65 and xc<img2shape+65):
                    #continue
                if xc<img2shape-75:
                    servo0=servo0+speed0
                    pwm.set_pwm(0, 0, servo0)
                if xc>img2shape+75:
                    servo0=servo0-speed0
                    pwm.set_pwm(0, 0, servo0)
                if yc<img1shape-75:
                    servo1=servo1-speed1
                    pwm.set_pwm(1, 1, servo1)
                if yc>img1shape+75:
                    servo1=servo1+speed1
                    pwm.set_pwm(1, 1, servo1)
            cv2.imshow("Face Detection Window", image)

            if(cv2.waitKey(1) & 0xFF==ord("q")):
                break
            
        cap.release()
        cv2.destroyAllWindows()



faceDetect()

