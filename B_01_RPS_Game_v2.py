import random


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


# compares user / computer choice and returns
# results (win/lose/tie)

def rps_compare(user, comp):

    # if the user and the computer choice is the same, it's a tie
    if user == comp:
        round_result = "tie"

    elif user == "paper" and comp == "rock":
        round_result = "win"
    elif user == "scissors" and comp == "paper":
        round_result = "win"
    elif user == "rock" and comp == "scissors":
        round_result = "win"


    # if its
    else:
        round_result = "lose"

    return round_result



# main routine



# initialise game variable
mode = "regular"

rounds_played = 0
rounds_tied = 0
rounds_lost = 0

rps_list = ["rock", "paper", "scissors", "xxx"]
game_history = []



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
    print("You chose", user_choice)

    # randomly chooses from the rps list (excluding the exit code
    comp_choice = random.choice(rps_list[:-1])
    print("Computer Chose", comp_choice)

    # if user choice is the exit code it breaks the loop

    if user_choice == "xxx":
        break

    result = rps_compare(user_choice, comp_choice)

    # adjust game lost / game tied counter and add results to game history

    if result == "tie":
        rounds_tied += 1
        feedback = "🪢 It's a TIE! 🪢"
    elif result == "lose":
        rounds_lost += 1
        feedback = "😭😭 YOU LOSE! 😭😭"
    else:
        feedback = "🏆🥇 YOU WON! 🥇🏆"

# set up round feedback and output it user
# add it to the game history list (include the round number)
    round_feedback = f"{user_choice} vs {comp_choice}, {feedback}"
    history_item = f"Round: {rounds_played + 1} - {round_feedback}"

    print(round_feedback)
    game_history.append(history_item)

    rounds_played += 1


    # if users are in infinite mode. increase number of rounds
    if mode == "infinite":
        num_rounds += 1


#game loop ends here

if rounds_played > 0:

    # game history / statistic
    rounds_won = rounds_played - rounds_tied - rounds_lost
    percent_won = rounds_won / rounds_played * 100
    percent_lost = rounds_lost / rounds_played * 100
    percent_tied = 100 - percent_won - percent_lost


    #output game statistic
    print("📊📊📊 GAME STATISTICS 📊📊📊")
    print(f"🥇 Games Won: {percent_won:.2f} \t"
        f"😭 Games Lost: {percent_lost:.2f} \t"
        f"👔 Games Tied: {percent_tied:.2f}"  )

    see_history = string_checker("\nDo you want to see your game history?")
    if see_history == "yes":
        for item in game_history:
            print(item)

    print()
    print("Thanks for playing!!!🦦")

else:
    print()
    print("Chickened out 🤣😂🍗🐔")


