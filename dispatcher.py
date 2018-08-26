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

# create db

if do == "create db":
    name = input("Database name\n")
    ensure_dir("{}/".format(name), True)
    sun = input("Superuser name\n")
    sup = getpass.getpass("Superuser password\n")
    with open("{}/users.json".format(name), "w") as f:
        data = json.dump({sun: {"pass": sup, "permission": "all"}}, fp=f)
        f.close()
else:
    functions = do.split(":")
    if len(functions) > 1:
        function = functions[0]
        # create table
        if function == "create table":
            arg = functions[1]
            os.chdir("somedb/")
            ensure_dir("{}/".format(arg))
        # add column
        if function == "add col":
            arg = functions[1]
            try:
                f = open("somedb/sometable/table.json")
                f.close()
                fis = True
            except IOError as e:
                fis = False
            if fis:
                with open("somedb/sometable/table.json", "r") as f:
                    data = json.load(f)
                    newdata = {}
                    newdata['cols'] = []
                    for col in data['cols']:
                        if col == arg:
                            print("Column already exists")
                            exit()
                        else:
                            newdata['cols'].append(col)
                    newdata['cols'].append(arg)
                    f.close()
                    f2 = open("somedb/sometable/table.json", "w")
                    json.dump(newdata, f2)
                    f2.close()
            else:
                with open("somedb/sometable/table.json", "w") as f:
                    data = {}
                    data['cols'] = []
                    data['cols'].append(arg)
                    json.dump(data, f)
                    f.close()
