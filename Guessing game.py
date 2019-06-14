from random import randint
num=randint(1,100)
print('It is a guessing game')
print("you have to guess a number between 1 and 100")
print("As your guess will come closer to the actual number you will be notified WARMER!")
print("As your guess will goes farther to the actual number you will be notified COLDER!")
print("Good luck! Let's start the game")
guess=0
guess_list=[]
var_list=[]
while guess!=num:
    guess=int(input("Guess a number: "))
    guess_list.append(guess)
    if (guess<1 or guess >100):
        print("Out of Bounds! Guess a valid number")
    elif (guess==num):
        print("Hurray! You won.\nCongratulations")
        print(f'You made {len(var_list)+1} Guesses')
    else:
        var_list.append(abs(guess-num))
        if len(var_list)==1:
            if var_list[0]<=10:
                print("WARM!,Try another Guess")
            else:
                print("COLD!,Try another Guess")
        else:
            if var_list[-1] < var_list[-2]:
                print("WARMER!,Try another Guess")
            else:
                print("COLDER!,Try another Guess")
print("Press any key and hit enter to close!")
_=input("")

   