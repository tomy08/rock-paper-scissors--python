import random
from colorama import init, Fore, Style

def main():
    user_wins = 0
    computer_wins = 0
    print(Style.BRIGHT + Fore.MAGENTA + "Welcome to Rock, Paper, Scissors!" + Style.RESET_ALL)    
    user_choice, computer_choice = choose_option()
    print("Computer chose: " + computer_choice)
    while True:
        user_wins, computer_wins = check_results(user_choice, computer_choice, user_wins, computer_wins)
        print(Fore.LIGHTMAGENTA_EX + "*" * 20 + Style.RESET_ALL)
        print("You won " + Fore.CYAN + str(user_wins) + " times." + Style.RESET_ALL)
        print("Computer won " + Fore.CYAN + str(computer_wins) + " times." + Style.RESET_ALL)
        print(Fore.YELLOW + "Do you want to play again? (yes/no)" + Style.RESET_ALL)
        play_again = input()
        play_again = play_again.lower()
        if play_again == "no":
            break
        else:
            print(Fore.LIGHTMAGENTA_EX + "*" * 20 + Style.RESET_ALL)
            user_choice, computer_choice = choose_option()
            print("Computer chose: " + computer_choice)

def choose_option():
    options = ("rock", "paper", "scissors")
    print(Fore.GREEN + Style.BRIGHT + "Please enter your choice (rock, paper or scissors):" + Style.RESET_ALL)
    user_choice = input()
    user_choice = user_choice.lower()
    while user_choice not in options:
        user_choice = input()
        user_choice = user_choice.lower()
    computer_choice = random.choice(options)
    return [user_choice, computer_choice]

def check_results(user_choice, computer_choice, user_wins, computer_wins):
    if user_choice == computer_choice:
        print(Fore.YELLOW + "It's a tie!" + Style.RESET_ALL)
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print(Fore.GREEN + "You win!" + Style.RESET_ALL)
        user_wins += 1
    else:
        print(Fore.RED + "You lose!" + Style.RESET_ALL)
        computer_wins += 1
    return [user_wins, computer_wins]

if __name__ == "__main__":
    init()  # Initialize colorama
    main()
