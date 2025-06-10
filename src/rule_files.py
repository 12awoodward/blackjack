import os

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
