import sys
import time
import os


def write(s):
    for i in s:
        print(i, end="", flush=True)
        time.sleep(.075)


def beginning():

    write('''
  Hello Adventurer !
  I am your guide , Svaltek,
  what should I call you ?
  ''')

    global username
    username = input("Enter name: ")

    write(f'''
  Warm greetings {username}!
  You don't remember anything, do you ?
  ''')

    prompt1 = input(">")
    print(prompt1.lower)

    if prompt1.lower == "yes":
      write('''
      *Svaltek mutters anxiously, but you hear him*
      
      Maybe I should re-do the ritual,
      he's too dangerous like this
      ''')
    elif prompt1.lower == "no":
      write(f'''
      *Svaltek breathes a sigh of relief*
    
      Well then {username}, we should get you some food!
      What do you fancy , some soup or chicken ?
      ''')
      soup_or_chicken = input(">")
    if soup_or_chicken.lower != "soup" or "chicken":
      write('''
        *Svaltek shouts angrily*
                  
          ANSWER ME ya skinny pillock or I'll CLOBBER ya
          over your thick skull!
            ''')
    else:
      write('''
        *Svaltek grins toothily*
            
        Well jokes on you , we've got neither,
        I've some dried reindeer in my pack,
        you can have a roll.
          ''')
    elif prompt1.lower != "yes" or "no":
      write("Do you remember? YES or NO")
  
  



