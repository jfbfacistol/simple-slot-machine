# Slot Machine Game

Welcome to the Slot Machine Game! This Python program simulates a simple slot machine where players can bet on multiple lines and spin the reels. The game provides an interactive experience by allowing players to deposit money, choose the number of lines to bet on, and place bets.

## Table of Contents

1. [Game Overview](#game-overview)
2. [Game Logic](#game-logic)
3. [Functions](#functions)
    - [check_winnings](#check_winnings)
    - [get_slot_machine_spin](#get_slot_machine_spin)
    - [print_slot_machine](#print_slot_machine)
    - [deposit](#deposit)
    - [get_number_of_lines](#get_number_of_lines)
    - [get_bet](#get_bet)
    - [spin](#spin)
    - [main](#main)

## Game Overview

The slot machine game allows players to deposit money, place bets on a chosen number of lines, and spin the reels to win or lose money. The game continues until the player decides to quit or runs out of funds.

## Game Logic

The game consists of the following key elements:

- **Symbols and Values:**
    - The slot machine has symbols such as "Cherry," "Orange," "Bar," and "Seven," each associated with specific counts and values.
    - The `symbol_count` and `symbol_value` dictionaries define the count and value for each symbol.

- **Reel Configuration:**
    - The slot machine has a 3x3 reel configuration (ROWS x COLS), where symbols are randomly assigned to each cell.

- **Betting:**
    - Players can choose the number of lines to bet on (up to a maximum of 3) and the bet amount per line.
    - The total bet is calculated by multiplying the bet amount by the number of lines.

- **Spinning:**
    - The game simulates spinning the slot machine, generating a random configuration of symbols for each reel.

- **Winning Calculation:**
    - The `check_winnings` function calculates winnings based on the aligned symbols on the selected lines.
    - Winnings are determined by multiplying the bet amount, the symbol count, and the corresponding symbol value.

- **User Interaction:**
    - Players can deposit money, check their balance, and choose to spin the reels or quit the game.
    - The game prompts users for inputs and provides feedback on the outcomes of each spin.

## Functions


### check_winnings

```python
def check_winnings(columns, lines, bet, values):
    """
    Calculate winnings based on the aligned symbols on selected lines.

    Parameters:
    - columns: List of columns representing the slot machine configuration.
    - lines: Number of lines selected by the player.
    - bet: Bet amount per line.
    - values: Dictionary mapping symbols to their respective values.

    Returns:
    - winnings: Total winnings from the spin.
    - winning_lines: List of line numbers with winning combinations.
    """
```

### get_slot_machine_spin
```python
def get_slot_machine_spin(rows, cols, symbols):
    """
    Generate a random slot machine spin configuration.

    Parameters:
    - rows: Number of rows in the slot machine.
    - cols: Number of columns in the slot machine.
    - symbols: Dictionary mapping symbols to their counts.

    Returns:
    - columns: List of columns representing the slot machine configuration.
    """
```
### print_slot_machine
def print_slot_machine(columns):
    """
    Print the current slot machine configuration.

    Parameters:
    - columns: List of columns representing the slot machine configuration.
    """
### deposit
```python
def deposit():
    """
    Prompt the user to deposit money.

    Returns:
    - amount: Amount deposited by the user.
    """
```
### get_number_of_lines
```python
def get_number_of_lines():
    """
    Prompt the user to enter the number of lines to bet on.

    Returns:
    - lines: Number of lines selected by the user.
    """
```
### get_bet
```python
def get_bet():
    """
    Prompt the user to enter the bet amount per line.

    Returns:
    - amount: Bet amount per line.
    """
```
### spin
```python
def spin(balance):
    """
    Perform a slot machine spin, calculate winnings, and update the player's balance.

    Parameters:
    - balance: Current balance of the player.

    Returns:
    - balance_update: Change in the player's balance after the spin.
    """
```
### main
```python
def main():
    """
    Main function to execute the slot machine game.
    """
```
