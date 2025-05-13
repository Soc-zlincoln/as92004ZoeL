"""
DIGI Internal Quiz.
By zoe lincoln
Starting Date:29/04/2025
"""
#variables
def game_play():
  score = 0
  name = input("What's your name?")
  start_game = input("Would you like to play a true or false Māori  colour quiz?")
  question = ["Whero is the Māori word for Red. true or false??", "Kōwhai  is the Māori for Blue. true or false?","Kākāriki is the Māori word for Green. true or false??","Mā Whero is the Māori word for White. true or false??","Pango is the Māori word for Black. true or false?"]
  answer = ["true","false","true","false","true"]
  
  #says hello to the user asking if they want to play a game
  
  if start_game == "yes" :
    print("Great", name,"let's get started!! The way you play is You will be asked if the Māori translation lines up with the english translation of the colour.")
  else:
    print("Ok bye-bye.")
    return
  
  #gives them 5 questions with true or false answers
  for x in range(len(question)):
    user_answer = input(question[x])
  
    if user_answer == answer[x]:
      print("Correct!! Well done.")
      score += 20
    else:
      print("Incorrect!! Remember for next time.")
   
  #farewell the player
  #tells them their score out of 100
  
  print("Good job you did it!!")
  print("You got", score, "out of 100!!")

game_play()
