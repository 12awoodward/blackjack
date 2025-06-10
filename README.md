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

## Creating Rules

You can create a set of rules by adding them to a `.txt` file in the rules directory. The file should have 1 rule per line.

Each rule should have 3 parts: the suit, number, and effect. Each part should be separated by a vertical bar `|`. Rules are not case sensitive.

To apply multiple effects to the same cards, add a new rule for each effect. For example, these rules will set all 8 cards to skip a turn and pickup 2:
```
all|8|skip
all|8|pickup_add:2
```

### Suits

The suit value will determine which of the card suits the rule will apply to.

- `spades`/`clubs`/`hearts`/`diamonds` - The rule will apply to only the suit specified.
- `black` - The rule will apply to the Black suits (Spades & Clubs).
- `red` - The rule will apply to the Red suits (Hearts & Diamonds).
- `all` - The rule will apply to all suits.

### Number

The number value is used to specify which card numbers the rule will apply to.

This can be any of the numbers 2-10 along with `A`, `J`, `Q`, `K`. Rules can only be set to apply to a specific card number.

### Effects

The effect value will add an effect to the cards specified by the rule.

- `suit` - When played, the player can choose a suit to switch to.
- `direction` - When played, the direction of play is switched.
- `skip` - When played, the next players turn is skipped.
- `pickup_add:` - When played, adds the amount specified to the number of cards the next player will need to pickup.
- `pickup_set:` - When played, sets the current pickup count to the amount specified, ignoring the current amount.

`pickup_add:` and `pickup_set:` will need a number added after the rule to set the value the rule will apply.

These rules will set Black Jacks to pickup 5 and Red Jacks to set the current pickup amount to 0 (to cancel any pickups).
```
black|J|pickup_add:5
red|J|pickup_set:0
```

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
