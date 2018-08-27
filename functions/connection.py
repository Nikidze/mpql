import json


class Connect:

    # connection to the database

    def __init__(self, db_name, username, password):
        self.db = db_name
        self.username = username
        self.password = password
        self.permissions = None
        self.selected_table = None
        self.table_cols = None
        try:
            f = open("{}/users.json".format(self.db))
            data = json.load(f)
            if self.username in data and self.password in data[self.username]["pass"]:
                self.permissions = data[self.username]['permission']
            else:
                print("Wrong username or password")
                exit()
            f.close()
        except IOError:
            print("The database or users.json file does not exist")
            exit()

    def select_table(self, table_name):
        try:
            f = open("{}/{}/table.json".format(self.db, table_name))
            self.table_cols = json.load(f)['cols']
            self.selected_table = table_name
            f.close()
        except IOError:
            print("The table or table.json file does not exist")
            exit()