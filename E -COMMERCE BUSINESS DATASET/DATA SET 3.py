import pandas as pd
customers = [
    {"cust_id": 1, "cust_name": "Arun", "city": "Chennai", "signup_date": "2023-05-12"},
    {"cust_id": 2, "cust_name": "Priya", "city": "Bangalore", "signup_date": "2023-06-22"},
    {"cust_id": 3, "cust_name": "Rahul", "city": "Mumbai", "signup_date": "2023-07-10"},
    {"cust_id": 4, "cust_name": "Sneha", "city": "Delhi", "signup_date": "2023-08-18"},
    {"cust_id": 5, "cust_name": "Vijay", "city": "Hyderabad", "signup_date": "2023-09-03"},
    {"cust_id": 6, "cust_name": "Ananya", "city": "Pune", "signup_date": "2024-01-14"},
    {"cust_id": 7, "cust_name": "Ramesh", "city": "Chennai", "signup_date": "2024-02-05"},
]


orders = [
    {"order_id": 101, "cust_id": 1, "order_date": "2025-03-10", "branch_id": 1, "status": "Delivered"},
    {"order_id": 102, "cust_id": 2, "order_date": "2025-03-12", "branch_id": 2, "status": "Pending"},
    {"order_id": 103, "cust_id": 3, "order_date": "2025-03-15", "branch_id": 3, "status": "Delivered"},
    {"order_id": 104, "cust_id": 4, "order_date": "2025-03-18", "branch_id": 4, "status": "Cancelled"},
    {"order_id": 105, "cust_id": 5, "order_date": "2025-03-20", "branch_id": 3, "status": "Delivered"},
    {"order_id": 106, "cust_id": 6, "order_date": "2025-03-22", "branch_id": 1, "status": "Delivered"},
    {"order_id": 107, "cust_id": 7, "order_date": "2025-03-25", "branch_id": 2, "status": "Returned"},
]


order_details = [
    {"order_id": 101, "product_id": 201, "quantity": 1},
    {"order_id": 101, "product_id": 202, "quantity": 2},
    {"order_id": 102, "product_id": 203, "quantity": 1},
    {"order_id": 103, "product_id": 204, "quantity": 3},
    {"order_id": 104, "product_id": 205, "quantity": 2},
    {"order_id": 105, "product_id": 201, "quantity": 1},
    {"order_id": 105, "product_id": 206, "quantity": 1},
    {"order_id": 106, "product_id": 207, "quantity": 5},
    {"order_id": 107, "product_id": 205, "quantity": 1},
]


products = [
    {"product_id": 201, "product_name": "Laptop", "category_id": 301, "price": 65000},
    {"product_id": 202, "product_name": "Mobile", "category_id": 301, "price": 25000},
    {"product_id": 203, "product_name": "Headphones", "category_id": 302, "price": 3000},
    {"product_id": 204, "product_name": "Shoes", "category_id": 303, "price": 4000},
    {"product_id": 205, "product_name": "Watch", "category_id": 303, "price": 5000},
    {"product_id": 206, "product_name": "Tablet", "category_id": 301, "price": 35000},
    {"product_id": 207, "product_name": "Keyboard", "category_id": 302, "price": 2000},
]


categories = [
    {"category_id": 301, "category_name": "Electronics"},
    {"category_id": 302, "category_name": "Accessories"},
    {"category_id": 303, "category_name": "Fashion"},
]


payments = [
    {"payment_id": 501, "order_id": 101, "payment_mode": "UPI", "amount": 95000, "payment_status": "Success"},
    {"payment_id": 502, "order_id": 102, "payment_mode": "Credit Card", "amount": 3000, "payment_status": "Pending"},
    {"payment_id": 503, "order_id": 103, "payment_mode": "Net Banking", "amount": 12000, "payment_status": "Success"},
    {"payment_id": 504, "order_id": 104, "payment_mode": "UPI", "amount": 10000, "payment_status": "Failed"},
    {"payment_id": 505, "order_id": 105, "payment_mode": "Credit Card", "amount": 40000, "payment_status": "Success"},
    {"payment_id": 506, "order_id": 106, "payment_mode": "UPI", "amount": 10000, "payment_status": "Success"},
    {"payment_id": 507, "order_id": 107, "payment_mode": "UPI", "amount": 5000, "payment_status": "Refunded"},
]


