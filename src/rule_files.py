import os

from deck import Suits, Numbers
from card_effects import effect_alias

default = {
    "all" : {
        "A" : ["suit"],
        "2" : ["pickup_add:2"],
        "8" : ["skip"],
        "Q" : ["direction"],
    },
    "black" : {
        "J" : ["pickup_add:5"],
    },
    "red" : {
        "J" : ["pickup_set:0"],
    },
}

def is_rule_dir_valid(rule_dir):
    if os.path.exists(rule_dir):
        if len(os.listdir(rule_dir)) > 0:
            return True
    return False

def get_all_rule_files(rule_dir):
    rule_files = []
    for file in os.listdir(rule_dir):
        file_path = os.path.join(rule_dir, file)

        if os.path.isfile(file_path):
            ext = os.path.splitext(file_path)[1]
            if ext == ".txt":
                rule_files.append(file_path)

    return rule_files

def get_rule_name(rule_path):
    return os.path.splitext(os.path.basename(rule_path))[0].replace("_", " ")

def get_file_contents(path):
    with open(path, "r") as file:
        return file.read()
    
def get_valid_number_str():
    options = []
    for num in Numbers:
        options.append(num.value.strip().lower())
    return options

def get_valid_suit_str():
    options = ["all", "black", "red"]
    for suit in Suits:
        options.append(suit.name.lower())
    return options

def get_valid_effect_str():
    return effect_alias.keys()

def load_rules(rule_path):
    rules = get_file_contents(rule_path).strip()
    # no rules
    if len(rules) == 0:
        return {}

    rules = rules.split("\n")
    valid_suits = get_valid_suit_str()
    valid_nums = get_valid_number_str()
    valid_effect = get_valid_effect_str()
    rule_set = {}

    for rule in rules:
        rule_parts = rule.lower().split("|")

        if len(rule_parts) != 3:
            print(f"\nUnknown Rule: {rule}")
            continue

        suit = rule_parts[0]
        num = rule_parts[1]
        rule_effect = rule_parts[2].split(":")[0]

        if suit not in valid_suits:
            print(f"\nUnknown Rule: {rule}")
            continue

        if num not in valid_nums:
            print(f"\nUnknown Rule: {rule}")
            continue

        if rule_effect not in valid_effect:
            print(f"\nUnknown Rule: {rule}")
            continue

        if suit not in rule_set:
            rule_set[suit] = {}
        
        num = num.upper()
        if num not in rule_set[suit]:
            rule_set[suit][num] = []

        rule_set[suit][num].append(rule_parts[2])

    return rule_set