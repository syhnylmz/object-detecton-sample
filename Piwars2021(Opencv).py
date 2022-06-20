try:   
    import cv2
    import numpy as np
    import RPi.GPIO as GPIO
    import time
    import Pi20

    motorlar = Pi20.MotorKontrol()

    GPIO.setmode(GPIO.BCM)

    GPIO.setwarnings(False)
    TRIG = 14
    ECHO = 15

    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)




    distance=10
    sayac=0
    TLRS = 60
    xorta = 320
    renk=0
    x=0   # cisim x koordinat 
    y=0   # cisim y koordinat 
    w=0   # cisim w koordinat 
    h=0   # cisim h koordinat 
    xe=0
    ye=0
    cap = cv2.VideoCapture(0)


    ret=cap.set(3, 600)
    ret=cap.set(3, 600) # cap degiskenine atanan videonun boyutu belirlendi
    ret, frame = cap.read()  # ret
    rows, cols, _ = frame.shape

    x_medium = int(cols / 2)
    y_medium = int(cols / 2)
    w_medium = int(cols / 2)
    h_medium = int(cols / 2)
    center = int(cols / 2)     # cizme ait x y h w bilgileri degiskenlere atandi
        
                


    while True: # sonsuz donguye girildi
        
        
        if(renk==0):
            low=np.array([21,35,46])  
            high= np.array([35,78,123])
        if(renk==1):
            low=np.array([100,80,50])  #
            high= np.array([115, 255, 255])
        if(renk==2):
            low=np.array([31,90,90])  
            high= np.array([48, 255, 255])
        if(renk==3):
            low=np.array([100,80,50])  #
            high= np.array([115, 255, 255])
        if(renk==4):
            low=np.array([14, 92, 92])  
            high= np.array([26, 200, 200])
        if(renk==5):
            low=np.array([100,80,50])  #
            high= np.array([115, 255, 255])
        if(renk==6):
            low=np.array([2,90,90])  
            high= np.array([12, 255, 255])
        if(renk==7):
            low=np.array([100,80,50])  #
            high= np.array([115, 255, 255])
        if(renk==8):
            low=np.array([21,35,46])  
            high= np.array([35,78,123])
        if(renk==9):
            low=np.array([100,80,50])  #
            high= np.array([115, 255, 255])
        ret, frame = cap.read()
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)      
        mask = cv2.inRange(hsv_frame, low, high)      
        _, contours,hierachy=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=lambda x:cv2.contourArea(x), reverse=True)
        
        


        for cnt in contours:
            (x, y, w, h) = cv2.boundingRect(cnt) # algilanan rengin x ve y koordinatlari bulundu        
            if(x!=0 and y!=0):
                x_medium = int((x + x + w)/2) 
                y_medium = int((y + y + h)/2)
                break
            if(x==0 and y==0):
                x_medium = 0
                y_medium = 0
        if(xe==x and ye==y and (x!=0 or y!=0)):
            sayac=sayac+1
        if(xe!=x and ye!=y):
            sayac=0     
        if(sayac==35):
            x_medium =0
            sayac=0
            x=0   
            y=0   
            w=0   
            h=0   
            xe=0
            ye=0
            
        xe=x
        ye=y
        
        cv2.line(frame, (x_medium, 0), (x_medium, 480), (0, 0, 255), 2)  # x koordinati ekranda gosterildi                                     
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,250),3) 
        cv2.putText(frame,"RENK",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,250),4)
        
        

        if(0==x and 0==y and 0==w and 0==h): 
            motorlar.hizlariAyarla(90,-115)
        
                
                
        if(0!=x or 0!=y):
            if(distance<=5):
                if(renk==0):
                    x_medium=0
                    sayac=0
                    x=0   
                    y=0   
                    w=0   
                    h=0   
                    xe=0
                    ye=0
                    renk=1
                    distance=10
                if(renk==2):
                    x_medium=0
                    sayac=0
                    x=0   
                    y=0   
                    w=0   
                    h=0   
                    xe=0
                    ye=0
                    renk=3
                    distance=10
                if(renk==4):
                    x_medium=0
                    sayac=0
                    x=0   
                    y=0   
                    w=0   
                    h=0   
                    xe=0
                    ye=0
                    renk=5
                    distance=10
                if(renk==6):
                    x_medium=0
                    sayac=0
                    x=0   
                    y=0   
                    w=0   
                    h=0   
                    xe=0
                    ye=0
                    renk=7
                    distance=10
                if(renk==8):
                    x_medium=0
                    sayac=0
                    x=0   
                    y=0   
                    w=0   
                    h=0   
                    xe=0
                    ye=0
                    renk=9
                    distance=10
            if(renk==1 or renk==3 or renk==5 or renk==7 or renk==9): 
                if((x!=0 or y!=0)and x_medium>=xorta-30 and x_medium<=xorta+30):
                    cv2.rectangle(frame,(290,-50),(350,640),(0,255,0),3)
                    motorlar.hizlariAyarla(-125,-125)
                    time.sleep(1.5)
                    motorlar.hizlariAyarla(100,100)
                    time.sleep(1)
                    if(renk==1):
                        x_medium=0
                        sayac=0
                        x=0   
                        y=0   
                        w=0   
                        h=0   
                        xe=0
                        ye=0
                        renk=2
                    if(renk==3):
                        x_medium=0
                        sayac=0
                        x=0   
                        y=0   
                        w=0   
                        h=0   
                        xe=0
                        ye=0
                        renk=4
                    if(renk==5):
                        x_medium=0
                        sayac=0
                        x=0   
                        y=0   
                        w=0   
                        h=0   
                        xe=0
                        ye=0
                        renk=6
                    if(renk==7):
                        x_medium=0
                        sayac=0
                        x=0   
                        y=0   
                        w=0   
                        h=0   
                        xe=0
                        ye=0
                        renk=8
                    if(renk==9):
                        motorlar.hizlariAyarla(0,0)
                        break
                        
                if((x!=0 or y!=0) and x_medium<xorta-30):
                    print("sola don")
                    cv2.rectangle(frame,(290,-50),(350,640),(0,0,0),3)
                    motorlar.hizlariAyarla(90,-90)
                if((x!=0 or y!=0) and x_medium>xorta+30):
                    print("sag don")
                    cv2.rectangle(frame,(290,-50),(350,640),(0,0,0),3)
                    motorlar.hizlariAyarla(-90,90)
            if(renk==0 or renk==2 or renk==4 or renk==6 or renk==8 ):
                if(x!=0 and x_medium>=xorta-TLRS and x_medium<=xorta+TLRS):
                    cv2.rectangle(frame,(260,-50),(380,640),(0,255,0),3)
                    if(renk==0 or renk==2 or renk==4 or renk==6 or renk==8):
                        GPIO.output(TRIG, True)
                        time.sleep(0.000001)
                        GPIO.output(TRIG, False)
                        while GPIO.input(ECHO)==0:
                            pulse_start = time.time()
                        while GPIO.input(ECHO)==1:
                            pulse_end = time.time()
                        pulse_duration = pulse_end - pulse_start
                        distance = pulse_duration * 17150
                        distance = round(distance, 2)    
                    if(distance>5):
                        motorlar.hizlariAyarla(-100,-100)
                        print("ilerle")
                    if(distance<=5):
                        if(renk==0):
                            x_medium=0
                            sayac=0
                            x=0   
                            y=0   
                            w=0   
                            h=0   
                            xe=0
                            ye=0
                            renk=1
                            distance=10
                        if(renk==2):
                            x_medium=0
                            sayac=0
                            x=0   
                            y=0   
                            w=0   
                            h=0   
                            xe=0
                            ye=0
                            renk=3
                            distance=10
                        if(renk==4):
                            x_medium=0
                            sayac=0
                            x=0   
                            y=0   
                            w=0   
                            h=0   
                            xe=0
                            ye=0
                            renk=5
                            distance=10
                        if(renk==6):
                            x_medium=0
                            sayac=0
                            x=0   
                            y=0   
                            w=0   
                            h=0   
                            xe=0
                            ye=0
                            renk=7
                            distance=10
                        if(renk==8):
                            x_medium=0
                            sayac=0
                            x=0   
                            y=0   
                            w=0   
                            h=0   
                            xe=0
                            ye=0
                            renk=9
                            distance=10
                if(x!=0 and x_medium<xorta-TLRS):
                    print("sola don")
                    cv2.rectangle(frame,(260,-50),(380,640),(0,0,0),3)
                    motorlar.hizlariAyarla(90,-90)
                if(x!=0  and x_medium>xorta+TLRS):
                    print("sag don")
                    cv2.rectangle(frame,(260,-50),(380,640),(0,0,0),3)
                    motorlar.hizlariAyarla(-90,90)
            

                

                    
                   
                
                     
        
     
        cv2.imshow("Frame", frame)   
        cv2.imshow("mask",mask)         
        print("x ",x," y ",y,"h",h,"renk",renk,"x_medium: ",x_medium,"distance" ,distance)
        key = cv2.waitKey(1)
        
        


        

            
    cap.release()
    cv2.destroyAllWindows()
finally:
    motorlar.hizlariAyarla(0,0)