import random
import replit
import time


def Cut(deck,P_hand,Tab):
  
  while True:
    i= input("Choose a numeber 1..40: ")
    if(i.isdecimal()):
      i=int(i)
      if(i in range(1,41)):
        break
        

  print(deck[i-1])

  while True:
    K=input("Do you want to keep it?  1: Yes  2: No ")
    if((K=="1")or(K=="2")):
      break

  if(K=="1"):
    P_hand.append(deck[i-1])
    del deck[i-1]
    return "P"

  else:
    print("As you like.")
    Tab.append(deck[i-1])
    del deck[i-1]
    return "T"

def Give(deck,n):
  L=deck[0:n]
  del deck[0:n]
  return L
  
def Nb_Dineri(deck):
  Nb=0
  for x in deck:
    if(x[0]=="♦"):
      Nb+=1

  return Nb

def Nb_7(deck):
  Nb=0
  for x in deck:
    if(x[2]=="7"):
      Nb+=1

  return Nb

def Nb_6(deck):
  Nb=0
  for x in deck:
    if(x[2]=="6"):
      Nb+=1

  return Nb

def Score(deck):
  S=0
  if (len(deck)>20):
    S+=1
  if ("♦-7-♦" in deck): 
    S+=1
  if(Nb_7(deck)>2):
    S+=1
  if((Nb_7(deck)==2)and(Nb_6(deck)>2)):
    S+=1
  if(Nb_Dineri(deck)>5):
    S+=1


  return S  

def Card_Num(C):
  return int(C[2:-2])

def Sum_Table(Tab):
  S=0
  for i in Tab:
    S+=Card_Num(i)

  return S
  
def Find_Card(C,Tab):
  for T in Tab:
    if(Card_Num(T)==Card_Num(C)):
      return Tab.index(T)

  return -1

def By2(C,Tab):
  L=[]
  LX=[]

  for i in range(len(Tab)-1):
    for j in range(i+1,len(Tab)):
      if(Card_Num(Tab[i])+Card_Num(Tab[j])==Card_Num(C)):
        L.append(2)
        L.append(Tab[i])
        L.append(Tab[j])
        L.append(i)
        L.append(j)
        LX.append(L)
        L=[]

  return LX

def By3(C,Tab):
  L=[]
  LX=[]

  for i in range(len(Tab)-2):
    for j in range(i+1,len(Tab)-1):
      for k in range(j+1,len(Tab)):
        if(Card_Num(Tab[i])+Card_Num(Tab[j])+Card_Num(Tab[k])==Card_Num(C)):
          L.append(3)
          L.append(Tab[i])
          L.append(Tab[j])
          L.append(Tab[k])
          L.append(i)
          L.append(j)
          L.append(k)
          LX.append(L)
          L=[]

  return LX

def By4(C,Tab):
  L=[]
  LX=[]

  for i in range(len(Tab)-3):
    for j in range(i+1,len(Tab)-2):
      for k in range(j+1,len(Tab)-1):
        for l in range(k+1,len(Tab)):
          if(Card_Num(Tab[i])+Card_Num(Tab[j])+Card_Num(Tab[k])+Card_Num(Tab[l])==Card_Num(C)):
            L.append(4)
            L.append(Tab[i])
            L.append(Tab[j])
            L.append(Tab[k])
            L.append(Tab[l])
            L.append(i)
            L.append(j)
            L.append(k)
            L.append(l)
            LX.append(L)
            L=[]

  return LX

def Choices(C,Tab):
  L=[]
  if(len(Tab)>4):
    L=By4(C,Tab) + By3(C,Tab) + By2(C,Tab)
  elif(len(Tab)>3):
    L=By3(C,Tab) + By2(C,Tab)
  elif(len(Tab)>2):
    L=By2(C,Tab)

  return L

def Play(i,P_hand,Tab):
  L=[]
  if(Sum_Table(Tab)==Card_Num(P_hand[i])):
    L.append(P_hand[i])
    L += Tab
    del Tab[0:len(Tab)]
    L.append("*")

  elif(Find_Card(P_hand[i],Tab)!=-1):
    L.append(P_hand[i])
    L.append(Tab[Find_Card(P_hand[i],Tab)])
    del Tab[Find_Card(P_hand[i],Tab)]

  elif((Find_Card(P_hand[i],Tab)==-1)and(Choices(P_hand[i],Tab)!=[])):
    L.append(P_hand[i])
    Ch=Choices(P_hand[i],Tab)

    Choice=1
    
    if(len(Ch)>1):
      for h in range(len(Ch)):
        print(h+1,end=": ")
        for m in range(1,Ch[h][0]+1):
          print(Ch[h][m],end="  ")
        print("")
      

      while True:
        Choice=input("what combination do you want to take : ")
        
        if(Choice.isdecimal()):
          Choice=int(Choice)
          if Choice in range(1,len(Ch)+1):
            break

    
    Nb_Card=Ch[Choice-1][0]
    
    diff = 0
    for c in range(1,Nb_Card+1):
      L.append(Ch[Choice-1][c])
      del Tab[Ch[Choice-1][c+Nb_Card]-diff]
      diff += 1

  else:
    Tab.append(P_hand[i])
    
  del P_hand[i]
  return L
