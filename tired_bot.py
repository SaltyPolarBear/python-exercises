import datetime
from time import sleep
import replit
eye_state = 0
current_text = ('')
speech = ('what do you want?','go away, im tired')
def eye_open():
  print(' _______        _______ ')
  print(' |  0  |        |  0  | ')
  print(' -------   \    ------- ')
  print('           /            ')
  print('       __________       ')
  print('        \/              ')
def eye_closed():
  print()
  print(' _______        _______ ')
  print(' -------   \    ------- ')
  print('           /            ')
  print('       __________       ')
  print('        \/              ')
while True:
  if eye_state%4 == 0:
    eye_closed()
  else:
    eye_open()
  sleep (1)
  eye_state += 1
  replit.clear()
  print(current_text)
