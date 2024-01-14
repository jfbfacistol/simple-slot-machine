import random
import time

MAX_PAYLINES = 3
MAX_BET_AMOUNT = 100
MIN_BET_AMOUNT = 1

ROWS = 3
COLS = 3

# Define symbols and their properties
symbols = {
    "Cherry": {"occurrences": 3, "payout": 5},
    "Orange": {"occurrences": 4, "payout": 4},
    "Bar": {"occurrences": 6, "payout": 3},
    "Seven": {"occurrences": 8, "payout": 2},
    "Wild": {"occurrences": 1, "payout": 10},
    "Star": {"occurrences": 2, "payout": 8},
    "Bell": {"occurrences": 4, "payout": 6}
}

progressive_jackpot = 1000
bonus_round_flag = False
free_spins_count = 0
in_free_spins = False

def get_all_symbols():
    """Get a list of all symbols based on their occurrences."""
    return [symbol for symbol, info in symbols.items() for _ in range(info["occurrences"])]

def get_symbol_payout(symbol):
    """Get the payout value for a specific symbol."""
    return symbols.get(symbol, {}).get("payout", 0)

def validate_input(prompt, validator_func):
    """Handle user input validation."""
    while True:
        user_input = input(prompt)
        if validator_func(user_input):
            return user_input
        else:
            print("Invalid input. Please try again.")

def deposit_or_top_up(balance):
    """Handle player's deposit or top-up."""
    return balance + deposit_amount()

def print_message(message):
    """Print a formatted message."""
    print(message)

def get_slot_machine_spin(rows, cols):
    """Generate a random spin for the slot machine."""
    all_symbols = get_all_symbols()

    columns = []

    for _ in range(cols):
        column = random.sample(all_symbols, rows)
        columns.append(column)

    return columns

def has_enough_balance(balance, total_bet):
    """Check if the player has enough balance to place the bet."""
    return balance >= total_bet

def print_slot_machine(columns):
    """Print the current state of the slot machine."""
    for row in zip(*columns):
        print(" | ".join(row))

def is_free_spins_condition_met(columns):
    """Check if the conditions for triggering free spins are met."""
    return any(column.count("Star") >= 3 for column in zip(*columns))

def get_symbol_payout(symbol):
    """Get the payout value for a specific symbol."""
    return symbols.get(symbol, {}).get("payout", 0)

def main_game():
    """Main loop of the game where the player interacts with the slot machine."""
    global progressive_jackpot, bonus_round_flag, free_spins_count, in_free_spins

    balance = deposit_amount()

    while True:
        if balance == 0:
            print("Your balance is empty.")
            top_up = input("Do you want to top up? (y/n): ").lower()
            if top_up == 'y':
                balance = deposit_or_top_up(balance)
            else:
                print("Exiting the game.")
                break

        print(f"Current balance is ₱{balance}")

        answer = input("Press enter to play (x to quit).")

        if answer == "x":
            break

        balance = spin_slot_machine(balance)

        # Introduce more randomness in the increase of progressive jackpot
        progressive_jackpot += random.randint(20, 100)

    print(f"You left with ₱{balance}")

def deposit_amount():
    """Handle player's deposit amount."""
    return int(validate_input("What amount would you like to deposit? ₱", lambda x: x.isdigit() and int(x) > 0))
 
def get_number_of_paylines():
    """Get the number of paylines to bet on."""
    return int(validate_input(f"Enter the number of paylines to bet on (1-{MAX_PAYLINES})? ", lambda x: x.isdigit() and 1 <= int(x) <= MAX_PAYLINES))

def get_bet_amount():
    """Get the bet amount on each payline."""
    return int(validate_input(f"What amount would you like to bet on each payline? ₱", lambda x: x.isdigit() and MIN_BET_AMOUNT <= int(x) <= MAX_BET_AMOUNT))

def check_winnings(columns, paylines, bet):
    """Check for winning combinations and calculate total winnings."""
    global progressive_jackpot, bonus_round_flag

    total_winnings = 0
    winning_paylines = []

    for line in range(paylines):
        symbol = columns[0][line]

        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            total_winnings += get_symbol_payout(symbol) * bet
            winning_paylines.append(line + 1)

    if bonus_round_flag:
        total_winnings += progressive_jackpot
        bonus_round_flag = False
        progressive_jackpot = 1000

    return total_winnings, winning_paylines

def initiate_free_spins():
    """Initiate the free spins mode."""
    global free_spins_count, in_free_spins, bonus_round_flag
    free_spins_count = random.randint(5, 15)  # Randomize the number of free spins
    in_free_spins = True
    bonus_round_flag = False  # Reset bonus_round_flag when free spins are initiated
    print_message(f"Free Spins Activated! {free_spins_count} free spins remaining.")

def spin_slot_machine(balance):
    """Handle the spinning of the slot machine and manage game logic."""
    global progressive_jackpot, bonus_round_flag, free_spins_count, in_free_spins

    if in_free_spins:
        free_spins_count -= 1
        print_message(f"Free Spin! {free_spins_count} free spins remaining.")
        time.sleep(1)  # Introduce a delay for the spinning effect

        if free_spins_count == 0:
            print_message("End of Free Spins.")
            in_free_spins = False
    else:
        paylines = get_number_of_paylines()

        while True:
            bet = get_bet_amount()
            total_bet = bet * paylines

            if not has_enough_balance(balance, total_bet):
                print_message(f"You do not have enough to bet that amount. Your current balance is: ₱{balance}")
                top_up = input("Do you want to top up? (y/n): ").lower()
                if top_up == 'y':
                    balance = deposit_or_top_up(balance)
                else:
                    print_message("Exiting the game.")
                    return 0
            else:
                break

        print_message(f"You are betting ₱{bet} on {paylines} paylines. Total bet is equal to: ₱{total_bet}")

        # Introduce more randomness in the spinning effect
        print_message("Spinning...")
        time.sleep(random.uniform(1, 3))  # Randomize the spinning effect duration

        # Generate a random spin for the slot machine
        slots = get_slot_machine_spin(ROWS, COLS)
        print_slot_machine(slots)

        if is_free_spins_condition_met(slots):
            initiate_free_spins()
        else:
            winnings, winning_paylines = check_winnings(slots, paylines, bet)
            print_message(f"You won ₱{winnings}.")

            if any(symbol in symbols for column in slots for symbol in column):
                bonus_round_flag = True
                print_message("Bonus Round Activated!")

            print_message(f"You won on paylines:", *winning_paylines)
            print_message(f"Current Jackpot: ₱{progressive_jackpot}")

            balance += (winnings - total_bet)

    return balance

if __name__ == "__main__":
    main_game()
