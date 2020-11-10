import random
import os
import time
players=0
choice=0
def inputs():
	global players
	try:
		players=int(input("Enter the number of players: "))
		logic()
	except:
		print("Invalid Input\nTry Again")
		inputs()
		
def choices():
	global choice
	try:
		choice=input("Choice: ")
		if(choice != "r" and choice != "q"):
			raise Exception
	except:
		print("Invalid Input\nTry Again")
		choices()

def logic():
	global players
	global choice
	for i in range(1,(players+1)):
		print(">>>>Player",i,"'s turn")
		print("Press 'r' to roll the dice")
		print("Press 'q' to quit")
		choices()
		if(choice=='r'):
			if(i==players):
				print("<<<Rolling the dice>>>")
				time.sleep(4)
				print(">>",random.randint(1,6),"<<")
				print()
				logic()
			else:
				print("<<<Rolling the dice>>>")
				time.sleep(4)
				print(">>",random.randint(1,6),"<<")
				print()
		else:
			os._exit(0)
print("<<<<<<<<<< The Dice >>>>>>>>>>")
inputs()