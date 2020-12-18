lives = 5
solution = "python"
Fletters = ""
displayWord = ""

for i in solution:
  displayWord = displayWord + "_ "

while lives>0:
    print("Guess the word : ", displayWord)
    guessLetter = input("Lettre ? ")
    if guessLetter in solution:
        Fletters = Fletters + guessLetter
        print("Trouvé")
    else:
        lives -= 1
        print("Raté ! ", lives, " chances.")

