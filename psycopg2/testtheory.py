import psycopg2

conn = psycopg2.connect(database ="myduka_class", user="postgres", password="T@fari2022")

def get_data(sales):
    cur = conn.cursor()
    f = f"SELECT * from {sales}"
    cur.execute(f)
    all_data = cur.fetchall()

    return all_data