x = 1
import random
print ("think of a number between 1 and 100")
print ("you dont need to input it, simply enter yes or no. if the machine did not guess your number correctly, say 'too high' or 'too low'.")
(input())
h = 100
l = 0
while x == 1:
  g = random.randint(l,h)
  print ("is it",g,"?")
  a = (input())
  if a == "yes":
    print ("great!")
    x = 2
  else :
    print ("was i too low or too high?")
    t = (input())
    print()
    if t == "too high":
      h = g-1
    if t == "too low":
      l = g+1
