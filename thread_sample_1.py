import threading
import queue  # library for queu operation
import time
from thread_one_class import thread_one  # import thread body
import random
#
import time
import ADS1256
import RPi.GPIO as GPIO
#
ADC = ADS1256.ADS1256()
ADC.ADS1256_init()
#
i=1   # counter
thread1=thread_one(i) #provide a thread
q =queue.Queue()  # queue which stores a result of a thread
th = threading.Thread(target=thread1.thread, args=(i,q),daemon=True)
# setting of thread
a=1
q.put(a)
th.start() # start thread
while True:  # infinite loop
  ADC_Value = ADC.ADS1256_GetAll()
  print ("0 ADC = %lf"%(ADC_Value[0]*5.0/0x7fffff))
  print ("1 ADC = %lf"%(ADC_Value[1]*5.0/0x7fffff))
  print ("2 ADC = %lf"%(ADC_Value[2]*5.0/0x7fffff))
  print ("3 ADC = %lf"%(ADC_Value[3]*5.0/0x7fffff))
  print ("4 ADC = %lf"%(ADC_Value[4]*5.0/0x7fffff))
  print ("5 ADC = %lf"%(ADC_Value[5]*5.0/0x7fffff))
  print ("6 ADC = %lf"%(ADC_Value[6]*5.0/0x7fffff))
  print ("7 ADC = %lf"%(ADC_Value[7]*5.0/0x7fffff))
  print ("\33[9A")
  if th.is_alive()==False:  #when thread ends
    result = q.get()  # take queu values
#    print("thread: "+str(i)+" "+str(result))
    i=i+1
#    if i>5:  # execute total five thread 
#      break;  # exit loop
    thread1=thread_one(i) #proivide the next thread
    a=i % 2
    q.put(a)
    th = threading.Thread(target=thread1.thread, args=(i,q),daemon=True)
    # setting the next thread
    th.start() # start thread
  time.sleep(2)  #do other tasks
#
GPIO.cleanup()
exit()
