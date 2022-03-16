# For some time difference between each comparison
import time

from colors import *

def bubble_sort(data, drawData, timeTick):
  ''' Implementation of Bubble Sorting Algorithm'''
  size = len(data)

  for i in range(size-1):
    for j in range(size-1-i):
      
      if data[j] > data[j+1]: # swap
        data[j], data[j+1]  = data[j+1], data[j] 

        drawData(data, [YELLOW if x==j or x==j+1 else BLUE for x in range(size)])
        time.sleep(timeTick)
      
  drawData(data, [BLUE for x in range(size)])
