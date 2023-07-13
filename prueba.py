from datetime import datetime
import time
import random

odds = list(range(0,60,2))

second_now = datetime.today().second

if second_now in odds:
  print('segundo es par')
else:
  print('segundo es impar')

time.sleep(3)
print('3 segundos despues...')
print(random.randint(0,100))

