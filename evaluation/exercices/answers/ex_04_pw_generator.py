import random
import string


nombre1 = random.choice(range(0, 9))
nombre2 = random.choice(range(0, 9))
nombre3 = random.choice(range(0, 9))
nombre4 = random.choice(range(0, 9))

lettreUpper1 = random.choice(string.ascii_uppercase[0:26])
lettreUpper2 = random.choice(string.ascii_uppercase[0:26])
lettreUpper3 = random.choice(string.ascii_uppercase[0:26])
lettreUpper4 = random.choice(string.ascii_uppercase[0:26])

lettreLower1 = random.choice(string.ascii_lowercase[0:26])
lettreLower2 = random.choice(string.ascii_lowercase[0:26])
lettreLower3 = random.choice(string.ascii_lowercase[0:26])
lettreLower4 = random.choice(string.ascii_lowercase[0:26])

mdp1 = str(nombre1) + lettreUpper1 + lettreLower1
mdp2 = str(nombre2) + lettreUpper2 + lettreLower2
mdp3 = str(nombre3) + lettreUpper3 + lettreLower3
mdp4 = str(nombre4) + lettreUpper4 + lettreLower4

mdp = mdp1 + mdp2 + mdp3 + mdp4
print(mdp)

