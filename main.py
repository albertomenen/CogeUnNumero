#Number Guessing Game Objectives:

##Escoger un numero random desde el 1 al 100

from random import randint

MODO_FACIL = 10

MODO_DIOS = 5

turns = 0


# Funcion para comparar el numero elegido por el usuario comparado con el elegido por la maquina. 

def check_answer(guess, answer, turns): 
  """La funcion de check answer nos devuelve con return el numero de turns que nos quedan o intentos"""
  if guess > answer:
    print("Muy alto")
    return turns -1
  elif guess < answer:
    print("Muy bajo")
    return turns -1
  else:
    print("Acertaste! la respuesta es {answer} ")

## Hacer que la función elija la dificultad 

def set_difficulty():
  level = input("Elige una dificultad. Teclea 'facil' o 'dificil':")
  if level == "facil":
    return  MODO_FACIL
  else:
    return  MODO_DIOS
  
          
      
def game():
  
  print("Bienvenido al juego de adivina el numero!")
  print("Podrias adivinar en que numero estoy pensando entre el 1 y el 100?")
  answer = randint(1, 100)
  print(f"Psst, la respuesta correcta es {answer}")
  
  turns = set_difficulty()
  
  

  
  guess = 0 
  
  while guess != answer: 
    print(f"Te quedan {turns} intentos")

    # Hacer que el usuario elija el numero
    guess = int(input("Di un número: "))
  
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("Has perdido el juego!")
      # Utilizamos esta función return para hacer que el juego se detenga una vez nos quedamos sin vidas.
      return
    elif guess != answer:
      print("Vuelve a intentarlo")

# Contar el numero de intentos 

    
# llamar a la función de juego.

game()
