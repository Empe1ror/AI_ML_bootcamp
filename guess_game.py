import random as r
random_no = r.randint(1, 100)
total = 0
while True:
    guess = int(input("Guess the between 1 - 100: "))
    total += 1
    if total == 5:
        print("You're unable to guess after 5 trials: ")
        break
    elif guess > random_no:
        print("Guess to high!")
    elif guess < random_no:
        print("Guess to low!")
    else:
        print("Correct Guess")
        print (f"Total no of guess is {total}" )
        break
        