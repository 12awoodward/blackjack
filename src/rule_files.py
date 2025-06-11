import os

from deck import Suits, Numbers
from card_effects import effect_alias, effect_has_arg

default_rules = {
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


def print_rule_issue(rule, issue):
    print(f"\n\nUnknown Rule: {rule}")
    print(f"     Error: {issue}")


def load_rules(rule_path):
    rules = get_file_contents(rule_path).strip()
    # no rules
    if len(rules) == 0:
        return {}

    rules = rules.split("\n")
    valid_suits = get_valid_suit_str()
    valid_nums = get_valid_number_str()
    valid_effects = get_valid_effect_str()
    rule_set = {}

    for rule in rules:
        rule_parts = rule.lower().split("|")

        if len(rule_parts) != 3:
            print_rule_issue(rule, "Not 3 Parts")
            continue

        suit = rule_parts[0].strip()
        num = rule_parts[1].strip()
        rule_effect = rule_parts[2].split(":")
        effect_name = rule_effect[0].strip()

        if suit not in valid_suits:
            print_rule_issue(rule, "Invalid Suit")
            continue

        if num not in valid_nums:
            print_rule_issue(rule, "Invalid Number")
            continue

        if effect_name not in valid_effects:
            print_rule_issue(rule, "Invalid Card Effect")
            continue

        if effect_has_arg(effect_name) and len(rule_effect) == 2:
            effect_arg = rule_effect[1].strip()

            try:
                effect_arg = int(effect_arg)

            except ValueError:
                print_rule_issue(rule, "Effect Given Invalid Number")
                continue

            rule_effect[1] = str(effect_arg)
        
        elif effect_has_arg(effect_name) or len(rule_effect) != 1:
            print_rule_issue(rule, "Effect Needs Number Value / Has Number Value When Not Needed")
            continue

        if suit not in rule_set:
            rule_set[suit] = {}
        
        num = num.upper()
        if num not in rule_set[suit]:
            rule_set[suit][num] = []

        rule_effect[0] = effect_name
        rule_set[suit][num].append(":".join(rule_effect))

    return rule_set