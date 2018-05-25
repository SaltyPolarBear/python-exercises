#imports---------------------------------------------------------
from time import sleep
import replit
import random

#Base Stats------------------------------------------------------
female_pronouns = ['she','hers','her']
male_pronouns = ['he','his','him']
current_pronouns = female_pronouns
player_health = 20
attack = 1
p, bold, italic, flashing, flashingfast, red, green, yellow, blue, violet, lightBlue, white, hred, hgreen, hyellow, hblue, hviolet, hlightBlue, hwhite = 'p', 'bold', 'italic', 'flashing', 'flashingfast', 'red', 'green', 'yellow', 'blue', 'violet', 'lightBlue', 'white', ';hred', ';hgreen', ';hyellow', ';hblue', ';hviolet', ';hlightBlue', ';hwhite'
font_ = {'p':'0','bold':'1','italic':'3','flashing':'5','flashingfast':'6'}
color_ = {'p':'29','red':'31','green':'32','yellow':'33','blue':'34','violet':'35','lightBlue':'36','white':'37'}
highlight_ = {'p':'',';hred':';41',';hgreen':';42',';hyellow':';43',';hblue':';44',';hviolet':';45',';hlightBlue':';46',';hwhite':';47'}

#Enemies---------------------------------------------------------
'''
def goblin():
def lamia():
'''

#Moves-----------------------------------------------------------

#Other-----------------------------------------------------------
from time import sleep
def sprint(string):
  for x in string:
    print (x, end='', flush = True)
    sleep (0.05)
def cprint(text,color,highlight,words):
  if text in font_ and color in color_ and highlight in highlight_:
    print ('\x1b['+font_[text]+';'+color_[color]+highlight_[highlight]+'m'+words+'\x1b[0m')
  else:
    print('One of the fonts/colors/highlights you entered didnt work, try again.')
def scprint(text,color,highlight,words):
  if text in font_ and color in color_ and highlight in highlight_:
    for x in words:
      print ('\x1b['+font_[text]+';'+color_[color]+highlight_[highlight]+'m'+x+'\x1b[0m', end='', flush = True)
      sleep (0.05)
  else:
    print('One of the fonts/colors/highlights you entered didnt work, try again.')
print ()
#Weapons---------------------------------------------------------
weapons = ['sword','handaxe','bow','spear','fists']

def sword_stats():
  global attack, counter_attack
  attack = 5
  counter_attack = 10
def handaxe_stats():
  global attack, counter_attack
  attack = 8
  counter_attack = 15
def bow_stats():
  global attack, counter_attack
  attack = 3
  counter_attack = 2
def spear_stats():
  global attack, counter_attack
  attack = 4
  counter_attack = 8
def fists_stats():
  global attack, counter_attack
  attack = 1
  counter_attack = 18

#Main--------------------------------------------------------------
scprint(bold, red, 'p','Battle simulater!')
print()
sleep (0.5)
scprint(bold, white, 'p','What weapon do you want?')
print()
print()
sleep (1)
for x in weapons:
  scprint(bold, 'p', hblue, x)
  print ()
  exec(x+'_stats()')
  sprint (' attack: ')
  cprint(p, red, hred, str(attack))
  sprint (' chance for counter attack: ')
  print (counter_attack/20*100,'%')
  print ()
  sleep (0.5)
# anouncing game and listing choosable weapons

while True:
  sprint ('choose your weapon.')
  chosen_weapon = str(input())
  sprint ('You chose')
  print(chosen_weapon)
  sprint(' is that correct?')
  print ()
  answer_1 = str(input())
  if answer_1 == 'yes':
    break
  elif chosen_weapon != 'sword' or chosen_weapon != 'handaxe' or chosen_weapon != 'bow' or chosen_weapon != 'spear' or chosen_weapon != 'fists':
    sprint('Well you didnt spell that right, try again.')
  else:
    sprint ('Ok, then try again.')
  print ()
sprint('Ok')
print()
sleep (1)
replit.clear
# letting player choose weapon












