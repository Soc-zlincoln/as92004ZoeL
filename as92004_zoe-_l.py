"""
DIGI Internal Quiz.
By zoe lincoln
Starting Date:29/04/2025
"""
#variables
score = 0
name = input("What's your name?")
start_game = input("Would you like to play a true or false Maori colour quiz?")
question1 = ["Whero is the Maori word for Red. True or False?", "Kowhai is the Maori for Blue. True or False?","Kakariki is the Maori word for Green. True or False?","Ma Whero is the Maori word for White. True or False?","Pango is the Maori word for Black. True or False?"]
answer = ["True","False","True","False","True"]

#says hello to the user asking if they want to play a game

if start_game == "yes" :
  print("Great", name,"let's get started!! The way you play is You will be asked if the Maori translastion lines up with the english translastion of the colour.")
else:
  print("Ok bye-bye.")

#gives thems 5 questions with true or false answers
for x in question1:
  if x == user_answer:
    break
  print(x)

 
#farewell the player
#tells them their score out of 100

print("Good job you did it!!")
print("You got", score, "out of 100!!")







