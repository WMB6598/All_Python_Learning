#Magic 8 ball code from Codecademy

#imports the random funciton, used below to generate a random number
import random

name = "Will"
question = "Are cats female dogs?"
answer = ("")
random_number = random.randint(1,9)

#random number = random answer
if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
else:
  answer = "Error"

#if name or question blank, the response is different
if name == (""):
  print("Question: " + question)
elif question == (""):
  print("Please ask a question")
else:
  print(name + " asks " + question)

print("Magic 8 ball's answer is: " + answer)