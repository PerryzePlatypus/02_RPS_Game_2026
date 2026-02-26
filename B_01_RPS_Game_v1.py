# Check that users have entered a valid
# option based on a list

# Check that users have entered a valid
# option based on a list
def string_checker(question, valid_ans= ('yes', 'no')):

    error = f"\n\033[95m  [!] Please enter a valid option from the following list: {valid_ans}\033[0m\n"

    while True:
        user_response = input(question).lower()

        for item in valid_ans:
            # Checks if the user response is a word in the list
            if item == user_response:
                return item

            # check if the user response is the as
            # the first letter of an item in the list
            elif user_response == item[0]:
                return item

        print(error)
        print()


def instructions():
    """Prints instructions"""

    print("""
    *** Instructions ***

    To begin, choose the number of rounds ( or play
    infinite mode♾️)

    Then play against a computer💻. You must pick:
    R ( Rock🪨 ), P ( Paper📃 ), S ( Scissors✂️ )

    The rule are as follows:
    - Paper📃 beats Rock🪨
    - Rock🪨 beats Scissors✂️
    - Scissors✂️ beats Paper📃


Good Luck! 🍀
    """)


#checks for an integer more than 0 ( allows <enter>)

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

rps_list = ["rock", "paper", "scissors", "xxx"]


print("🪨Rock🪨 / 📃Paper📃 / ✂️Scissors✂️ Game")
print()

#ask users if they want to see the instruction and display them
#if requested

want_instructions = string_checker("Do you want to see the instructions? ")

if want_instructions == "yes":
    instructions()






# ask user for number of round / infinite

num_rounds = int_check(" How many rounds would you like? Push <enter> for infinite mode:  ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

# game loop starts here
while rounds_played < num_rounds:

    if mode == "infinite":
        rounds_heading = f"\n♾️♾️♾️ ROUND {rounds_played + 1} ( Infinite Mode )♾️♾️♾️"
    else:
        rounds_heading = f"\n🕹️🕹️🕹️ Round {rounds_played + 1} of {num_rounds} 🕹️🕹️🕹️"

    print(rounds_heading)
    print()


    user_choice = string_checker("Choose: ", rps_list)
    print("you chose", user_choice)

    if user_choice == "xxx":
        break

    rounds_played += 1


    # if users are in infinite mode. increase number of rounds
    if mode == "infinite":
        num_rounds += 1





#game loop ends here


# game history / statistic