def welcome():
    print("\nWelcome to our Haiku puzzle extravaganza!")
    
def instructions():
    print("\n" + player1 , ", you must create a haiku poem within the designated time limit.")
    print("\nIf" + player1 , "fails to complete the haiku in time, you will lose a life!")
    print("\nLose 3 lives and it's game over!")

def options():
    b = 0
    #while loop creates avenue to close program
    while b == 0:
        choice = input("Press 1 for easy, 2 for medium, 3 for hard, or 4 to exit: ")
        if choice == "1":
            easy()
        elif choice == "2":
            medium()
        elif choice == "3":
            hard()
        elif choice == "4":
            print("Goodbye")
            b = 1
        else:
            print("Please press 1 for easy, 2 for medium, 3 for hard, or 4 to exit:")
    
def player():
    #establishes player profiles and the creation of usernames
    global player1
    player1 = input("Please enter a username: ").upper()
    print("\nHello, " + player1)
    players = [player1]
    welcome()
    
player()