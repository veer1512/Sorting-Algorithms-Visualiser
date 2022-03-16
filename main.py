# Main Executable file to run the visualizer project.
# Import all packages and modules in this file.
# Setup basic Graphical User Interface


# ---------------------------------------------------------
### IMPORTS ###

# From tkinter import all
from tkinter import *

# To configure tkinter widgets with style
from tkinter import ttk 

# To create random sequence
import random

# Import colors for project
from colors import *

# Import Sorting Algorithms
from algorithms.Bubble_sort import bubble_sort
from algorithms.Merge_sort import merge_sort
from algorithms.Selection_sort import selection_sort
from algorithms.Insertion_sort import insertion_sort

# ---------------------------------------------------------
### ROOT WINDOW ###

# Create a basic tkinter window. 
window = Tk() # assign window as window object name
window.title("Sorting Algorithms Visualizer")
window.maxsize(1200,700)
window.config(bg = WHITE)
window.geometry('850x550')




# ---------------------------------------------------------
### VARIABLES ###

# StringVar(): class to monitor changes to tkinter variables. 
# eg: via buttons

algo_name = StringVar() 
algo_list = ["Bubble-sort","Merge-sort","Selection-sort","Insertion-sort"]

speed_name = StringVar()
speed_list = ['Fast','Medium','Slow']

# To store random values generated to feed sorter
data = []




# ---------------------------------------------------------
### FUNCTIONS ###

# ------------------------------
def drawData(data,colorArray):
  '''visualize randomized sequence feed as vertical bars'''

  # Clear canvas 
  canvas.delete('all')

  # Canvas Dimensions
  canvas_width = 800
  canvas_height = 400+10 # +10 for clean representation of highest bar

  # Width of each vertical section w.r.t total data points in feed
  x_width = canvas_width / (len(data)+1)

  offset = 4
  spacing = 2

  # 0 < normalised_Data value height  <= 1
  normalised_Data = [i/max(data) for i in data]

  # Creating vertical bars(rectangles)
  for i,height in enumerate(normalised_Data):

    # (x0,y0)
    # *----------
    # |         |
    # |         |
    # |         |
    # ----------*
    #         (x1,y1)

    # rectangle width 
    x0 = i * x_width + offset + spacing
    x1 = (i+1) * x_width  + offset + spacing

    # rectangle height 
    y0 = canvas_height - (height*400)
    y1 = canvas_height

    # create a rectangle
    canvas.create_rectangle(x0,y0,x1,y1, fill = colorArray[i])
  
  window.update_idletasks()


# ---------------
def generate():
  '''generate array of random values'''
  
  # Make data to be modify-able from within function. 
  global data 

  # For faster  list initialisation
  # Immutable: [obj]*n  # [0]*n Same id for each obj
  # Mutable: [obj for _ in range(n)]  Different id for each obj

  data = [None]*100 # Taken DataPoints 100 nos.

  for i in range(0,100):
    data[i] = random.randint(1,150) # random values

  drawData(data, [BLUE for _ in range(len(data))])




# ----------------
def set_speed():
  '''set sorting speed'''

  speed_value = {
    'Slow': 0.5,
    'Medium': 0.01,
    'Fast': 0.001,
  }

  speed_name = speed_menu.get()
  return speed_value[speed_name]


# -----------
def sort():
  '''Trigger the selected algorithm and start sorting'''
  global data
  timeTick = set_speed()

  if algo_menu.get() == 'Bubble-sort':
    bubble_sort(data, drawData, timeTick)

  elif algo_menu.get() == 'Merge-sort':
    merge_sort(data, 0, len(data)-1, drawData, timeTick)

  elif algo_menu.get() == 'Selection-sort':
    selection_sort(data, drawData, timeTick)

  elif algo_menu.get() == 'Insertion-sort':
    insertion_sort(data,drawData,timeTick)

# ---------------------------------------------------------
### USER INTERFACE SETUP ###

# Requirements
# - 2 dropdown menus. (select algo,speed)
# - 2 buttons. (generate random array,start sorting)
# - A canvas to draw array.

# Design
# + UI_frame
#   - dropdown
#   - buttons
# + canvas

UI_frame = Frame(window, width=900, height=300, bg=BLUE)
UI_frame.grid(row=0, column=0, padx=10, pady=5)

# dropdown to select Sorting Algorithms
l1 = Label(UI_frame, text='Algorithm: ', bg=WHITE)
l1.grid(row=0, column=0, padx=10, pady=5, sticky=W)
algo_menu = ttk.Combobox(UI_frame, textvariable = algo_name, values = algo_list)
algo_menu.grid(row=0, column=1, padx=5, pady=5)
algo_menu.current(0)

# dropdown to select sorting speed 
l2 = Label(UI_frame, text="Sorting Speed: ", bg=WHITE)
l2.grid(row=1, column=0, padx=10, pady=5, sticky=W)
speed_menu = ttk.Combobox(UI_frame, textvariable=speed_name, values=speed_list)
speed_menu.grid(row=1, column=1, padx=5, pady=5)
speed_menu.current(0)

# button to generate random array 
b1 = Button(UI_frame, text='Generate Random Sequence', command=generate, bg=LIGHT_GRAY)
b1.grid(row=2, column=0, padx=5, pady=5)

# sort button 
b2 = Button(UI_frame, text='Sort', command=sort, bg = LIGHT_GRAY)
b2.grid(row=2, column=1, padx=5, pady=5)

# Canvas to draw array sequence 
canvas = Canvas(window, width=800, height=400, bg=WHITE) 
canvas.grid(row=1,column=0, padx=10, pady=5)

# Display
window.mainloop() # Infinite loop running application as long as window is not closed.

