primeNumbers = []
happyNumbers = []
NbEnCommun = []


with open('primenumbers.txt') as text1:
	line = text1.readline()
	while line:
		primeNumbers.append(int(line))
		line = text1.readline()


with open('happynumbers.txt') as text2:
	line = text2.readline()
	while line:
		happyNumbers.append(int(line))
		line = text2.readline()


for e in primeNumbers:
	if e in happyNumbers:
		NbEnCommun.append(e)
		
print(NbEnCommun)