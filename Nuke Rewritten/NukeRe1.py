# 1/24/23 Made By Jibril 
# expected outPut
# https://en.wikipedia.org/wiki/Intercontinental_ballistic_missile#:~:text=Flight%20phases,-The%20following%20flight&text=reentry%2Fterminal%20phase%20(starting%20at,see%20also%20maneuverable%20reentry%20vehicle. 
# https://www.123calculus.com/en/two-circles-calculator-page-7-60-400.html
# Notes
# Once i get the main game loop working, Start figuring out the balencing and add differnces between the types of projectiles 
#
# For The love of god make sure your flags are accrate 
# 
# Fucking Write Test, Holy shit. Test are imporant. 
# Date Of THE Incident 8:44PM 2/1/2023 
#
# Set_Countrys at the begainnig of the game implemting Coin_Toss to randmoize it 
# Add A pouplation Funtion 
#
import random
import math
from math import acos, sqrt

nukes = []
ICBM =  [] 
Locations = ["Capital", "Industry","Radar", "MissleDefense"]
country_picked = False
player_Country = ""

class projectile: # everything is mesured in Km unless stated otherwise
  def __init__(self, name, totalMoves, currntPos,endPos, numberOfProjectile, blastRadius, eta, owner):
    self.totalMoves = totalMoves 
    self.numberOfProjectile = numberOfProjectile
    self.currentPos = currntPos
    self.endPos = endPos

    self.name = name 
    self.blastRadius = blastRadius 
    self.eta = eta
    self.owner = owner

class Country:
    def __init__(self, name, population, location ):
        self.name = name
        self.population = population
        self.location = location
 
class Capital(Country):
    def __init__(self, name, population, location,radiusOfPeople):
        self.name = name
        self.population = population
        self.location = location
        self.radiusOfPeople = radiusOfPeople

class Industry(Country):
    def __init__(self, name, workers, location ,radiusOfPeople):
        self.workers = workers
        self.location = location
        self.name = name
        self.radiusOfPeople = radiusOfPeople

class Radar(Country):
    def __init__(self, name, workers,location, radiusOfAffect,radiusOfPeople):
        self.workers = workers
        self.location = location
        self.name = name
        self.radiusOfAffect = radiusOfAffect
        self.radiusOfPeople = radiusOfPeople

class MissleDefenseSystem(Country):
    def __init__(self, name, workers,location, radiusOfAffect,radiusOfPeople):
        self.workers = workers
        self.location = location
        self.name = name
        self.radiusOfAffect = radiusOfAffect
        self.radiusOfPeople = radiusOfPeople

def set_cuba():
    def display_info():
        print("\ndisplay_info")
        print("Country name:", cuba.name,"\nCountry population:", cuba.population,"\nCountry location:", cuba.location)
        print("\nCapital name:", havana.name,"\nCapital population:", havana.population,"\nCapital location:", havana.location)
        print("\nFactory name:", factory.name,"\nfactory workers:", factory.workers,"\nfactory location:", factory.location)
        print("\nRadar name:", radar.name,"\nradar workers:", radar.workers,"\nradar location:", radar.location)
        print("\nmissleDefense name:", missleDefense.name,"\nmissleDefense workers:", missleDefense.workers, "location:", radar.location)

    for x in range(0, 4, 1):
  
        location = (500,0,500)
        # Xcords = int(input("\nset_cuba\nEnter X Cords For %s: " % Locations[x]))
        # while Xcords > 500:
        #     Xcords = int(input("X Cords Cannot be greater than 500, Enter X Cords Again: "))
        # Ycords = int(input("Enter Y Cords For %s: " % Locations[x]))
        # while Ycords > 500:
        #     Ycords = int(input("Y Cords Cannot be greater than 500, Enter Y Cords Again: "))
        global cuba,havana,factory,radar,missleDefense
        cuba = Country('cuba', 60000, location)
        if Locations[x] == "Capital":
            havana  = Capital('Havana', 60000, location,15)
        elif Locations[x] == "Industry":
            factory = Industry("Bomb Factory", 5000, location,2)
        elif Locations[x] == "Radar":
            radar = Radar("Radar", 5000,location, 50,2)
        elif Locations[x] == "MissleDefense":
            missleDefense = MissleDefenseSystem("MissleDefense", 2000,location, 25,2)  
            display_info() 

