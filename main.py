import cmd
import textwrap
import sys
import os
import time
import random


screen_width = 100

#####  Player Setup  ######
class player:
    def __init__(self):
        self.name = ''
        self.job = ''
        self.hp = 0
        self.mp = 0
        self.status_effects = []
        self.location = 'b1'
        self.gameOver = False

myPlayer = player()


###### Title Screen #######
def title_screen_selections():
    option = input(">")
    if option.lower() == ("play"):
      setup_game() # placeholder  until  written
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print("Please enter a valid command")
        option = input(">")
        if option.lower() == ("play"):
           setup_game()  # placeholder  until  written
        elif option.lower() == ("help"):
          help_menu()
        elif option.lower() == ("quit"):
          sys.exit()



def title_screen():
    os.system('cls')
    print('################################')
    print('# WELCOME TO THE TEXT RPG #')
    print('################################')
    print('             -Play-              ')
    print('             -Help-              ')
    print('             -Quit-              ')
    print('Copyright yomommas  face')

    title_screen_selections()


def help_menu():
    print('##############################')
    print('user up, down, left, right')
    print('good luck have fun')
    title_screen_selections()


###### Game Functionality #####



######  Map ######
ZONENAME =''
DESCRIPTION = 'description'
EXAMINATION = 'examine'
SOLVED = False
UP  = 'up', 'north'
DOWN = 'down',  'south'
LEFT = 'left',  'west'
RIGHT = 'right', 'east'

solved_places = {'a1': False, 'a2':False, 'a3': False, 'a4':False,
                 'b1': False, 'b2':False, 'b3' : False, 'b4':False,
                 'c1': False, 'c2':False, 'c3' : False, 'c4':False,
                 'd1': False, 'd2':False, 'd3' : False, 'd4':False }



zonemap = {
    'a1': {
        ZONENAME: "Town Market",
        DESCRIPTION: 'description',
        EXAMINATION:  'examine',
        SOLVED: False,
        UP: '',
        DOWN: 'b1',
        LEFT: '',
        RIGHT: 'a2'
        # UP : ['up', 'north'],
        # DOWN : ['down', 'south'],
        # LEFT : ['left' , 'west'],
        # RIGHT : ['right', 'east']
     },
    'a2': {
        ZONENAME: "Town Entrance",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: '',
        DOWN: 'b2',
        LEFT: 'a1',
        RIGHT: 'a3'
        # UP : ['up', 'north'],
        # DOWN : ['down', 'south'],
        # LEFT : ['left' , 'west'],
        # RIGHT : ['right', 'east']
    },
    'a3': {
        ZONENAME: "Town Square",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: '',
        DOWN: 'b3',
        LEFT: 'a2',
        RIGHT: 'a4'
        # UP : ['up', 'north'],
        # DOWN : ['down', 'south'],
        # LEFT : ['left' , 'west'],
        # RIGHT : ['right', 'east']
    },
    'a4': {
        ZONENAME: "Town Hall",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: '',
        DOWN: 'b4',
        LEFT: 'a3',
        RIGHT: ''
        # UP : ['up', 'north'],
        # DOWN : ['down', 'south'],
        # LEFT : ['left' , 'west'],
        # RIGHT : ['right', 'east']
    },
    'b1': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'a1',
        DOWN: 'c1',
        LEFT: 'b1',
        RIGHT: 'b3'
        # UP : ['up', 'north'],
        # DOWN : ['down', 'south'],
        # LEFT : ['left' , 'west'],
        # RIGHT : ['right', 'east']
     }
}

def  print_location():
    print('\n' + ('#' * (4 + len(myPlayer.location))))
    print('#  ' + myPlayer.location.upper()  + '#')
    print('# ' + zonemap[myPlayer.location][DESCRIPTION] + ' #')
    print('\n' + ('#' * (4 + len(myPlayer.location))))


def prompt():
    print("\n"  + "==================================")
    print("What would you like to do?")
    action  = input(">")
    acceptable_actions = ['move', 'go',  'travel', 'walk', 'quit','examine',  'inspect', 'interact', 'look']
    while  action.lower() not in acceptable_actions:
        print("Uknown action, try again. \n")
        action = input(">")
    if action.lower() == 'quit':
        sys.exit()
    elif action.lower() in ['move','go', 'travel', 'walk']:
        player_move(action.lower())
    elif action.lower() in ['examine','inspect', 'interact', 'look']:
        player_examine(action.lower())

def player_move(myAction):
    ask = "where would you like to move to? \n"
    dest = input(ask)
    if dest in ['up', 'north']:
        destination =  zonemap[myPlayer.location][UP]
        movement_handler(destination)
    elif dest in ['left', 'west']:
        destination =  zonemap[myPlayer.location][LEFT]
        movement_handler(destination)

    elif dest in ['east', 'right']:
        destination =  zonemap[myPlayer.location][RIGHT]
        movement_handler(destination)

    elif dest in ['south', 'down']:
        destination =  zonemap[myPlayer.location][DOWN]
        movement_handler(destination)

def movement_handler(destination):
    print("\n"  + "You have moved to the " + destination + ".")
    myPlayer.location =  destination


def player_examine(action):
    if zonemap[myPlayer.location][SOLVED]:
        print("You have already exhausted this zone")
    else:
        print("You can trigger puzzle here")


##Game functionality


def main_game_loop():
    while myPlayer.gameOver is False:
        prompt()

def setup_game():
    os.system('cls')


    ##NAME Collecting
    question1 = "Hello, whats your name?"
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name  = input(">")
    myPlayer.name = player_name

    ##JOB Collecting
    question2 = "Hello, what role do you want to play?"
    question2added = "(You can play as a warrior, priest, or mage)"
    for character in question2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in question2added:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    player_job = input(">")
    valid_jobs = ['warrior', 'mage',  'priest']
    myPlayer.job = player_job
    if player_job.lower() in  valid_jobs:
        myPlayer.job = player_job
        print("You are now a " + player_job + "!\n")
    else:
        while player_job.lower() not in valid_jobs:
            player_job = input(">")
            if player_job.lower() in valid_jobs:
                myPlayer.job = player_job
                print("You are now a " + player_job + "! \n")

    ##Health handling
    if myPlayer.job   is 'warrior':
        self.hp = 120
        self.mp = 20
    elif myPlayer.job is  'mage':
        self.hp = 40
        self.mp = 120
    elif myPlayer.job is 'priest':
        self.hp = 60
        self.mp = 60

    ##Introduction
    question3 = "Welcome, " + player_name + "the" + player_job + ".\n"
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(.05)
    player_name = input(">")
    myPlayer.name =  player_name

    speech1 = "Welecome to this fantasy world \n"
    speech2  =  "I hope it greets you well! \n"
    speech3 = "Just make sure you don't get too lost... \n"
    speech4  = "Heheheh... \n"

    for character in speech1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(.03)

    for character in speech2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(.03)

    for character in speech3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(.01)

    for character in speech4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(.02)

    os.system('cls')
    print('###################################')
    print(" Lets start now! ")
    print('###################################')
    main_game_loop()

title_screen()