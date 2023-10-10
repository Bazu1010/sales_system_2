import psycopg2
from flask import request, redirect

conn = psycopg2.connect(
     database="myduka_class", user='postgres', password='T@fari2022')


# Getting Data
def get_data(table_name):
    cursor = conn.cursor()
    t= f"select * from {table_name}"
    cursor.execute(t)
    all_data = cursor.fetchall()

    return all_data


## Inserting a new product in the table
def insert_product(values):
    cursor = conn.cursor()
    insert_products="INSERT INTO products(name,buying_price,selling_price,stock_quantity) VALUES(%s,%s,%s,%s)"
    cursor.execute(insert_products,values)
    conn.commit()

    

# Inserting Sale

def insert_sale(values):
    cursor = conn.cursor()
    insert_s = "INSERT INTO sales(product_id,quantity,created_at) VALUES(%s,%s,now())"
    cursor.execute(insert_s,values)
    conn.commit()

## Calculate profit per day
def calculate_profit():
        cursor = conn.cursor()

        run_query ="SELECT DATE(created_at) AS date,(SUM(products.selling_price - products.buying_price) * sales.quantity) AS profit from sales JOIN products on products.id = sales.product_id Group by date, sales.quantity ORDER by date;"
        cursor.execute(run_query)
        all_data =cursor.fetchall()

        return all_data





# ##  Check if email exists
def check_email(new_email):
     cursor = conn.cursor()
     check_email = "SELECT users.email from users where email = %s "
     cursor.execute(check_email)
     one_email = cursor.fetchone(new_email)
     
     if one_email:
          return one_email
     else:
          return False
     
# CHECK IF EMAIL AND PASS MATCH

def check_login(email,password):
    cursor = conn.cursor()
    check_all = "SELECT * FROM users WHERE email=%s and password=%s"
    cursor.execute(check_all,(email,password))
    all = cursor.fetchone() 
   
         
    if all:
         if all[3] == password:
         
           return all
    
         else:
          return False
        
     
     





## Inserting a new user in the table
def insert_user(values):
    cursor = conn.cursor()
    new_user="INSERT INTO users(full_name,email,password) VALUES(%s,%s,%s)"
    cursor.execute(new_user,values)
    conn.commit()

values =("Tyson","Tyson@mail.com","simon@254")
n =insert_user(values)

print(n)

  

  

   


  