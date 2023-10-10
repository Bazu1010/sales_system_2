### With our table already created and existing, we use the insert command to insert values in the table.
## First we write a string INSERT SQL command for the execute() method.

import psycopg2
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres")
cur = conn.cursor()
w = "INSERT INTO table_name(colum1, column2) VALUES (%s,%s)"
cur.execute(w)

### After having the insert query and has been executed, we commit our change as shown below:
conn.commit()
