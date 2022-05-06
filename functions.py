from quiz import *
taken = 0
def selector(option):
  while option != 0:
    if option == 1:
      quizmgr()
    elif option == 2:
      #credits
      pass
    else:
        print("Invalid option.")
        time.sleep(1)
        print()
def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner("Game Show")
    print()
    print("[1] Play                    [2] Credits")
    print()


#use: question("What is the best animal in the world", "Dogs", "Cats", )