def set_america():
    def display_info():
        print("\ndisplay_info")
        print("Country name:", america.name,"\nCountry population:", america.population,"\nCountry location:", america.location)
        print("\nCapital name:", washington.name,"\nCapital population:", washington.population,"\nCapital  location:", washington.location)
        print("\nFactory name:", factory.name,"\nfactory workers:", factory.workers,"\nfactory location:", washington.location)
        print("\nRadar name:", radar.name,"\nradar workers:", radar.workers,"\nradar location:", radar.location)
        print("\nmissleDefense name:", missleDefense.name,"\nmissleDefense workers:", missleDefense.workers,"\nmissleDefense location:", radar.location)
    for x in range(0, 4, 1):
        
        location = (5150,0,4500)
        # Xcords = int(input("\nset_set_america\nEnter X Cords For %s: " % Locations[x]))
        # while Xcords > 500:
        #     Xcords = int(input("X Cords Cannot be greater than 500, Enter X Cords Again: "))
        # Ycords = int(input("Enter Y Cords For %s: " % Locations[x]))
        # while Ycords > 500:
        #     Ycords = int(input("Y Cords Cannot be greater than 500, Enter Y Cords Again: "))
        # Ycords = int(input("Y Cords Cannot be greater than 500, Enter Y Cords Again: "))
        global america,washington,factory,radar,missleDefense
        america = Country('USA', 60000, location)
        if Locations[x] == "Capital":
            washington = Capital('washington', 60000, location,15)
        elif Locations[x] == "Industry":
            factory = Industry("Bomb Factory", 5000, location,2)
        elif Locations[x] == "Radar":
            radar = Radar("Radar", 5000, location, 50, 1)
        elif Locations[x] == "MissleDefense":
            missleDefense = MissleDefenseSystem("MissleDefense", 2000, location, 25, 2)  
            display_info()
            
def display_cuba(): 
    print("\ndisplay_info")
    print("Country name:", cuba.name,"\nCountry population:", cuba.population,"\nCountry location:", cuba.location)
    print("\nCapital name:", havana.name,"\nCapital population:", havana.population,"\nCapital location:", havana.location)
    print("\nFactory name:", factory.name,"\nfactory workers:", factory.workers,"\nfactory location:", factory.location)
    print("\nRadar name:", radar.name,"\nradar workers:", radar.workers,"\nradar location:", radar.location)
    print("\nmissleDefense name:", missleDefense.name,"\nmissleDefense workers:", missleDefense.workers, "location:", radar.location)

def display_america(): 
    print("\ndisplay_america")
    print("Country name:", america.name,"\nCountry population:", america.population,"\nCountry location:", america.location)
    print("\nCapital name:", washington.name,"\nCapital population:", washington.population,"\nCapital  location:", washington.location)
    print("\nFactory name:", factory.name,"\nfactory workers:", factory.workers,"\nfactory location:", washington.location)
    print("\nRadar name:", radar.name,"\nradar workers:", radar.workers,"\nradar location:", radar.location)
    print("\nmissleDefense name:", missleDefense.name,"\nmissleDefense workers:", missleDefense.workers,"\nmissleDefense location:", missleDefense.location)

def parametricEqu(startPos, endPos, angle):
    x0, y0, z0 = startPos
    x1, y1, z1 = endPos
    # calculates the initial velocity and angle(Radiens) Dont feel like converting to degrees 
    vx = math.sqrt((x1 - x0) * 9.81 / (2 * math.sin(math.pi / angle))) 
    vy = vx * math.sin(math.pi / angle)

    # calculate time of flight
    t = (x1 - x0) / vx

    # calculate y coordinates for each time step
    steps = 4  # number of time steps
    dt = t / steps
    y_coords = []
    z_coords = []
    traj_coords = []
    for i in range(steps + 1):
        t_i = i * dt
        y = y0 + vy * t_i - 0.5 * 9.81 * t_i ** 2
        y_coords.append(y)
        z = z0 + (z1 - z0) * t_i / t
        z_coords.append(z)

        # store current (x, y, z) coordinates in traj_coords array
        x = x0 + i * (x1 - x0) / steps
        traj_coords.append((round(x, 2), round(y, 2), round(z, 2)))

    return traj_coords

