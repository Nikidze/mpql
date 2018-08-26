import getpass, os, json


# functions

# create a directory

def ensure_dir(file_path, ex=False):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    else:
        if ex:
            print("Database already exists")
            exit()


'''
Getting a parameter from the terminal

import sys
for param in sys.argv:
    par = param

'''

# Obtaining a parameter from a user
do = input("What should I do ?\n").lower()
if do == "create db":
    name = input("Database name\n")
    ensure_dir("{}/".format(name), True)
    sun = input("Superuser name\n")
    sup = getpass.getpass("Superuser password\n")
    with open("{}/users.json".format(name), "w") as f:
        data = json.dump({sun: {"pass": sup, "permission": "all"}}, fp=f)
        f.close()
