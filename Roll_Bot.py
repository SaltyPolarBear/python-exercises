import random
print ("roll bot. format: 1d12")
while True:
	roll = (input("what do you want to roll?: "))
	roll = roll.split("d")
	result = 0
	for x in range(int(roll[0])):
		result+= random.randint(1,(int(roll[1])))
	print (result)
	(input())
