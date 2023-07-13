from datetime import datetime
from os import getcwd
import time
from random import randint

 
odds = [ 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21,
         23, 25, 27, 29, 31, 33, 35, 37, 39, 41,
         43, 45, 47, 49, 51, 53, 55, 57, 59 ]

for i in range(5):
  if datetime.today().minute in odds:
    print("odd minute")
  else:
    print("even minute")
  time.sleep( randint(1,4) )

print( getcwd() )