branches = [
    {"branch_id": 1, "branch_name": "Chennai", "manager": "Ravi Kumar"},
    {"branch_id": 2, "branch_name": "Bangalore", "manager": "Sneha Patel"},
    {"branch_id": 3, "branch_name": "Hyderabad", "manager": "Arun Raj"},
    {"branch_id": 4, "branch_name": "Delhi", "manager": "Neha Singh"},
]
print("1.Load all seven tables as pandas DataFrames.\n")
a=pd.DataFrame(customers)
b=pd.DataFrame(orders)
c=pd.DataFrame(order_details)
d=pd.DataFrame(products)
e=pd.DataFrame(categories)
f=pd.DataFrame(payments)
g=pd.DataFrame(branches)
print(a,b,c,d,e,f,g,sep="\n")
print("________________completed1_______________\n")
print("2.Merge orders, customers, and branches to get full order info.\n")
a=pd.DataFrame(customers)
b=pd.DataFrame(orders)
g=pd.DataFrame(branches)
kk=pd.merge(b,a,on="cust_id",how="outer")
kp=pd.merge(kk,g,on="branch_id",how="outer")
print(kp)
print("________________completed2________________\n")
print("3.Merge order_details with products and categories to show item details.\n")
c=pd.DataFrame(order_details)
d=pd.DataFrame(products)
e=pd.DataFrame(categories)
hj=pd.merge(c,d,on="product_id",how="outer")
hk=pd.merge(hj,e,on="category_id",how="outer")
print(hk)
print("________________completed3________________\n")
print("4.Calculate total price per order (quantity * price).\n")
c=pd.DataFrame(order_details)
d=pd.DataFrame(products)
hk=pd.merge(c,d,on="product_id",how="outer")
hk["total_price"] = hk["quantity"] * hk["price"]
print(hk.groupby("order_id")["total_price"].sum())
print("________________completed4________________\n")
print("5.Find all orders made from Chennai customers.")
p=pd.DataFrame(customers)
print(p[p["city"]=="Chennai"])
print("________________completed5________________\n")
print("6.Calculate total revenue per branch.")
b=pd.DataFrame(orders)
f=pd.DataFrame(payments)
c=pd.DataFrame(order_details)
jl=pd.merge(f,c,on="order_id",how="outer")
ik=pd.merge(jl,b,on="order_id",how="outer")
print(ik.groupby("branch_id")["amount"].sum())
print("________________completed6________________\n")
print("7.Find the most sold category overall.\n")
d=pd.DataFrame(products)
e=pd.DataFrame(categories)
c=pd.DataFrame(order_details)
hk=pd.merge(d,e,on="category_id",how="outer")
hk1=pd.merge(hk,c,on="product_id",how="outer")
print(hk1["category_name"].max())
print("________________completed7________________\n")
print("8.Find total quantity sold per product.\n")
jq=pd.DataFrame(order_details)
jg=pd.DataFrame(products)
op=pd.merge(jq,jg,on="product_id",how="outer")
print(op.groupby("product_name")["quantity"].sum())
print("_____________completed8____________________\n")
print("9.Calculate total payment amount per payment mode.\n")
jb=pd.DataFrame(payments)
print(jb.groupby("payment_mode")["amount"].sum())
print("___________________compeleted9_________________\n")
print("10.Find all orders where payment failed or refunded.\n")
opp=pd.DataFrame(payments)
print(opp[opp["payment_status"]=="Failed"])
print(opp[opp["payment_status"]=="Refunded"])
print("________________compeleted10________________________\n")
print("11.Create a final_sales_report DataFrame joining all 7 tables.\n")
a=pd.DataFrame(order_details)
b=pd.DataFrame(products)
c=pd.DataFrame(categories)
d=pd.DataFrame(branches)
e=pd.DataFrame(payments)
f=pd.DataFrame(orders)
g=pd.DataFrame(customers)
h=pd.merge(f,g,on="cust_id",how="outer")
i=pd.merge(h,a,on="order_id",how="outer")
j=pd.merge(i,b,on="product_id",how="outer")
k=pd.merge(j,c,on="category_id",how="outer")
l=pd.merge(k,e,on="order_id",how="outer")
final_sales_report=pd.merge(l,d,on="branch_id",how="outer")
print(final_sales_report)
print("____________________compeleted11____________________\n")
print("12.Calculate average order value per city.\n")
a=pd.DataFrame(order_details)
b=pd.DataFrame(orders)
c=pd.DataFrame(payments)
d=pd.DataFrame(customers)
e=pd.merge(a,b,on="order_id",how="outer")
f=pd.merge(e,c,on="order_id",how="outer")
g=pd.merge(f,d,on="cust_id",how="outer")
print(g.groupby("city")["amount"].mean())
print("________________complete12________________________\n")
print("13.Identify top 3 customers by total amount spent.\n")
e=pd.DataFrame(payments)
f=pd.DataFrame(orders)
g=pd.DataFrame(customers)
h=pd.merge(f,g,on="cust_id",how="outer")
i=pd.merge(h,e,on="order_id",how="outer")
print(i.groupby("cust_name")["amount"].agg("sum","max").sort_values(ascending=False).head(3))
print("________________compeleted13________________________\n")
print("14.Find branch managers who handled the most orders.\n")
f=pd.DataFrame(orders)
d=pd.DataFrame(branches)
c=pd.merge(f,d,on="branch_id",how="outer")
print(c.groupby(["manager","branch_name"])["order_id"].count() )
print("____________________completed14___________________\n")
print("15.Find which payment mode has the highest success rate.")
m=pd.DataFrame(payments)
print(m[m["payment_status"]=="Success"][["payment_mode","amount"]].max())
print("________________complete15________________________\n")