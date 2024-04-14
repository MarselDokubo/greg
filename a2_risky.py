import random
"""
CP1401 2024-1 Assignment 2
Risky Business
Student Name: Uchenna Emeh
Date started: 12-04-2024
Pseudocode:
function main 
    balance = 1000
    get menu_option,
    while menu_option is not 'Q'
        if menu_option is 'P' and balance > 0
            play()
        else if menu_option is 'D'
            print report 
        else if menu_option is 'I'
            print instructions
        else if menu_option is 'S' 
            print stats
        else
            print error message 
        get menu_option 

function play
     mark = generate random number 
     cons_reward = 25%
     cons_chance = 64
     aggr_reward = 60%
     aggr_chance = 44
     silly_reward = 125%
     silly_chance = 8

    get stake_amount,
    get risk_level, 
    if stake_amount > balance 
        print error message
        get stake_amount  
    if risk_level is 'C'
        if mark < cons_chance 
            stake_amount = stake_amount + cons_reward * stake_amount
            balance = balance + stake_amount
    else if risk_level is 'A'
        if mark < aggr_reward 
            stake_amount = stake_amount + aggr_reward * stake_amount
            balance = balance + stake_amount
    else if risk_level is 'S'
        if mark < silly_reward 
            stake_amount = stake_amount + silly_reward * stake_amount
            balance = balance + stake_amount
    else 
        Invalid input 
        get risk_level    
"""

CONSERVATIVE_RISK_LEVEL = 64
CONSERVATIVE_REWARD = .25
AGGRESSIVE_RISK_LEVEL = 44
AGGRESSIVE_REWARD = .60
SILLY_RISK_LEVEL = 8
SILLY_REWARD = 1.25


def main():
    start_balance = 1000
    current_balance = 1000
    outcomes = []
    print("Welcome to Risky Business")
    option = get_valid_option()
    while option != "Q":
        if option == "P":
            outcome = play(current_balance)
            outcomes.append(outcome)
            current_balance += outcome
        elif option == "I":
            display_instruction()
        elif option == "D":
            if len(outcomes) == 0:
                print("No risks taken yet. Get started...")
            else:
                print("Risk-Reward Results Report:")
                print(f"Starting balance: ${start_balance}")
                print(f"Current balance: ${current_balance}")
        else:
            if len(outcomes) == 0:
                print("No risks means no statistics.")
            else:
                print(f"Best result: ${outcomes[-1]}")
                print(f"Worst result: ${outcomes[0]}")
        option = get_valid_option()
    quit_game()

    
def play(current_balance):
    wager = get_valid_amount(current_balance)
    risk_level = get_valid_level()
    outcome = place_bet(wager)
    if outcome > 0: 
        print(f"You won {outcome}")
    else:
        print(f"You lost {wager}")
    print(f"You staked {wager}")
    return outcome
    # print("\n")

def quit_game():
    print("Game over")

def get_valid_option():
    option = input("(P)lay\n(I)nstructions\n(D)isplay Report\n(S)how Statistics\n(Q)uit\nChoose: ").upper()
    while option != "P" and option != "I" and option != "D" and option != "S" and option != "Q": 
        print("Invalid Choice")
        option = input("(P)lay\n(I)nstructions\n(D)isplay Report\n(S)how Statistics\n(Q)uit\nChoose: ").upper()
    return option

def get_valid_amount(current_balance):
    amount = float(input(f"Enter amount to risk upto {current_balance}: "))
    while 10 >= amount:
        print("Amount must be greater than 10")
        amount = float(input("Enter amount to risk: "))
    if amount > current_balance:
        print(f"Amount must be less than current")
        amount = float(input("Enter amount to risk: "))
    else:
        return amount 
def get_valid_level():
    level = input("C)onservative, A)gressive, S)illy: ").upper()
    while level != "C" and level != "A" and level != "S":
        print("Please choose from the available options.")
        level = input("C)onservative, A)gressive, S)illy: ").upper()
    return level 

def place_bet(wager):
    # odds = random.randint(1,100)
    odds = 0
    if 0 < odds < SILLY_RISK_LEVEL: #falls under silly risk level 
        return  wager * SILLY_REWARD
    elif SILLY_RISK_LEVEL < odds < AGGRESSIVE_RISK_LEVEL: #falls under aggressive risk level 
        return  wager * AGGRESSIVE_REWARD
    elif AGGRESSIVE_RISK_LEVEL< odds < CONSERVATIVE_RISK_LEVEL : #falls under conservative risk level 
        return  wager * CONSERVATIVE_REWARD
    else:
        return -wager
    
def display_instruction():
    print("Risky Business.\n Each turn, you can risk some of your cash to try and win a reward.\n You can choose a risk level: \n - conservative (64% chance for a +25% reward)\n - aggressive (44% chance for a +60% reward)\n - silly (8% chance for a +125% reward)")
    print("If your risk-taking doesn't pay off, you lose the amount you choose to risk.")
    print("Risky Business. You win some. You lose more.")

main()
# play()
# place_bet()