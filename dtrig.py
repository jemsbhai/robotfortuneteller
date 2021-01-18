#Libraries
import RPi.GPIO as GPIO
import time
import os
import subprocess
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_TRIGGER = 24
GPIO_ECHO = 26
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
 
def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance
 
if __name__ == '__main__':
    try:
        p2 = subprocess.Popen(['vlc', '/home/pi/robotlove/idle_screen.mp4', '--no-video-title', '--loop', '--fullscreen'])
        while True:
            dist = distance() 
            # px = subprocess.Popen(['sudo', 'python3', '/home/pi/robotlove/pixel1.py'])

            print ("Measured Distance = %.1f cm" % dist)
            if dist < 15:
                p2.kill()
                p1 = subprocess.Popen(['vlc', '/home/pi/robotlove/whole_video_uncut.mp4', '--no-video-title', '--loop', '--fullscreen'])
                os.system("sudo python3 basictellerv1.py")
                p1.kill()
                p2 = subprocess.Popen(['vlc', '/home/pi/robotlove/idle_screen.mp4', '--no-video-title', '--loop', '--fullscreen'])
            time.sleep(4)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()