import random
 
number_to_guess = random.randint(1,100)

while True: 
    try:

        guess = input ('make a guess between 1 and 100: ')
        guess = int (guess) 

    except ValueError:
            print ("Please enter a valid number")



    if guess < number_to_guess:
        print ("Too low! ")


    elif guess > number_to_guess:
        print ("Too High! ")

    else:
        print ("Congratulations! You guessed the number")

