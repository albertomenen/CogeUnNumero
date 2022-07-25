#Number Guessing Game Objectives:

from random import random

numero_jugador = input("Que numero eliges?")

def pick_a_number():

  test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
  numero_elegido= random.choice(test_list)
    
  return(numero_elegido)
  
  def ganador():
    if numero_elegido == numero_jugador:
      print("Tu ganas")
    else:
      print("Tu pierdes")



##pick_a_number()




# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).


