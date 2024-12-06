# a question and answer code

#print("Hello World")
#print("What is your name?") #Ask for their name

#myName= input() #Input Name
#print("It is good to meet you, " + myName)
#print("the length of your name is:")
#print(len(myName))
#print("what is your age?") #Ask for their age
#myAge = input() #Input Age
#print("You will be " + str(int(myAge) + 1) + " in a year")

#name = input()
#age = 25
#if name == 'John':
#    print("Hello, John")
#elif age < 17:
#    print("You are not John, buddy")
#elif age > 25:
#    print("Keep it moving, old man")
#elif age == 25:
#    print("My best friend John!")

#name = ''
#while name != 'your name':
#    print("please type your name.")
#    name = input()
#print("Thank you")

#while True:
#    print("PLease type your name")
#    name = input()
#    if name == 'your name':
#        break #Jumps straight to the end, when the satement is equal
#print("Thank you")

#while True:
#    print("Who are you?")
#    name = input()
#    if name != 'joe':
#        continue #If any other name is used, this function will jump to the start of loop
#    print("Hello, Joe. What is the password?")
#    password = input()
#    if password == 'swordfish':
#        break #Break is used so the while loop doesn't keep repeating and end the loop
#print("Access Granted")


#FIRST ATTEMPT
#while True:
#    print("My name is")
#    name = input()
#    if name != 'jimmy':
#        continue
#        #Goes from 0-4 in a list
#        for i in range (5):
#            print("Hello Jimmy, (" + str(i) + ")")
#        print("Would you like more numbers?")
#        question = input()
#        if question == 'Yes':
#            #Continues from where you left off
#            for x in range (5, 11):
#                print("Here are some more numbers Jimmy! (" + str(x) + ")")
#                break
#print("That's all the numbers we have now!")


#REMODIFIED ATTEMPT
#print("My name is")
#name = input()

#if name == 'jimmy':
    # First loop to print numbers from 0 to 4
#    for i in range(5):
#        print("Hello Jimmy, (" + str(i) + ")")

#    print("Would you like more numbers?")
#    question = input()

#    if question.lower() == 'yes':
        # Continue numbering from where the first loop ended (i.e., 5)
#        for x in range(5, 11):  # This will print numbers from 5 to 10
#            print("Here are some more numbers Jimmy! (" + str(x) + ")")
#    else:
#        print("No more numbers then!")
        
#print("That's all the numbers we have now!")

#total = 0
#for num in range(101): #Loops it 100 times
#    total = total + num
#print(total)

#Using a while loop rather than a for loop
#print ("My name is")
#i = 0
#while i < 5:
#    print("Hello Jimmy, (" + str(i) + ")")
#    i = i + 1

#for i in range (0, 10, 2): #First two are the numbers printed and last one is the interval
#Can even go down with numbers by using (-x)
#    print(i)

#import random #Imports a module (i.e random) and gives unique programs and executions
#for i in range(5):
#    print(random.randint(1, 10))

#print("I am thinking of a number between 1 and 20")

#attempt = 0
#correct_number = 17

#while True:
#    print("Take a guess")
#num = input()

#attempt += 1

#if num == correct_number:
#    print("Good job! You guessed the right number in")
#    break
#else:
#    print("Wrong Answer! Try again.")

#print("I am thinking of a number between 1 and 20")

# Initialize a variable to keep track of the number of attempts
#attempts = 0
#correct_number = 17

#while True:
#    print("Take a guess")
#    num = int(input())  # Convert input to an integer #Keeps asking for a guess

    # Increment the attempt counter
#    attempts += 1

#    if num == correct_number: #checks if 'num' is correct
#        print(f"Good job! You guessed the right number in {attempts} attempts.") #records the amount of attempts it took
#        break  # Exit the loop once the correct number is guessed
#    else:
#        print("Wrong answer! Try again.") #if wrong, it keeps going

#import sys
#import random

#print("ROCK, PAPER, SCISSORS")
#W = 0
#L = 0
#T = 0

#while True:
#    print("Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit")
#    move = input()
#    if move == "q":
#        sys.exit()
#    elif move == "r":
#        print("Rock versus")
#    elif move == "p":
#        print("Paper versus")
#    elif move == "s":
#        print("Scissors versus")

#responses = [
#    "PAPER",
#    "SCISSORS",
#    "ROCK",
#]

#random-reponse == random.choice(responses)
#print(random-response)

#import sys
#import random

#print("ROCK, PAPER, SCISSORS")
#W = 0  # Wins
#L = 0  # Losses
#T = 0  # Ties

# Map player moves for comparison
#moves_map = {"r": "ROCK", "p": "PAPER", "s": "SCISSORS"}

#while True:
    # Ask for player's move
#    print("Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit")
#    player_move = input()

    # If the player wants to quit
#    if player_move == "q":
#        print(f"Final score: {W} Wins, {L} Losses, {T} Ties.") #{} allows for the data to be printed
#        sys.exit()

    # Ensure the player makes a valid move
#    if player_move not in moves_map:
#        print("Invalid move. Please choose 'r', 'p', 's', or 'q' to quit.")
#        continue

    # Print player's move
#    print(f"{moves_map[player_move]} versus...")

    # Randomly choose a response for the computer
#    computer_move = random.choice(["ROCK", "PAPER", "SCISSORS"])
#    print(computer_move)

    # Determine the outcome
#    if moves_map[player_move] == computer_move:
#        print("It's a tie!")
#        T += 1  # Increment tie counter
#    elif (
#        (player_move == "r" and computer_move == "SCISSORS") or
#        (player_move == "p" and computer_move == "ROCK") or
#        (player_move == "s" and computer_move == "PAPER")
#    ):
 #       print("You win!")
  #      W += 1  # Increment win counter
  #  else:
   #     print("You lose!")
   #     L += 1  # Increment loss counter

    # Print current score
#    print(f"{W} Wins, {L} Losses, {T} Ties.")

#spam = 1
#if spam == 1:
#    print("hello")
#    spam = spam + 1
#if spam == 2:
#    print("Howdy")
#else:
#    print("Greetings!")

#for i in range (1, 11):
#    print(i)

#i = 1
#while i < 11:
#    print(i)
#    i = i + 1

