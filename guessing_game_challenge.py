from random import randint
num = randint(1, 100)
print('Welcome to Guessing Game!')
print('Try go guess a number between 1 and 100')
guesses = [0]
while True:
	guess = int(input('Please enter a number: '))
	if guess < 1 or guess > 100:
		print('Your guess is out of range!')
		continue
	elif guess == num:
		print('Congratulations! You guessed the correct number in {} tries'.format(len(guesses)))
		break
	guesses.append(guess)
	if guesses[-2]:
	    if abs(num - guess) < abs(num - guesses[-2]):
	        print('Warmer!')
	    else:
	        print('Colder!')
	else:
	    if abs(num - guess) <= 10:
	        print('Warm!')
	    else:
	        print('Cold')                	
	
