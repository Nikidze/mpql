import json, os


class addrow:
    def __init__(self, con, order='id', **cols):
        row = {}
        exists_cols = con.table_cols
        for ec in exists_cols:
            if ec in cols:
                row[ec] = cols[ec]
        row_path = "{}/{}/{}/{}.json".format(con.db, con.selected_table, order, "1")
        directory = os.path.dirname(row_path)
        if not os.path.exists(directory):
            os.makedirs(directory)
        f = open(row_path, "w")
        json.dump(row, f)
        f.close()

class getrow:
    def __init__(self, con, getting, order='id'):
        exists_cols = con.table_cols
        row_path = "{}/{}/{}/{}.json".format(con.db, con.selected_table, order, "1")
        f = open(row_path, "r")
        f_row = json.load(f)
        row = {}
        for i in getting:
            if i in exists_cols:
                row[i] = f_row[i]
                continue
            else:
                print("Column does not exist")
                exit()
                break
        self.row = row
        f.close()

