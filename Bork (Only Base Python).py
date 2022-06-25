# #suspishpenguinforlife
# r.snchz was here
# Ṅ̢̻̟̞͙͚͚̮̣͙̺̪̠̤̖̘͈̜̩ͦ̊̒̅̈́̉ͦͤ̒ͮ̂̈́ͯ̕ȍ̴̼̪̼̞͉͎̲͔̠̞͎͍̲̾ͣͩ̂ͮ́͝͝r̴̢̢͈̲͉̮̘͕͙̒ͯͣͭ̎͊ͮ̓ͩͨ̊ͅǫ͔̻͚̣̣̱͓̮̮̠̥̣͔̫͖̳͉͑̒̏̂ͩ͊ͥͯ̓̏̊̽̾̋̑ͯ̎̐̑͜k̵̨̪̪̖̜̬̎̆͊̎ͤ̉͆̽ͦ̈ͩ͛̕ was here

import time
import os
#from alive_progress import alive_bar


def clear_console():
    """Clears the console"""
    os.system('cls')
    return


def wait_for_it(seconds):
    """Adds suspense"""
    for i in range(0, 3):
        time.sleep(1)
        print("\n.")
    time.sleep(seconds)
    return


#def progress_bar(iterations):
 #   """Shows a really cool progress bar"""
  #  with alive_bar(iterations, force_tty=True,
   #                title='Loading...',
    #               length=25,
     #              spinner='twirl',
                   # receipt = True,
                   # receipt_text = 'Success'
      #             ) as bar:
       # for i in range(iterations):
        #    time.sleep(0.005)
         #   bar()
    #return


print("Shoutout to the hamster in the computer powering this program.")
wait_for_it(1)
#progress_bar(3000)
clear_console()

print("S U S P I C O U S   P E N G U I N   \nS T R I K E S   A G A I N !")

for character in " By Ramon and Toma":
    print(character)
wait_for_it(1)
#progress_bar(250)
clear_console()

print(
    "\"Penguins are smarter than humans, we just don't show it off (especially Bork).\" - Me (Bork)"
)
wait_for_it(7)
clear_console()

print(
    "Hello, I am Bork (aka Suspicious Penguin), Bork is Bork. Bork likes borking. Bork is a penguin.\nBork has hit his head many times since we last talked, so Bork will act a little different.\nBork now likes taking your personal dat- I mean speaking in third person, and I love to eat food.\nNo food makes Borks tummy rumble! :("
)
wait_for_it(12)
clear_console()

firstName = input("What is your first name?: ")
lastName = input("What is your last name?: ")

if firstName == "Toma" and lastName == "Brasoveanu":
    print("Hello One Of My Creators!")
    wait_for_it(3)
    clear_console()

elif firstName == "Ramon" and lastName == "Sanchez":
    print("Hello One Of My Creators!")
    wait_for_it(3)
    clear_console()
elif firstName == "ramon" and lastName == "sanchez":
    print("Hello One Of My Creators!")
    wait_for_it(3)
    clear_console()
elif firstName == "toma" and lastName == "brasoveanu":
    print("Hello One Of My Creators!")
    wait_for_it(3)
    clear_console()
  
else:
    print(
        f"\nBork says hello to {firstName} {lastName}. Nice to see you again. Bork hopes we did not get off on the wrong foot in scratch!\n(If you do not remember, Borks name is Bork, and I do in fact like borking.)")
    wait_for_it(9)
    clear_console()

color = input("What is your favorite color?: ")

if color == "blue":
    print(f"Borks feathers are {color}! ")
    wait_for_it(3)
    clear_console()
elif color == "Blue":
    color = color.lower()
    print(f"Borks feathers are {color}!")
    wait_for_it(3)
    clear_console()

elif color == "ASCEND":
    #progress_bar(1000)
    print(f"You have ascended {firstName}...\nBork now respects and worships you and your power.")
    wait_for_it(5)
    firstName = firstName.upper()
    print(f"Mark Borks words, {firstName} WILL PREVAIL!")
    wait_for_it(3)
    clear_console()
    print("Fin...")
    quit()

else:
    print(f"{color} is Borks least favorite color!")
    wait_for_it(3)
    clear_console()
print(
    "\nBork is not very good at dates.\nHonestly, Bork has never used a calender, Bork just hopes it is the right day to go to work or be at home on the weekend.")
