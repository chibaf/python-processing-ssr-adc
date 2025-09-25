from multiprocessing import Process

def f(ssr,swt):
  import RPi.GPIO as GPIO
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(int(ssr), GPIO.OUT)  # bottom heater
  GPIO.output(int(ssr), swt)

import time
while(1):
  if __name__ == '__main__':
    p = Process(target=f, args=(35,1,))
    p.start()
    p.join()
    time.sleep(1)
    p = Process(target=f, args=(35,0,))
    p.start()
    p.join()
    time.sleep(1)
