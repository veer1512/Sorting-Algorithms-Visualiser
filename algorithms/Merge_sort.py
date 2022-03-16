# For some time difference between each comparison
import time
from colors import *

def merge_sort(data, left_index, right_index, drawData, timeTick):
  '''Divide data array into two halves and sort each half recursively'''

  if left_index < right_index:
    mid = (left_index + right_index)//2  

    merge_sort(data, left_index, mid, drawData, timeTick)
    merge_sort(data, mid+1, right_index, drawData, timeTick)
    merge(data, left_index, right_index, mid)
    # visualise
    drawData(data, [
      PURPLE if x >= left_index and x < mid else 
      YELLOW if x == mid else 
      DARK_BLUE if x > mid and x <= right_index else 
      BLUE for x in range(len(data)) 
      ])
    time.sleep(timeTick)

    
  drawData(data, [BLUE for x in range(len(data))])




def merge(data, left_index, right_index, mid):
  '''Merge two sorted halves of data'''

  # Make copies of both halves that require merging 
  left_copy = data[left_index : mid+1]
  right_copy = data [mid+1 : right_index+1]

  # Initialise to keep track of sorting status 
  left_copy_index = 0
  right_copy_index = 0
  sorted_index = left_index
  # left_copy   right_copy
  # ---------  -----------
  # |          | 

  # -----------
  # | (sorted_index)

  # Go through both copies until one gets exhausted
  while left_copy_index < len(left_copy) and right_copy_index < len(right_copy):
    
    # Compare left right copies and refill data array in ascending order
    if left_copy[left_copy_index] <= right_copy[right_copy_index]:
      data[sorted_index] = left_copy[left_copy_index]
      left_copy_index = left_copy_index + 1

    else:
      data[sorted_index] = right_copy[right_copy_index]
      right_copy_index = right_copy_index + 1

    # Move forward in sorted part after every fill
    sorted_index = sorted_index + 1

  # If a half gets exhausted, add remaining elements of another half
  while left_copy_index < len(left_copy):
    data[sorted_index] = left_copy[left_copy_index]
    left_copy_index = left_copy_index + 1
    sorted_index = sorted_index + 1

  while right_copy_index < len(right_copy):
    data[sorted_index] = right_copy[right_copy_index]
    right_copy_index = right_copy_index + 1
    sorted_index = sorted_index + 1


 
