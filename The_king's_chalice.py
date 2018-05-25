import replit
from time import sleep
import random
from colorama import Fore
replit.clear()
sleep(0.5)
def spr(wa):
	for hk in wa:
		print( hk, end='', flush=True) ;
		if hk == ".":
			sleep(0.25)
		elif hk == ",":
			sleep(0.2)
		else:
			sleep(0.05)
	print()
#For prying eyes, 0=health, 1= max health possible, 2=attack power, 3=healing abilities, 4=speed, 5=magical abilities
# 0 = health, 1 = max health possible, 2 = attack power, 3 = healing abilities, 4=speed, 5 = magical abilities, 6 = name
pdata = [15,15,5,4,17,1]
eMathew = [25,25,3,2,15,3,"Mathew"]#H-MH-AP-HA-S-MA-name
def btl(data):
	global pdata
	while data[0] > 0:
		#printing health bars
		print("\n"*4)
		#♥ █
		print(str(data[6]+"_"*(data[1]-len(data[6]))+"\n"+data[0]*"█"+"\n"+"¯"*data[1]+"\n"))
		
		print("Rogue"+"_"*(pdata[1]-5)+"\n"+pdata[0]*"█"+"\n"+"¯"*pdata[1]+"\n")
		sleep(0.5)
		
		#player input
		spr("What will you do?\nStrike(1) Curse(2) Heal(3) Run(4)")
		while True:
			paction = input()
			if paction in ['1','2','3','4']: #did you input a valid action?
				break
			else: # did you input a valid action?
				spr("Enter 1, 2, 3, or 4.")
				
		
		if data[4] < pdata[4]: #who goes first, you or the enemy?
			if paction == '1': #did you strike?
				sleep(2)
				if  random.randint(1, (round((pdata[4]/data[4])*10))) > 3: #did you miss?
					dmg = random.randint(round((pdata[2])*0.75),pdata[2])
					spr(str("you struck "+ data[6]+"!"))
					data[0] = data[0]-dmg
				else: # did you miss?
					spr("You missed!")
				sleep(0.5)
			elif paction == "2": #did you Curse
				spr("\nCurse of time (slow the enemy)(1) Curse of poisen(hurt everyturn)(2) or Curse of weakness(weakens the enemy)(3)?")
				while True:
					paction = input()
					if paction in ['1','2','3']: #did you input a valid Curse?
						break
					else: # did you input a valid Curse?
						spr("Enter 1, 2, 3")
				if paction == '1':
					pass
				elif paction == '2':
					pass
				else:
					pass
				print ("WIP")
				sleep(3)
				if paction == '1':
					print ("WIP")
					sleep (3)
				elif paction == '2':
					print ("WIP")
					sleep (3)
				else:
					print ("WIP")
					sleep (3)
			elif paction == "3": # did you heal?
				print ("WIP")
				sleep (3)
			else: #did you run?
				print ("WIP")
				sleep (3)
		else: # who goes first?
			pass
			
			
		replit.clear()
	spr("You won!")
	sleep(1)
	replit.clear()
btl(eMathew)
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

spr("The king's chalice is a text-based RPG. This game is story heavy, just a heads up. Basically when in a battle you have 4 options: Strike, curse, heal, and run. The succes of the option you choose is entirely up to your stats, which you can upgrade by using their respective moves. ")
spr("(Sidenote: The experience might be better if you play some zelda music while playing this, just a suggestion.(https://www.youtube.com/watch?v=4qJ-xEZhGms)")
sleep(2)
replit.clear()
def ipan():
	print("           ___----------___		")
	print("          /                \ 	")
	print("          \---__________---/ 	")
	print("          | 0 0   oo   0 0 | 	")
	print("           \_            _/		") 
	print("             \__      __/			")
	print("                \ || /   			")
	print("                / || \ 				")
	print("               |  ()  | 				")
	print("                \ || /					")
	print("                 ||||					")
	print("          ___---/ || \---___ 	")
	print("         /     / /  \ \     \  ")
	print("         \__________________/  ")
	spr("         The king's Chalice.")
ipan()
sleep(6)
replit.clear()
sleep(4)
spr("Our story begins with 10 year old Rogue, son to the king. He had Royal blood, but his brother was destined to the throne. Rogue had no problems with this, however, he hated his extravegent life. Often, Rogue would dress as a peasent, and sneak off to play with the other children. He knew if his identity was revealed, he wouldnt be treated the same. ")
sleep(1)
replit.clear()
spr("*Rogue wakes up in his bed, and looks out to the kingdom that would soon be his brother's. As he steps out of his room, he sees his gaurd.\n\nRogue: My good knight Mathew, I ask that you leave me be for some time, I wish to be alone.\n\nMathew: Sir Rogue, forgive me, but I cannot leave you alone, what if you were to be attacked? or Kidnapped? or even worse!?! *The gaurd hoisted Rogue onto his shoulders and shouted* MARRIED?\n\n*The gaurd and Rogue giggled and shouted for a while*\n\nRogue: I am serious about the alone time though, Mathew.\n\nMathew: Hm, prove to me that you can protect yourself.*The gaurd hands rogue a sheild and a sword, along with some healing potions.* I do not like this, but it is necessary that I know you will be safe.")
sleep(4)
replit.clear()
print(Fore.RED+"BATTLE START!"+Fore.WHITE)
replit.clear()
btl(eMathew)
























