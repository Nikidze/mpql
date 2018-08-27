import time
from functions.connection import Connect
from functions.rows import addrow, getrow

con = Connect("somedb", "somesu", "somesupass")
con.select_table("sometable")
#addrow(con, somecol="some_text", somecol2="some_text_2")
start_time = time.time()
print(getrow(con, ['somecol', "somecol2"]).row['somecol'])
print("--- %s seconds ---" % (time.time() - start_time))