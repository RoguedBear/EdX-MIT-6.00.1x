print("Please think of a number between 0 and 100!")
reply = None

low = 0
high = 100

while reply != 'c':
    guess = round((low + high)/2)
    print("Is your secret number", guess,'?')
    while True:
        reply = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
        if reply in ['h', 'c', 'l']:
            break
        else:
            print("Sorry, I did not understand your input")
            continue

    if reply == 'h':
        high = guess
    else:
        low = guess


print("Game over. Your secret number was:", guess)
