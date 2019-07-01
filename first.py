import random
possible = ["CUCUMBER","JAVASCRIPT","TANGERINE","EXTRAVAGENT","EMBARK"]
random.shuffle(possible)
answer = list(possible[1])
#print(answer)
display = []
display.extend(answer)
for i in range(len(display)):
	display[i] = "_"
print("Welcome to the hangman game!\n")
print(''.join(display))
print("\n\n\n\n")
count = 0
while count < len(answer):
	guess = input("Please guess a letter: ")
	guess = guess.upper()
	for i in range(len(answer)):
		if answer[i] == guess:
			display[i] = guess
			count+=1
	print(''.join(display))
	print("\n\n\n")
print("You guessed the word!")
print(''.join(display))