def launch_Nuke(nuke, owner,startPos, endPos,angle):
    def display_info(): 
        print("\nTotalMove = %d" % nuke.totalMoves)       
        print("Name = " + nuke.name)
        print("Current Move = %d" % (nuke.eta ))
        print("Total Projectiles = %d" %  (nuke.numberOfProjectile) )  
        print("The Blast Raduis = %d" % (nuke.blastRadius))
        print("Pos = (%d,%d,%d)" % (nuke.currentPos))
        print("endPos = (%d,%d,%d)" % (nuke.endPos))
        print("Owner = " + nuke.owner)
        print("\n")

    print("\nLaunched Nuke")
    
    nuke = projectile("Nuke", 5, (0,0,0),(endPos), 1, 5, 0,owner)
    positions = parametricEqu(startPos, endPos,angle)
    for x in range(0,5,1):
        print(positions[x])

    for x in range(nuke.eta, nuke.totalMoves, 1): 
        nuke.currentPos = positions[x]
        display_info()    
        # test_Player() # For testing purposes 
        player_Picker() # For the real game 
        nuke.eta = x + 1
        if nuke.eta == nuke.totalMoves:
            print("Nuke\nBoom!")       
            check_Projectile_Collision(nuke, radar)
            player_Picker() # For the real game 
           #test_Player() # For testing purposes 
            break 

def launch_ICBM(ICBM, owner):
    def display_info(): 
          print("\nTotalMove = %d" % ICBM.totalMoves)       
          print("Name = " + ICBM.name)
          print("Current Move = %d" % (ICBM.eta ))
          print("Total Projectiles = %d" %  (ICBM.numberOfProjectile) )  
          print("The Blast Raduis = %d" % (ICBM.blastRadius))
          print("Pos = (%d,%d)" % (currentPos))
          print("Owner = " + ICBM.owner)
          print("\n")
    print("\nLaunched ICBM")
    ICBM = projectile("ICBM", 5, (0,0), 1, 0.5, 0,owner)
    positions = [(0,0),(2500, 850), (4000,1000),(5570,800),(7850,0)]   

    for x in (range(ICBM.eta, ICBM.totalMoves, 1)): 
        currentPos = positions[x]
        display_info()    
        # test_Player() # For testing purposes 
        player_Picker() # For the real game 
        ICBM.eta = x + 1
        if ICBM.eta == ICBM.totalMoves:
            print("ICBM\nBoom!")
            player_Picker() # For the real game 
        #test_Player() # For testing purposes 
            break

def intersection_area(d,r1,r2): # finds the area of the intersection of two circles, d = distance between center1 -> r1 and center2 -> r2 = r1 = raduis1 r2 = raduis2   
    d1 = (r1**2 - r2**2 + d**2) / (2 * d)
    d2 = d - d1
    area = (r1**2 * acos(d1/r1) - d1 * sqrt(r1**2 - d1**2)) + (r2**2 * acos(d2/r2) - d2 * sqrt(r2**2 - d2**2))
    return round(area ,2) ,d1 ,d2

def circle_area(r): # finds the area of a circle,  r = raduis  
    area = 3.14 * r**2
    return area 

def check_Projectile_Collision(nuke, radar ):
    if (nuke.currentPos >= radar.location):
        print("Location {} was hit".format(radar.name))
    else:                                                                  
        print("Location {} was not hit".format(radar.name))       


def coin_toss(): # Ran First Starts the Game, and is a 50 50 shot wether playerOne or playerTwo will be ran 
    coin = (random.randint(0,1))
    if coin == 0:
        print("coin_toss\nmove_Counter = 0 ") # Remove Later
        move_Counter = 0 
    else:
        print("coin_toss\nmove_Counter = 1 ") # Remove Later
        move_Counter = 1 
    return move_Counter

move_Counter = coin_toss() 

