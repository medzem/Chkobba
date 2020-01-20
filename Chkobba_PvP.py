#Note: This game is meant to be ran on "repl.it". Feel free to import it so you can run it yourself. Have Fun ^^

import random
import replit
import time

import Card

def Clear():
  global Total_Score
  global P1_score
  global P2_score
  replit.clear()
  print("Total Score   P1 : ",Total_Score[0]," |  P2 : ",Total_Score[1])
  print("")
  print("P1 Score= ",P1_score)
  print("")
  print("P2 Score= ",P2_score)
  print("")
  print("--------------------------------------------")


CH=["♥-1-♥","♥-2-♥","♥-3-♥","♥-4-♥","♥-5-♥","♥-6-♥","♥-7-♥","♥-8-♥","♥-9-♥","♥-10-♥"]
CD=["♦-1-♦","♦-2-♦","♦-3-♦","♦-4-♦","♦-5-♦","♦-6-♦","♦-7-♦","♦-8-♦","♦-9-♦","♦-10-♦"]
CC=["♣-1-♣","♣-2-♣","♣-3-♣","♣-4-♣","♣-5-♣","♣-6-♣","♣-7-♣","♣-8-♣","♣-9-♣","♣-10-♣"]
CS=["♠-1-♠","♠-2-♠","♠-3-♠","♠-4-♠","♠-5-♠","♠-6-♠","♠-7-♠","♠-8-♠","♠-9-♠","♠-10-♠"]

while True:
  K=input("Choose the final score:  1: |--11--|  2: |--21--| ")
  if((K=="1")or(K=="2")):
    break

if(K=="1"):
  FR=11
else:
  FR=21

Total_Score=[0,0]

while((Total_Score[0]<FR)and(Total_Score[1]<FR)):
  replit.clear()
  C_Total=CH+CD+CC+CS

  P1_hand=[]
  P2_hand=[]
  Table=[]

  P1_score=[]
  P2_score=[]


  R=0
  L_aux=[]
  LE="P1"

  #Begin--------------------------------------------------------------------

  random.shuffle(C_Total)

  print("P2 9oss")
  w=Card.Cut(C_Total,P2_hand,Table)

  if (w=="P"):
    P2_hand += (Card.Give(C_Total,2))
    Table += (Card.Give(C_Total,4))
  else:
    P2_hand += (Card.Give(C_Total,3))
    Table += (Card.Give(C_Total,3))

  P1_hand += (Card.Give(C_Total,3))


  Clear()#---------------------------------------------------------------

  while (R<6): 
    R+=1
    print("Round ",R,": -------------------------------")
    for Round in range(3):
      reveal=input("Player 2, Press Enter to reveal cards...")
      print("P2 Hand: ",P2_hand)
      print("Table: ",Table)
      print("")

      i=1
      if(len(P2_hand)>1):
        while True:
          i= input("Choose a numeber 1..3: ")
          if(i.isdecimal()):
            i=int(i)
            if i in range(1,len(P2_hand)+1):
              break
      
      time.sleep(0.5)
      L_aux = Card.Play(i-1,P2_hand,Table)

      if (( L_aux != [] ) and ( L_aux[-1] == "*")):
        Total_Score[1] += 1
        del L_aux[-1]
      
      if(L_aux != []):
        LE="P2"

      P2_score += L_aux

      Clear()#---------------------------------------------------------------
      reveal=input("Player 1, Press Enter to reveal cards...")
      print("P1 Hand: ",P1_hand)
      print("Table: ",Table)

      i=1
      if(len(P1_hand)>1):
        while True:
          i= input("Choose a numeber 1..3: ")
          if(i.isdecimal()):
            i=int(i)
            if i in range(1,len(P1_hand)+1):
              break
      
      time.sleep(0.5)
      L_aux = Card.Play(i-1,P1_hand,Table)

      if (( L_aux != [] ) and ( L_aux[-1] == "*")):
        Total_Score[0] += 1
        del L_aux[-1]
      
      if(L_aux != []):
        LE="P1"

      P1_score += L_aux

      Clear()#---------------------------------------------------------------
    
    P2_hand += (Card.Give(C_Total,3))
    P1_hand += (Card.Give(C_Total,3))

  if (LE == "P1") :
    P1_score += Table
  elif ( LE == "P2" ):
    P2_score += Table

  Total_Score[0]+= Card.Score(P1_score)
  Total_Score[1]+= Card.Score(P2_score)

  Clear()

  print("Statistics:------------------------")
  print(len(P1_score)," | ",len(P2_score)," : Total Cards")
  print(Card.Nb_Dineri(P1_score)," | ",Card.Nb_Dineri(P2_score)," : Total Dineri Cards")
  print(Card.Nb_7(P1_score)," | ",Card.Nb_7(P2_score)," : Total 7 Cards")

  if(Card.Nb_7(P1_score)==Card.Nb_7(P2_score)):
    print(Card.Nb_6(P1_score)," | ",Card.Nb_6(P2_score)," : Total 6 Cards")

  if ("♦-7-♦" in P1_score): 
    print("Player 1 has ♦-7-♦")
  else:
    print("Player 2 has ♦-7-♦")

  if (Total_Score[0]>Total_Score[1]):
    print("Player 1 Wins")
  else: 
    print("Player 2 Wins")

  again=input("Press Enter to continue...")

if (Total_Score[0]>Total_Score[1]):
  print("The final winner is Player 1")
else: 
  print("The final winner is Player 2")
#---------------------------------------------------------------
