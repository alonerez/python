import random

a = random.randint(1, 9)
cnt = 0
guess = ''
while guess != a:
	guess = int(input("please enter your guess, a number between 1-9: "))
	cnt += 1
	if guess>a:
		print ("Your guess it too high")
	elif guess<a:
		print ("Your guess it too low")
	
print ("You guessed it in " + str(cnt) + " tries, number was " + str(guess))


