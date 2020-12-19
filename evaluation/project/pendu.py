import random

listWords = []
o = ""

with open('words.txt') as text1:
	line = text1.readline()

	while line:
		listWords.append(line)
		line = text1.readline()

for o in listWords:
  o.split()

solution = random.choice(listWords)
lives = 5
displayWord = ""
Fletter = ""

for l in solution:
  displayWord = displayWord + "_ "

  print(">>> Welcome to Hangman!\n>>> Activez les caps !")
  print(solution)
  


while lives > 0:
  print("\nMot à deviner : ", displayWord)
  guessLetter = input(">>> Guess your letter : ")

  if guessLetter in solution:
    print(solution)
    Fletter = Fletter + guessLetter
    print("Vous avez trouvé la lettre")
    
  else:
    lives -= 1
    print("Incorrect! You have ", lives," guesses...")
    print(solution)
    

  displayWord = ""
  for x in solution:
      if x in Fletter:
          displayWord += x + " "
      else:
          displayWord += "_ "

  if "_" not in displayWord:
      print("Well done !")
      break

