#Number Guessing Game Objectives:


##Escoger un numero random desde el 1 al 100

from random import randint

MODO_FACIL = 10

MODO_DIOS = 5


# Funcion para comparar el numero elegido por el usuario comparado con el elegido por la maquina. 

def check_answer(guess, answer): 
  if guess > answer:
    print("Muy alto")
  elif guess < answer:
    print("Muy bajo")
  else:
    print("Acertaste! la respuesta es {answer} ")

## Hacer que la función elija la dificultad 

def set_difficulty():
  level = input("Elige una dificultad. Teclea 'facil' o 'dificil':")
  if level == "facil":
    return  MODO_FACIL
  else:
    return  MODO_DIOS
  
          
      

print("Bienvenido al juego de adivina el numero!")
print("Podrias adivinar en que numero estoy pensando entre el 1 y el 100?")
answer = randint(1, 100)
print(f"Psst, la respuesta correcta es {answer} ")


turns = set_difficulty()

print(f"Te quedan {turns} intentos")

# Contar el numero de intentos 



# Hacer que el usuario elija el numero

guess = int(input("Di un número: "))


check_answer(guess, answer)

