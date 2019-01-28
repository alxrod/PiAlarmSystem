#Libraries
import RPi.GPIO as GPIO
import time
from picamera import PiCamera
from time import sleep
import os

# from twilio.rest import Client
def getUpdatedFileInfo():
    with open("./sensor_status.txt", "r") as fp:
#         print fp.read()
        values = fp.read().split(",")
        return float(values[0]), bool(values[1]), bool(values[2])

def takePic(photoInt):
    print "Taking a Picture!"
    GPIO.output(GPIO_LED, True)
    time.sleep(5);
    camera.capture('./static/images/' + str(int(round(time.time()))) + ".jpg")
    photoInt += 1
    GPIO.output(GPIO_LED, False)
    return True
    
def notifyUser(number, client):
#     client.messages.create(from_="+16178700118",
#                            to=number,
#                            body="PiAlarm has just detected a package on your door step, Visit 10.0.1.125:5000/images to see what's there!")
    print "Message Sent!"
    
def distance():
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    StartTime = time.time()
    StopTime = time.time()

    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()

    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

    TimeElapsed = StopTime - StartTime
    distance = (TimeElapsed * 34300) / 2

    return distance

if __name__ == '__main__':
#     account_sid = "AC2cc4c08fab15b4a7ac6717a6a66fa3a6"
#     auth_token = "126df82c59b94219fe0b3294498b1936"
    
#     clt = Client(account_sid, auth_token)
#     clt.messages.create(from_="+16178700118",
#                            to="+16173010887",
#                            body="PiAlarm has just detected a package on your door step, Visit 10.0.1.125:5000/images to see what's there!")
    print "Message Sent!"
    
    
    calibratedDistance, needToCalibrate, removalWatch = getUpdatedFileInfo()
    
    
    camera = PiCamera()
    camera.rotation = 180
    #GPIO Mode (BOARD / BCM)
    GPIO.setmode(GPIO.BCM)

    #set GPIO Pins
    GPIO_TRIGGER = 23
    GPIO_ECHO = 24
    GPIO_LED = 25

    timeBeenThere = 0 
    hasBeenDelivered = False
    hasBeenCollected = False
    
    
    #set GPIO direction (IN / OUT)
    GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
    GPIO.setup(GPIO_ECHO, GPIO.IN)
    GPIO.setup(GPIO_LED, GPIO.OUT)

    needToPic = False
    haveTakenPic = False

    print "Initialized"
    try:
        startingPoint = 10
        while True:
#             nCalibratedDistance, nNeedToCalibrate, nRemovalWatch = getUpdatedFileInfo()
        
        
        
            if (needToPic):
                print "hello?!?"
                haveTakenPic = takePic(startingPoint)
                startingPoint += 1
                needToPic = False
#                 notifyUser("+16173010887",clt)
            dist = distance()
            
            
            if dist < 100:
                if haveTakenPic == False and needToPic == False:
                    needToPic = True
            else:
                print 'Resetting!'
                haveTakenPic = False
            print ("Measured Distance = %.1f cm" % dist)        
        
            
            time.sleep(1)

        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()