a="STONE,PAPER,SCISSOR GAME"
print(a.center(240))
print(" ")
import random

def check(comp, user):
  if comp ==user:
    return 0
    
  if(comp == 0 and user ==1):
    return -1
    
  if(comp == 2 and user ==1):
    return -1
    
  if(comp == 0 and user == 2):
    return -1

  return 1
    
  
comp = random.randint(0, 2)
user = int(input("Enter 0 for STONE: \nEnter 1 for PAPER: \nEnter 2 for SCISSOR: \n"))

score = check(comp, user)

print("You: ", user)
print("Computer: ", comp)

if(score == 0):
  print("Hey! Its a draw")
elif (score == -1):
  print("Sorry but You Lose the game")
else:
  print("Congratulations, HEY! You Won the game")  
