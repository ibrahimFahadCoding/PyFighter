# main.py

import random
import time

print("PyFight!") 

print()

pHP = 50
eHP = 50

username = input("Enter your username: ")
print("Hello " + username)

pS = False
eS = False
pP = False
eP = False

print("Player HP: " + str(pHP) + "/50")  
print("Enemy HP: " + str(eHP) + "/50")

pAnswered = False
eAnswered = True
while pHP != 0 or eHP != 0:
  if pAnswered == False and eAnswered == True: 
    print("Here are your options: \n1: Attack\n2: Defend\n3: Heal\n4: Powerup")   
    pC = input("Enter your choice (1-4): ")
    #If attack an he power up and no enemy shield
    if pC == "1" and pP == True and eS == False:
      print("You did a SUPER ATTACK!")
      eD = random.randint(3,7)
      print("You did " + str(eD) + " damage.")
      eHP -= eD
      pP = False
      pAnswered = True
      eAnswered = False
      eS = False
      pS = False
    #player attack and player powerup and enemy sheilde.
    elif pC == "1" and pP == True and eS == True:
      print("You did a SUPER ATTACK!")
      print("The enemy was shielded, so you did less damage with the powerup!")
      eD = random.randint(1,3)
      print("You did " + str(eD) + " damage.")
      pP = False
      pAnswered = True
      eAnswered = False
      eS = False
      pS = False
    #player attack and no enemy shield and no powerup.  
    elif pC == "1" and eS == False and pP == False:
      eD = random.randint(1,5)
      print("You did " + str(eD) + " damage.")
      eHP -= eD 
      pAnswered = True
      eAnswered = False
      eS = False
      pS = False

      print("Player HP: " + str(pHP) + "/50")  
      print("Enemy HP: " + str(eHP) + "/50")
      #player attack and enemy shield and no powerup
    if pC == "1" and eS == True and pP == False:
      print("The enemy is shielded. You did 0 damage.")
      eS = False
      pS = False
    #player shield
    if pC == "2":
      print("You are now shielded!") 
      pS = True
      pAnswered = True
      eAnswered = False
      print("Player HP: " + str(pHP) + "/50")  
      print("Enemy HP: " + str(eHP) + "/50")
    #Heal
    if pC == "3" and pHP == 50:
      print("You have 50 HP!") 
      pAnswered = True
      eAnswered = False
      print("Player HP: " + str(pHP) + "/50")  
      print("Enemy HP: " + str(eHP) + "/50")
      
    if pC == "3" and pHP != 50:
      pG = 56
      
      while pG + pHP > 50:
        pG = random.randint(1,5)
      
      pS = False

       
      print("You Healed! You gained " + str(pG) + " HP") 
      pHP += pG
      pAnswered = True
      eAnswered = False
      print("Player HP: " + str(pHP) + "/50")  
      print("Enemy HP: " + str(eHP) + "/50")
    #telliung that u have powerup
    if pC == "4" and pP == True:
      print("You already have the powerup equipped!")
      
    #set powerup to true
    if pC == "4":
      pP = True
      print("Your damage for next round has increased.")
      pAnswered = True
      eAnswered = False
      eS = False
      pS = False
    #Check who won
    if eHP < 1 and pHP >= 1:
      print("You Win!")
      break
    elif pHP < 1 and eHP >= 1:
      print("The enemy won!")
      break
    else:
      if pHP < 1 and eHP < 1:
        print('Tie!')
        break
  
    

      
      
    
  if eAnswered == False and pAnswered == True:
    time.sleep(1) 
    if eP == False:
      eC = random.randint(1,4)
    else:
      if eP == True:
        eC = 1
    if eC == 1 and eP == True and pS == False:
      print("The enemy did a SUPER ATTACK!")
      pD = random.randint(3,7)
      print("The enemy did " + str(pD) + " damage.")
      pHP -= pD
      eAnswered = True
      pAnswered = False
      eS = False
      pS = False
      eP = False
      print("Player HP: " + str(pHP) + "/50")  
      print("Enemy HP: " + str(eHP) + "/50")
    elif eC == 1 and eP == True and pS == True:
      print("The enemy did a SUPER ATTACK!")
      print("You were shielded, so the enemy did less damage with the powerup!")
      pD = random.randint(1,3)
      print("The enemy did " + str(pD) + " damage.")
      pHP -= pD
      eAnswered = True
      pAnswered = False
      eS = False
      pS = False
      eP = False
      print("Player HP: " + str(pHP) + "/50")  
      print("Enemy HP: " + str(eHP) + "/50")
    elif eC == 1 and pS == False and eP == False:
      pD = random.randint(1,5)
      print("The enemy attacked!")
      print("The enemy did " + str(pD) + " damage.")
      pHP -= pD
      pAnswered = False
      eAnswered = True
      eS = False
      pS = False
      print("Player HP: " + str(pHP) + "/50")  
      print("Enemy HP: " + str(eHP) + "/50")
      
    if eC == 1 and pS == True and pP == False:
      print("The enemy did 0 damage.")
      pAnswered = False
      eAnswered = True
      eS = False 
      pS = False
    if eC == 2:
      eS = True
      print("The enemy is shielded.")
      pAnswered = False
      eAnswered = True
    if eC == 3 and eHP == 50:
      eC = random.randint(1,4)
    if eC == 3:
      eGained = 78
      if eHP == 50:
        eC = random.randint(1,4)
        
      while eGained + eHP > 50:
        eGained = random.randint(1,5)
      print("The enemy Healed! The enemy gained " + str(eGained) + " HP") 
      eHP += eGained 
      pAnswered = False
      eAnswered = True
      print("Player HP: " + str(pHP) + "/50")  
      print("Enemy HP: " + str(eHP) + "/50")
      eS = False
    if eC == 4:
      eP = True
      
      print("The enemy's damage for next round has increased.")
      eAnswered = True
      pAnswered = False
      eS = False
      pS = False
    if eC == 4 and eP == True:
      eC = 1
      

      
  
    
    
    
    
    
