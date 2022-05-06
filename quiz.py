import time,sys
import pyfiglet
import os
#question("Test", "A", "B", "C", "D", "A"
def tp(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
def typingInput(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  value = input()  
  return value
def banner(x):
    banner = banner = pyfiglet.figlet_format(x)
    print(banner)
def question(title, a, b, c, d, answer):
  os.system('cls' if os.name == 'nt' else 'clear')
  
  print()
  print(f'''
  [A] {a}                    [B] {b}
  [C] {c}                  [D] {d}
  ''')
  response = typingInput(" Select an answer! ")
  time.sleep(2)
  if answer == response.upper():
    print("correct!")
    time.sleep(2)

def quizmgr():
  taken = 1
  os.system('cls' if os.name == 'nt' else 'clear')
  tp("* OH BOY!")
  print()
  tp("* I CAN ALREADY TELL IT'S GONNA BE A GREAT SHOW!")
  time.sleep(1.5)
  os.system('cls' if os.name == 'nt' else 'clear')
  tp("* EVERYONE GIVE A BIG HAND FOR OUR WONDERFUL CONTESTANT")
  time.sleep(2)
  os.system('cls' if os.name == 'nt' else 'clear')
  tp("* NEVER PLAYED BEFORE GORGEOUS?")
  time.sleep(2)
  os.system('cls' if os.name == 'nt' else 'clear')
  tp("* NO PROBLEM!")
  print()
  tp("* IT'S SIMPLE!")
  time.sleep(2)
  os.system('cls' if os.name == 'nt' else 'clear')
  tp("* THERE'S ONLY ONE RULE")
  time.sleep(2)
  os.system('cls' if os.name == 'nt' else 'clear')
  tp("* ANSWER CORRECTLY...")
  time.sleep(2)
  os.system('cls' if os.name == 'nt' else 'clear')
  tp("OR YOU DIE...")
  time.sleep(2)
  os.system('cls' if os.name == 'nt' else 'clear')
  question("What's the prize for answering correctly?", "Money", "Mercy", "New car", "More questions", "A")
  os.system('cls' if os.name == 'nt' else 'clear')
  tp("RIGHT! SOUNDS LIKE YOU GET IT!")
  time.sleep(2)
  os.system('cls' if os.name == 'nt' else 'clear')
  question("What's the king's full name?", "Lord Fluffybuns", "Fuzzy Pushover", "Asgore Dreemurr", "Mr. Friendship", "C")
  os.system('cls' if os.name == 'nt' else 'clear')
  
  
  
  