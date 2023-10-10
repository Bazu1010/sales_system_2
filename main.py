from flask import Flask,render_template,request,redirect,session,flash
from dbservice import get_data,insert_product,insert_sale,calculate_profit,insert_user,check_email,check_login
import psycopg2

# conn = psycopg2.connect(
#      database="myduka_class", user='postgres', password='T@fari2022')
app = Flask (__name__)

app.secret_key ="kimkim254"




@app.route("/")
def index1():
    return render_template("index.html")


# Get login
@app.route("/login", methods=['GET', 'POST'])
def login():
    
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        login= check_login(email,password)
        if login:
             session["login_s"] = login[0]
             flash("Login Successful")
             return redirect("/dashboard") 
        else:
            flash("Invalid Email or Password")
            return render_template("login.html")
        
        
@app.route("/logout",methods=['GET','POST'])
def logout():
    session.pop("id", None)
    return redirect('/login')


# SALES ROUTE

@app.route("/sales", methods =["POST"])
def insert_sales():
     product_id = request.form["product_id"]
     quantity   = request.form["quantity"]  
     values = (product_id,quantity)

     insert_sale(values)

     return redirect("/sales")
     

@app.route("/sales")
def sales():
    get_sales = get_data("sales") 
    myprods = get_data("products")   

    return render_template("sales.html", mysales = get_sales, myprods = myprods)

# POST NEW PRODUCTS ROUTE

# When inserting a new product, we call the function created in dbservice. And here is where we request 
# the form from products.html at the action and methods attribute and is where the values input by
# user are gotten and pushed to the db table "/products" using the ["POST"] method.
# Pass the values input inside the function in products in the dbservise.py file. 

@app.route("/products", methods=["Post"])
def add_product():
        name           =  request.form["name"]
        buying_price   =  request.form["buying_price"]
        selling_price  =  request.form["selling_price"]
        stock_quantity =  request.form["stock_quantity"]
        values = (name,buying_price,selling_price,stock_quantity)

        insert_product(values)

        return redirect("/products")

@app.route("/products")
def products():
    
    myprods = get_data("products")   
    return render_template("products.html", prd = myprods)


# DASHBOARD ROUTE
    
@app.route("/dashboard")
def dashboard(): 
 
# THE LONG WAY

# dates = []
# profits= []
# for i in calculate_profit():
# dates.append(i[0])
# profits.append(i[1]) 

 dates=[str(i[0]) for i in calculate_profit()]
 profits=[float(i[1]) for i in calculate_profit()]
 return render_template("dashboard.html", dates=dates, profits=profits )


#Add a new user

@app.route("/register", methods=["GET","POST"])
def add_new():
        if request.method=="POST":
            full_name = request.form.get("username")
            new_email = request.form.get("email")
            new_password = request.form.get("password")
            values= (full_name,new_email,new_password)

            insert_user(values)

            validate_e = check_email(new_email)
            if validate_e:
                  flash("Email already EXISTS")
            else:
                  flash("Registration Successful")
                  return redirect("/login")
            
        return render_template("login.html")





    

    



app.run(debug=True)