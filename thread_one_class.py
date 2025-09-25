class thread_one:

  def __init__(self,i):   # initial action
#    print(" start "+str(i))
    import RPi.GPIO as GPIO
    #GPIO.setwarnings(False)
    #GPIO.setmode(GPIO.BCM)
    #GPIO.setup(35, GPIO.OUT)  # bottom heater
    return
  def thread(self,i,q): # class body
    import time
    import random
    import RPi.GPIO as GPIO
    a=q.get()   # get Tc temp
    if a==1:
      GPIO.output(35,1)
    else:
      GPIO.output(35,0)
    return