wait_for_it(9)
opps = 0
for item in range(0, 3):
    opps = opps + 1
    year = int(input("\nWhat year is it?: "))
    if year == 2022:
        print("\nYes, Bork thinks that is correct. Thanks! \n(Bork still does not think you are smart.)")
        break
    elif year == 0 and opps == 3:
        clear_console()
        print("You rejected humanity and returned to monke")
        wait_for_it(5)
        clear_console()
        print("Fin...")
        quit()
      
    else:
        if opps == 3:
            print("\nAlright, Bork says that's enough! The year is 2022! dum-dum!")
            break
        else:
            print(f"dum, you have {3 - opps} try(s) left!")
wait_for_it(1)
clear_console()

print("Can you guess Borks age?")
opps = 0
for item in range(0, 3):
    opps = opps + 1
    age = int(input("\nEnter a number less than 100!: "))
    if age >= 100:
        print("\nBork said less than 100! Try again!")
    elif age < 0:
        print("\nBork thinks that is impossible! Try again!")
    elif age == 31:
        print(
            f"\nYes you are right. Bork is 31. Bork will be 100 in 69 years. That will be the year {2022 + 69}. Nice job {firstName} for figuring out my age!(again, Bork is not impressed by your intellect.)"
        )
        break
    else:
        if opps == 3:
            print(
                "\nAlright. That's enough! Bork guess's you will never find out! Hehehe..."
            )
            wait_for_it(5)
            break

        elif opps == 2:
            clear_console()
            print("This is Borks hint for you: 00011111. ;)")
        else:
            print(f"Dum! you have {3 - opps} try(s) left")
wait_for_it(5)
clear_console()

print(
    "Sorry Bork trailed off with personal questions, it is now time for the suspico- I mean important questions!")
#progress_bar(1000)
c_address = input("What is your first childhood homes address?: ")
print(f"Bork thinks he lived near {c_address} as a kid!")
ipv6 = input("What is your IPv6 address?: ")
ipv4 = input("What is your IPv4 address?: ")
email = input("What is your personal e-mail address?: ")
address = input("What is your current home address?: ")
maiden = input("What is your mothers maiden name?: ")
print("Bork promises there are only a few more questions!")
social = input("What is your social security number?: ")
credit = input("What is your credit card number,expiration date,\nand security code for that credit card?: ")
elder = input("Are you 65+ years old (Yes/No)?: ")
rela_status = input("Are you in a relationship right now (Yes/No)?: ")
wait_for_it(1)
clear_console()
print("Bork thanks you for your time!")
day = int(input("How would you rate my questions on a scale of 1 - 5?: "))
if day == 5:
    wait_for_it(3)
    clear_console()
    print(
        f"To: theboss@susmail.com, {email}\n{firstName} {lastName}.\n{c_address}.\n{ipv6}.\n{ipv4}.\n{address}.\n{maiden}.\n{social}.\n{credit}.\nIs {firstName} elderly: {elder}.\nIs {firstName} in a relationship: {rela_status}.\n- Bork")
    wait_for_it(1)
    print(
        f"Oh shoot! Bork thinks that message is not supposed to go to you {firstName}, please don't tell my boss! See ya later.")
    wait_for_it(5)
    print("Mark Borks words, PENGUINS WILL PREVAIL!")
    wait_for_it(5)
    clear_console()
    print("Fin...")
    wait_for_it(7)
    clear_console()
    #progress_bar(250)
    # Jeremy made the meat and potatoes of this:
    while True:
        game = input("Want to decrypt or encrypt something (Yes/No)?: ")
        if game == "y":
            secret = input("Enter text to encrypt/decrypt.: ")
            encrypted = ""
            for character in secret:
                char = (ord(character) -
                ord(' ') + 47) % 94
                encrypted = encrypted + chr(char + ord(' '))
            #progress_bar(1000)
            print(encrypted)

        elif game == "yes":
            secret = input("Enter text to encrypt/decrypt.: ")
            encrypted = ""
            for character in secret:
                char = (ord(character) -
                ord(' ') + 47) % 94
                encrypted = encrypted + chr(char + ord(' '))
            #progress_bar(1000)
            print(encrypted)
          
        elif game == "Yes":
            secret = input("Enter text to encrypt/decrypt.: ")
            encrypted = ""
            for character in secret:
                char = (ord(character) -
                ord(' ') + 47) % 94
                encrypted = encrypted + chr(char + ord(' '))
            #progress_bar(1000)
            print(encrypted
                 )
          
        elif game == "Y":
            secret = input("Enter text to encrypt/decrypt.: ")
            encrypted = ""
            for character in secret:
                char = (ord(character) -
                ord(' ') + 47) % 94
                encrypted = encrypted + chr(char + ord(' '))
            #progress_bar(1000)
            print(encrypted)

        else:
            print("Okay!")
            quit()

else:
    print("Bork disagrees! >:( Goodbye!")
# 🐧