# 1/24/23 Made By Jibril 
# expected outPut
# https://en.wikipedia.org/wiki/Intercontinental_ballistic_missile#:~:text=Flight%20phases,-The%20following%20flight&text=reentry%2Fterminal%20phase%20(starting%20at,see%20also%20maneuverable%20reentry%20vehicle. 
<<<<<<< HEAD

# Notes
# Once i get the main game loop working, Start figuring out the balencing and add differnces between the types of projectiles 
#
# For The love of god make sure your flags are accrate 
# 
# Fucking Write Test, Holy shit. Test are imporant 8:44PM 2/1/2023 



import random

=======

import random


>>>>>>> 2b0aec14250883aa936e037596f1b76da1500eda
class projectile: # everything is mesured in Km unless stated otherwise
  def __init__(self, name,totalMoves,currntPos,numberOfProjectile,blastRadius,eta):
    self.totalMoves = totalMoves 
    self.numberOfProjectile = numberOfProjectile
    self.currentPos = currntPos
    self.name = name 
    self.blastRadius = blastRadius 
    self.eta = eta

nukes = []
ICBM =  [] 

<<<<<<< HEAD
def launch_Nuke(nuke):
    def display_info(): 
        print("\nTotalMove = %d" % nuke.totalMoves)       
=======


def lanch_Nuke(): # everything is mesured in Km unless stated otherwise # contains updated version 
    def display_info():
        print("TotalMove = %d" % nuke.totalMoves)       
>>>>>>> 2b0aec14250883aa936e037596f1b76da1500eda
        print("Name = " + nuke.name)
        print("Current Move = %d" % (nuke.eta ))
        print("Total Projectiles = %d" %  (nuke.numberOfProjectile) )  
        print("The Blast Raduis = %d" % (nuke.blastRadius))
        print("Pos = (%d,%d)\n" % (currentPos))

<<<<<<< HEAD
    print("\nLaunched Nuke")
    nuke = projectile("Nuke", 5, (0,0), 1, 5, 0)
    positions = [(0,0),(1150,2000), (2750,4000),(5150,4500),(6700,2000),(7850,30)]   

    for x in range(nuke.eta, nuke.totalMoves, 1): 
        currentPos = positions[x]
        display_info()    
        # test_Player() # For testing purposes 
        player_Picker() # For the real game 
        nuke.eta = x + 1
        if nuke.eta == nuke.totalMoves:
            print("Nuke\nBoom!")
            player_Picker() # For the real game 
           #test_Player() # For testing purposes 
            break 

def launch_ICBM(ICBM):
    def display_info(): 
          print("\nTotalMove = %d" % ICBM.totalMoves)       
          print("Name = " + ICBM.name)
          print("Current Move = %d" % (ICBM.eta ))
          print("Total Projectiles = %d" %  (ICBM.numberOfProjectile) )  
          print("The Blast Raduis = %d" % (ICBM.blastRadius))
          print("Pos = (%d,%d)\n" % (currentPos))

    print("\nLaunched ICBM")
    ICBM = projectile("ICBM", 5, (0,0), 1, 0.5, 0)
    positions = [(0,0),(2500, 850), (4000,1000),(5570,800),(7850,0)]   
=======
               
    print("\nLanched Nuke")
    nuke = projectile("Nuke",5,(0,0),1,5,0)

    while nuke.eta <= 5: 
            if nuke.eta == 0 : 
                currentPos = (0,0) 
                nuke.eta = nuke.eta + 1
                display_info()
                player_Choice()
            elif nuke.eta == 1: 
                currentPos = (1150,2000) 
                nuke.eta = nuke.eta + 1
                display_info()
                player_Choice()

            elif nuke.eta == 2 :
                currentPos = (2750,4000) 
                nuke.eta = nuke.eta + 1
                display_info()
            elif nuke.totalMoves == 3: 
                currentPos = (5150,4500)
                nuke.eta = nuke.eta + 1 
                display_info()
            elif nuke.totalMoves == 4: 
                currentPos = (6700,2000)
                nuke.eta = nuke.eta + 1
                display_info()

            elif nuke.totalMoves == 5:
                currentPos = (7850,30)
                nuke.eta = nuke.eta + 1
                display_info()    

            if nuke.eta >= 5: 
                print("boom")
                break; 
>>>>>>> 2b0aec14250883aa936e037596f1b76da1500eda

    for i, x in enumerate(range(ICBM.eta, ICBM.totalMoves, 1)): 
        currentPos = positions[x]
        display_info(i+1)    
        # test_Player() # For testing purposes 
        player_Picker() # For the real game 
        ICBM.eta = x + 1
        if ICBM.eta == ICBM.totalMoves:
            print("ICBM\nBoom!")
            player_Picker() # For the real game 
        #test_Player() # For testing purposes 
            break


