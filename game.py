from random import choice
valid_inputs = ['rock', 'paper', 'scissors', '!exit', '!rating']
winning_dict = {'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'}
rating: int = 0


def search_user_score():
    global rating
    name = input('Enter your name:')
# Search for users score in rating.txt
    scores = open('rating.txt', 'r', encoding="utf-8")
    for line in scores:
        if line.startswith(name):
            rating = int(line.replace('\n', "").split()[1])
            break
    scores.close()
    print(f'Hello, {name}')


def handle_game_options():
    global valid_inputs, winning_dict
    user_options = input()
    print("Okay, let's start")
    
    if user_options:
        valid_inputs = ['!rating', '!exit']
        str_buff = ''
        # Separate words from user input
        for char in user_options:
            if char != ',' or user_options.index(char) == len(user_options) - 1:
                str_buff += char
            else:
                valid_inputs.append(str_buff)
                str_buff = ''

# Calculate which option loose over the others
        for option in valid_inputs:
            index = valid_inputs.index(option)
            working_list = valid_inputs[index + 1:] + valid_inputs[:index]
            half = len(working_list) // 2
        
            winning_dict.update({option: working_list[:half]})
    
    
def main():
    global rating
    search_user_score()
    handle_game_options()
    while True:
        computer_choice = choice(('rock', 'paper', 'scissors'))
        user_input = input()
# Check game final state
        if user_input not in valid_inputs:
            print("Invalid Input")
            continue
        if user_input == computer_choice:
            print(f"There is a draw {computer_choice}")
            rating += 50
        elif user_input == "!exit":
            print("Bye!")
            break
        elif user_input == "!rating":
            print(f"Your rating: {rating}")
        elif computer_choice in winning_dict[user_input]:
            print(f"Sorry, but computer chose {computer_choice}")

        else:
            print(f"Well done. Computer chose {computer_choice} and failed")
            rating += 100


main()
