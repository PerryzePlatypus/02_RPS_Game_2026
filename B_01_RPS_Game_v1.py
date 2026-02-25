# Check that users have entered a valid
# option based on a list
def int_check(question):
#checks if users integer is equal or more than 13

    while True:
        error = "Please enter an integer that is 1 or more | press <enter> to play infinite mode"

        to_check = input(question)

        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
             print(error)


# main routine



# initialise game variable
mode = "regular"
rounds_played = 0


print("ROCK🪨 / PAPER📃 / SCISSORS✂️ GAME")
print()

# instructions



# ask user for number of round / infinite

num_rounds = int_check(" How many rounds would you like? Push <enter> for infinite mode:  ")

if num_rounds == "infinite":
    mode = "infinite"
    print("You chose infinite mode!")
    num_rounds = 5

# game loop starts here
while rounds_played < num_rounds:
    user_choice = input("Choose: ")

    if user_choice == "xxx":
        break

    rounds_played += 1
    print("Rounds Played: ", rounds_played)

    # if users are in infinite mode. increase number of rounds
    if mode == "infinite":
        num_rounds += 1

    print("num rounds: ", num_rounds)



#game loop ends here


# game history / statistic