def coin_toss(): # Ran First Starts the Game 
    coin = (random.randint(0,1))
    if coin == 0:
        print("coin_toss\nmove_Counter = 0 ") # Remove Later
        move_Counter = 0 
    else:
        print("coin_toss\nmove_Counter = 1 ") # Remove Later
        move_Counter = 1 
    return move_Counter

<<<<<<< HEAD
move_Counter = coin_toss() 
=======
def player_One_Choice(): # will be the basis For the options a player is given
    exit_test = int(input("playerOneChoice\nenter 0 to fail test Or enter 1 to passtest NUKE: "))
    if exit_test == 1:
        print("Test = true")
        test_output = True
    else:
        print("Test = false")
        test_output = False
    return test_output

def player_Two_Choice(): # will be the basis For the options a player is given
    exit_test = int(input("playerTwoChoice\nenter 0 to fail test Or enter 1 to passtest NUKE: "))
    if exit_test == 1:
        print("Test = true")
        lanch_Nuke()
        test_output = True
    else:
        print("Test = false")
        test_output = False
    return test_output


# is the move system of the game and will also be the games main loop  

move_Counter = 0 

def do_something():
    global move_Counter
    exit_test = int(input("enter 0 to exit Or enter 1 to loop:\n "))
    if exit_test == 1:
        player_Picker()
        test_output = True
    else:
        test_output = False
    return test_output 
>>>>>>> 2b0aec14250883aa936e037596f1b76da1500eda

def player_Picker():
    global move_Counter
    if move_Counter % 2 == 0:
        player_One_Choice()
    else: 
        player_Two_Choice()


def test_Player(): # Remove Later
    global move_Counter
    exit_test = int(input("\nTest_Player_Choice\nEnter 0 to skip\nenter 1 to launch nuke\nenter 2 to launch ICBM\nEnter Option: "))
    if exit_test == 1:
        move_Counter = move_Counter + 1       
        nukes.append(projectile("Nuke", 5, (0,0), 1, 5, 0))
        launch_Nuke(nukes[-1])
    elif exit_test == 2:
        move_Counter = move_Counter + 1       
        ICBM.append(projectile("ICBM", 5, (0,0), 1, 5, 0))
        launch_ICBM(ICBM[-1])
    else:
        move_Counter = move_Counter + 1       
        print("Test = false") 

<<<<<<< HEAD
def player_One_Choice():
    global move_Counter
    exit_test = int(input("\nplayer_One_Choice\nEnter 0 to skip\nenter 1 to launch nuke\nenter 2 to launch ICBM\nEnter Option: "))
    if exit_test == 1:
        move_Counter = move_Counter + 1       
        nukes.append(projectile("Nuke", 5, (0,0), 1, 5, 0))
        launch_Nuke(nukes[-1])
    elif exit_test == 2:
        move_Counter = move_Counter + 1       
        ICBM.append(projectile("ICBM", 5, (0,0), 1, 5, 0))
        launch_Nuke(ICBM[-1])
    else:
        print("player_One_Choice\nMove Was skipped") # Remove Later
        move_Counter = move_Counter + 1       

def player_Two_Choice():
    global move_Counter
    exit_test = int(input("\nplayer_One_Choice\nEnter 0 to skip\nenter 1 to launch nuke\nenter 2 to launch ICBM\nEnter Option: "))
    if exit_test == 1:
        move_Counter = move_Counter + 1       
        nukes.append(projectile("Nuke", 5, (0,0), 1, 5, 0))
        launch_Nuke(nukes[-1])
    elif exit_test == 2:
        move_Counter = move_Counter + 1       
        ICBM.append(projectile("ICBM", 5, (0,0), 1, 5, 0))
        launch_Nuke(ICBM[-1])
    else:
        print("player_One_Choice\nMove Was skipped") # Remove Later
        move_Counter = move_Counter + 1       

# is the move system of the game and will also be the games main loop  


=======
>>>>>>> 2b0aec14250883aa936e037596f1b76da1500eda
do = True # on and off switch for game loop
while do == True:
    if player_Picker() == False:
        #Instead of Breaking Send to Another Function Or Break To Close program
        print("\nExiting\n")
        break; 
    else: 
<<<<<<< HEAD
        player_Picker()
        print("Not Exiting\n")
=======
        move_Counter = move_Counter + 1
        print(move_Counter)
        player_Choice()
        print("\nNot Exiting\n")

>>>>>>> 2b0aec14250883aa936e037596f1b76da1500eda
