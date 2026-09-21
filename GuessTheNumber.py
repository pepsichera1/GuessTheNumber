import random

#EXIT FROM DEF
class forceExit(Exception):
    pass

def ask(message):
    answer = input(message).strip().lower()
    if answer == 'exit':
        raise forceExit()
    return answer

def guessNumber():
    try:
        while True:
            #PRESENTATION
            exitCommand = "exit"
            randomNumber = 0
            #---------------------
            print('Welcome to Guess The Number! \n You will be guessing!\n')
            print(f'\n If you want to quit just type {exitCommand} when User input is granted.\n')
            #---------------------
            
            #RANGEMIN
            proceed = 0
            while proceed == 0:
                rangeMin = ask('Enter the minimum number to guess\n')
                try:
                    rangeMin = int(rangeMin)
                    proceed += 1
                except ValueError:
                    print('Enter a number\n')
                    continue
            
            #RANGEMAX
            proceed = 0
            while proceed == 0:
                rangeMax = ask('Enter the maximum number to guess\n')
                try:
                    rangeMax = int(rangeMax)
                    if rangeMax <= rangeMin:
                        raise ValueError
                    proceed += 1
                except ValueError:
                    print(f'Please enter a valid number GREATER than {rangeMin}\n')
                    continue
            
            #USER GUESSING
            proceed = 0
            randomNumber = random.randint(rangeMin, rangeMax)
            while proceed == 0:
                userGuess = ask(f'Guess the number between {rangeMin} and {rangeMax}:\n')
                try:
                    userGuess = int(userGuess)
                    if userGuess < rangeMin or userGuess > rangeMax:
                        raise ValueError
                except ValueError:
                    print(f' Please enter a valid number GREATER than {rangeMin} and LESSER than {rangeMax}\n')
                    continue
                if userGuess == randomNumber:
                    print('You did it!\n')
                    proceed = 0
                    while proceed == 0:
                        retry = ask('Play again? y/n \n')
                        if retry == 'y':
                            print('\n')
                            proceed += 1
                            break
                        if retry == 'n':
                            print('Thanks for playing! Come again!')
                            proceed += 1
                            return
                        else:
                            print('Please enter "y" or "n"\n')
                elif userGuess < randomNumber:
                    print('Too low! Try again!\n')
                    continue
                elif userGuess > randomNumber:
                    print('Too high! Try again\n')
            
    except forceExit:
        print('\nYou type exit. Quitting from Function...')
        return

guessNumber()
