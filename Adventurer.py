import time


# Sets a timed Delay after each print
def pause_print(message_to_print):

    print(message_to_print)
    time.sleep(2)

def left_path():
    pause_print("you start walking down the path " 
                "and you notice that everything look's the same.")
    pause_print("You start getting bored and wonder of the path.")
    pause_print("after walking for a while you decide to stop "
                "and take a break so you sit down next to a tree.")
    while True:
        look = input("Where would you like to look? Please type 'down' 'left' or 'right' ").lower()
        if "down" in look

# Intro to the game
def Intro():
    pause_print("\n\nWelcome to my text based adventure game!")

# Starts the game when Start is entered
def Game_Start():
    name = input("Type your name below then press ENTER\n")
    pause_print("Hi " + name + "!\n")
    while True:
        
        start = input("When you are ready to Start type 'Start' below then press ENTER To start the game\n").lower()
        
        if "start" in start:
            Game_play()
        else:
            pause_print("I'm sorry I dont understand\n")

# Defines gameplay
def Game_play():
    
    pause_print("You have been stuck inside your house "
                "for way too long.")
    
    pause_print("You go into the wood's to go adventure!")
    
    while True:
        path = input("There are two paths that you can take which "
                    "one do you want to take? Please type 'left' or 'right'")
        
        if "left" in path:
            left_path()
        #elif "right" in path:
            #right_path()
        
# Runs Gameplay
def Run_Code():
    Intro()
    Game_Start()
    Game_play()


# Calls the Run_Code function
Run_Code()