def player_Picker(): # ran everytime and will choose the player based off a counter 
    global move_Counter, country_picked
    if move_Counter % 2 == 0:
        if not country_picked:
            country_Picker()
            country_picked = True
        player_One_Choice()
    else:
        player_Two_Choice()
        
def player_One_Stats(): # displays the stats of playerOne  
    if player_Country == "cuba":
        print("\nplayer_One_Stats\nplayerOne is cuba") 
        display_cuba()
    else:
        print("\nplayer_One_Stats\nplayerOne is america") 
        display_america()

def player_Two_Stats(): # displays the stats of playerTwo  
    if player_Country == "cuba":
        print("\nplayer_Two_Stats\nplayerOne is america") 
        display_america()
    else:
        print("\nplayer_Two_Stats\nplayerTwo is cuba") 
        display_cuba()

def country_Picker(): # Gives the player a choice on what country, player is selceted off the decsion of coin toss 
    global country_picked, player_Country
    if not country_picked:
        if coin_toss() == True: 
            print("\ncountry_Picker\nplayerOne goes first")
            player_choice = int(input("Enter 0 for Cuba\nEnter 1 for America:\nEnter Option: "))
            if player_choice == 0: 
                print("\nplayerOne is now cuba")
                set_cuba()
                print("playerTwo is now america")
                set_america()
                player_Country = "cuba" 
            else: 
                print("\nplayerOne is now america")
                set_america()
                print("playerTwo is now cuba")
                set_cuba()
                player_Country = "america" 
        else: 
            print("\ncountry_Picker\nplayerTwo goes first")
            player_choice = int(input("Enter 0 for Cuba\nEnter 1 for America:\nEnter Option: "))
            if player_choice == 0: 
                print("playerTwo is now cuba")
                set_cuba()
                print("playerOne is now america")
                set_america()
                player_Country = "cuba" 
            else: 
                print("playerTwo is now america")
                set_america()
                print("playerOne is now cuba")
                set_cuba()
                player_Country = "america" 
        country_picked = True

def player_One_Choice(): # choices playerOne can make 
    owner = "player_One"
    global move_Counter 
    exit_test = int(input("\nplayer_One_Choice\nEnter 0 to skip\nenter 1 to launch nuke\nenter 2 to launch ICBM\nEnter 3 to view country info\n Enter Option: "))
    if exit_test == 1:
        move_Counter = move_Counter + 1       
        nukes.append(projectile("Nuke", 5, (0,0,0),(5000,0,5000),1, 5, 0,owner))
        launch_Nuke(nukes[-1],owner,(0,0,0),(5000,0,5000),2.09)
    elif exit_test == 2:
        move_Counter = move_Counter + 1       
        ICBM.append(projectile("ICBM", 5, (0,0), 1, 5, 0,owner))
        launch_ICBM(ICBM[-1],owner)
    elif exit_test == 3: 
        player_One_Stats() 
    else:
        print("player_One_Choice\nMove Was skipped") # Remove Later
        move_Counter = move_Counter + 1     

def player_Two_Choice(): # choices playerTwo can make 
    owner = "player_Two"
    global move_Counter
    exit_test = int(input("\nplayer_Two_Choice\nEnter 0 to skip\nenter 1 to launch nuke\nenter 2 to launch ICBM\nEnter 3 to view country info\n Enter Option: "))
    if exit_test == 1:
        move_Counter = move_Counter + 1       
        nukes.append(projectile("Nuke", 5, (0,0), 1, 5, 0,owner))
        launch_Nuke(nukes[-1],owner)
    elif exit_test == 2:
        move_Counter = move_Counter + 1       
        ICBM.append(projectile("ICBM", 5, (0,0), 1, 5, 0,owner))
        launch_ICBM(ICBM[-1],owner)   
    elif exit_test == 3: 
        player_Two_Stats()    
    else:
        print("player_Two_Choice\nMove Was skipped") # Remove Later
        move_Counter = move_Counter + 1      


# is the move system of the game and will also be the games main loop 
do = True # on and off switch for game loop
while do == True:
    if player_Picker() == False:
        #Instead of Breaking Send to Another Function Or Break To Close program
        print("\nExiting\n")
        break; 
    else: 
        player_Picker()
        print("Not Exiting\n")
