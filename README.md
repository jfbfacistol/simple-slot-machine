# Slot Machine Game

Welcome to the Slot Machine Game! This Python program simulates a slot machine where players can bet on multiple paylines, spin the reels, and win exciting prizes. The game includes features such as free spins, bonus rounds, and a progressive jackpot. Enjoy the thrill of the casino right from your terminal!

## Table of Contents

1. [Introduction](#introduction)
2. [Game Overview](#game-overview)
3. [Game Features](#game-features)
4. [How to Play](#how-to-play)
5. [Game Logic](#game-logic)
6. [Functions](#functions)
    - [deposit_amount](#deposit_amount)
    - [get_number_of_paylines](#get_number_of_paylines)
    - [get_bet_amount](#get_bet_amount)
    - [check_winnings](#check_winnings)
    - [initiate_free_spins](#initiate_free_spins)
    - [spin_slot_machine](#spin_slot_machine)
    - [main_game](#main_game)
    - [deposit_or_top_up](#deposit_or_top_up)
    - [print_message](#print_message)
    - [get_slot_machine_spin](#get_slot_machine_spin)
    - [has_enough_balance](#has_enough_balance)
    - [print_slot_machine](#print_slot_machine)
    - [is_free_spins_condition_met](#is_free_spins_condition_met)
    - [get_symbol_payout](#get_symbol_payout)
7. [Future Updates](#future-updates)


## Introduction

The Slot Machine Game is a Python-based console application that brings the excitement of a slot machine to your terminal. It features various symbols with unique properties, free spins, bonus rounds, and a progressive jackpot.

## Game Overview

- **Symbols:** The game includes symbols such as Cherry, Orange, Bar, Seven, Wild, Star, and Bell, each with different occurrences and payout values.
- **Features:** Players can enjoy free spins, bonus rounds, and aim for the progressive jackpot.
- **Balance:** Players start with an initial balance and can choose to top up when needed.

## Game Features

- **Free Spins:** Achieve specific symbol combinations to activate free spins, offering additional opportunities to win.
- **Bonus Round:** Certain symbol combinations trigger a bonus round, providing extra excitement and potential rewards.
- **Progressive Jackpot:** A progressive jackpot grows over time and can be won during specific conditions.

## How to Play

1. **Deposit or Top Up:** Start by depositing an initial amount or topping up your balance during the game.
2. **Spin the Reels:** Press Enter to spin the slot machine reels and wait for the results.
3. **Free Spins and Bonus Rounds:** Watch out for symbol combinations to activate free spins and bonus rounds.
4. **Progressive Jackpot:** Keep an eye on the progressive jackpot, as it can be won during the game.
5. **Quit:** Press 'x' to exit the game at any time.

## Game Logic

The game logic involves generating random spins for the slot machine, checking for winning combinations, and managing features like free spins and bonus rounds. The progressive jackpot adds an element of excitement, and players can strategically place bets on multiple paylines.

## Functions

### deposit_amount

```python
def deposit_amount():
    """Handle player's deposit amount."""
```
### get_number_of_paylines
```python
def get_number_of_paylines():
    """Get the number of paylines to bet on."""
```
### get_bet_amount
```python
def get_bet_amount():
    """Get the bet amount on each payline."""
```
### check_winnings
```python
def check_winnings(columns, paylines, bet):
    """Check for winning combinations and calculate total winnings."""
```
### initiate_free_spins
```python
def initiate_free_spins():
    """Initiate the free spins mode."""
```
### spin_slot_machine
```python
spin_slot_machine(balance):
    """Handle the spinning of the slot machine and manage game logic."""
```
### main_game
```python
def main_game():
    """Main loop of the game where the player interacts with the slot machine."""
```
### deposit_or_top_up
```python
def deposit_or_top_up(balance):
    """Handle player's deposit or top-up."""
```
### print_message
```python
def print_message(message):
    """Print a formatted message."""
```
### get_slot_machine_spin
```python
def get_slot_machine_spin(rows, cols):
    """Generate a random spin for the slot machine."""
```
### has_enough_balance
```python
def has_enough_balance(balance, total_bet):
    """Check if the player has enough balance to place the bet."""
```
### print_slot_machine
```python
def print_slot_machine(columns):
    """Print the current state of the slot machine."""
```
### is_free_spins_condition_met
```python
def is_free_spins_condition_met(columns):
    """Check if the conditions for triggering free spins are met."""
```
### get_symbol_payout
```python
def get_symbol_payout(symbol):
    """Get the payout value for a specific symbol."""
```
## Future Updates
### - Time-locked Specials
### - Mystery Symbols
### - Dynamic Paylines
###
