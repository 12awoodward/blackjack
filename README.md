# Blackjack

In the console, play the non-casino version of Blackjack (also known as Crazy 8's, Switch, Take 2, etc).

## About

### What is non-casino Blackjack?

It is a card game similar to Uno, played with a standard deck of cards. Some cards can have certain effects when played. There are a number of different versions of this game with different rules for the card effects.

By default the card effects for this game will be:

- Ace: Allows  the player to change the suit to their choice
- 2: Next player must pickup two or play another pickup card to add to the count for the next player
- 8: Next players turn is skipped
- Jack:
    - Black Jacks: Pickup 5
    - Red Jacks: Cancel pickups
- Queen: Change direction of play

### Features

This project will allow you to play Blackjack in the CLI against a number of Computer opponents. It will also include the ability to set different rules to change the card effects.

## Installation

### Requirements

- knowledge of CLI usage
- Python3

### Setup

1. Clone the repository
```
git clone https://github.com/12awoodward/blackjack.git
```

2. run `src/main.py` from the projects root directory
```
python3 src/main.py
```
