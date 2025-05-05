"""
DIGI Internal Quiz.
By zoe lincoln
Starting Date:29/04/2025
"""
#variables
score = 0
name = input("What's your name?")
start_game = input("Would you like to play a true or false Maori colour quiz?")

#says hello to the user asking if they want to play a game

if start_game == "yes" :
  print("Great", name,"let's get started!! The way you play is You will be asked if the Maori translastion lines up with the english translastion of the colour.")
else:
  print("Ok bye-bye.")

#gives thems 5 questions with true or false answers
user_answer = input("Whero is the Maori word for Red. True or False?")
if user_answer == "True":
  print("Correct! Whero is the Maori word for Red.")
  score = +20
else:
  print("Incorrect! Try and remember for next time.")

input("Kowhai is the Maori for Blue. True or False?")
if user_answer == "False":
  print("Correct! Kowhai is Maori for Yellow not Blue.")
  score = +20
else:
  print("Incorrect! Kowhai isn't Blue.")

input("Kakariki is the Maori word for Green. True or False?")
if user_answer == "True":
  print("Correct! Kakariki is the Maori word for Green.")
  score = +20
else:
  print("Incorrect! Try and remember for next time.")

 
#farewell the player
#tells them their score out of 100

print("Good job you did it!!")
print("You got", score, "out of 100!!")







