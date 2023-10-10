import psycopg2

## First step, connect to the db using the connect () method.
conn = psycopg2.connect(databade = "DB", user="postgre", password="pass")

##  Second step, introduce the cursor() method that will be able to execute commands.
cur = conn.cursor()

     ## Here we pass our commands (queries) example ('SELECT * FROM Products) = m
     ## It is advisable to create a variable outside the cur.execute function then pass it inside.
cur.execute('m')

## To get the returned values from your query, you need to call one of the two methods:
one_data = cur.fetchone()  
all_data = cur.fetchall()

## Finally we create a RETURN command for our function
#return one_data or all_data


###   GET_DATA FROM DB

conn = psycopg2.connect(databade = "DB", user="postgre", password="pass")

def get_data(table_name):
    cur = conn.cursor()
    v = f"SELECT * FROM {table_name}"
    cur.execute(v)
    all_data = cur.fetchall()

    return all_data









