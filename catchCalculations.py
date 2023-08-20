#now lets try to combine this screen and catcher
import random as r
from collections import deque

arr = deque()
for i in range(10):
  arr.append(["   " for j in range(10)]) 
numbers = [1,2,3,4,5,6,7,8,9,10]

catcher = "|_|" 
catchZone = ["   " for i in range(10)]
score = 0
pos = 0
catchZone[pos] = catcher
holdingNumber = -1
findings = deque()

def movement(pos):
  inp = input()
  if (inp == "a" and catchZone[0] == catcher)  or (inp == "d" and catchZone[-1] == catcher):
    pass 
  elif inp == "a": 
    catchZone[pos] = "   " 
    pos = pos-1
    catchZone[pos] = catcher 
  elif inp == "d": 
    catchZone[pos] = "   " 
    pos = pos+1 
    catchZone[pos] = catcher 
  elif inp == "p": 
    print("game quitting")
    return "ov","er"
  else:
    pass 
  return catchZone,pos 

def display(catchZone,pos,letter,score): 
  l = letter[1:-1] 
  if arr[-1][pos] != "   ": 
    catchZone[pos] = f"|{l}|" 
  for a in range(0,len(arr)-1): 
    # print("   ".join([aaa for aaa in a])) 
    if a==0: 
      print(arr[a],score,findings) 
    else: 
      print(arr[a]) 
    # print("".join(i for i in catchZone)) 
  print(catchZone) 
  catchZone[pos] = "|_|" 

def update(numbers,c,score):
  numbers = numbers[5:] 
  score+=1 
  numbers.append(c) 
  for i in range(4): 
    numbers.append(r.randint(1,c)+r.randint(1,c)) 
    return numbers,score 

for i in range(1,1000): 
  display(catchZone,pos,arr[-1][pos],score) 
  arr.pop() 
  arr.appendleft(["   " for i in range(10)]) 
  x = r.randint(0,9) 
  arr[0][x] =  f" {r.choice(numbers)} " 
  catchZone,pos = movement(pos) 
  
  if catchZone == "ov" and pos == "er": 
    break 
  
  if len(findings) < 2 and arr[-1][pos] != "   ": 
    findings.append(int(arr[-1][pos][1:-1])) 
    continue 
   
  if len(findings) == 2:
    holdingNumber = findings[-1]+findings[-2] 
    findings.append(holdingNumber)
    if holdingNumber > 10:
      numbers,score = update(numbers,findings[0]+findings[1],score) 
    continue 
  
  if len(findings)>2 and arr[-1][pos] != "   " and int(arr[-1][pos][1:-1]) != findings[-1]: 
    print("You chose the wrong number fool GAME OVER") 
    break 

  print(arr[-1][pos]) 
  #suppose we are now supposed to find the findings[-1] number just update the numbers array 
  if arr[-1][pos] != "   " and int(arr[-1][pos][1:-1]) == findings[-1]: 
        a = findings[-1] 
        b = findings[-2] 
        c = a+b 
        findings.append(c) 
        numbers,score = update(numbers,c,score)
      


print(f"Your score is {score}") 
print(f"Your numbers are {findings}")








