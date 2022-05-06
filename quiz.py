import time,sys
import pyfiglet
import os
from os import environ
username = environ["REPL_OWNER"]
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
def question(title, a, b, c, d, answer, rigged):
  os.system('cls' if os.name == 'nt' else 'clear')
  
  print()
  print(f'''
          {title}
        
  [A] {a}                    [B] {b}
  [C] {c}                  [D] {d}
  ''')
  response = typingInput(" Select an answer! ")
  if rigged:
    print("Correct!")
    time.sleep(2)
  else: 
    if answer == response.upper():
      print("correct!")
      time.sleep(2)
    else:
      death()
def death():
  os.system('cls' if os.name == 'nt' else 'clear')
  banner("GAME OVER")
  tp("You cannot give up just yet...")
  time.sleep(2)
  os.system('cls' if os.name == 'nt' else 'clear')
  banner("GAME OVER")
  tp(f"{username}!")
  print()
  tp("Stay determined!")
  print()
  time.sleep(2)
  quit()
def quizmgr():
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
  question("What's the prize for answering correctly?", "Money", "Mercy", "New car", "More questions", "D", False)
  os.system('cls' if os.name == 'nt' else 'clear')
  tp("RIGHT! SOUNDS LIKE YOU GET IT!")
  time.sleep(2)
  os.system('cls' if os.name == 'nt' else 'clear')
  question("What's the king's full name?", "Lord Fluffybuns", "Fuzzy Pushover", "Asgore Dreemurr", "Mr. Friendship", "C", False)
  os.system('cls' if os.name == 'nt' else 'clear')
  question("What are robots made of?", "Hopes & Dreams","Metal & Magic", "Snips & Snails", "Sugar & Spice", "B", False)
  question("Would you smooch a ghost?", "Heck yeah", "Heck yeah", "Heck yeah", "A", True)
  question("Two trains, Train A, and Train B, simultaneously depart Station A and Station B. Station A, and Station B are 252.5 miles apart from each other. Train A is moving at 124.7 mph towards Station B, and Train B is moving at 253.5 mph towards Station A. If both trains departed at 10:00 AM and it is now 10:08, how much longer until both trains pass each other?", "31.054 minutes", "16.232 minutes", "32.049 minutes", "32.058 minutes", "C", False)
  question("How many letters in the name Mettaton?", "11", "6", "8", "10", "C", False)
  question("Who does Dr. Alphys have a crush on?", "Undyne", "Asgore", "The human", "Don't know", "A", True)
  tp("WELL WELL WELL")
  time.sleep(1.5)
  os.system('cls' if os.name == 'nt' else 'clear') 
  tp("WITH DR. ALPHYS HELPING YOU...")
  time.sleep(1.5)
  tp("THE SHOW HAS NO DRAMATIC TENSION!")
  time.sleep(1.5)
  os.system('cls' if os.name == 'nt' else 'clear') 
  tp("WE CAN'T GO ON LIKE THIS!")
  time.sleep(1.5)
  os.system('cls' if os.name == 'nt' else 'clear') 
  tp("BUT.")
  time.sleep(1.5)
  os.system('cls' if os.name == 'nt' else 'clear') 
  tp("BUT!!")
  time.sleep(1.5)
  os.system('cls' if os.name == 'nt' else 'clear') 
  tp("THIS WAS JUST THE PILOT EPISODE!")
  time.sleep(1.5)
  os.system('cls' if os.name == 'nt' else 'clear') 
  tp("NEXT UP MORE DRAMA!")
  time.sleep(1.5)
  os.system('cls' if os.name == 'nt' else 'clear') 
  tp("MORE ROMANCE!")
  time.sleep(1.5)
  os.system('cls' if os.name == 'nt' else 'clear') 
  tp("MORE BLOODSHED!")
  time.sleep(1.5)
  os.system('cls' if os.name == 'nt' else 'clear')
  tp("UNTIL NEXT TIME DARLINGS!")
  
  
  
  
  