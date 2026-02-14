import pandas as pd
branches = [
    {"branch_id": 1, "branch_name": "Chennai", "manager": "Ravi Kumar"},
    {"branch_id": 2, "branch_name": "Bangalore", "manager": "Sneha Patel"},
    {"branch_id": 3, "branch_name": "Hyderabad", "manager": "Arun Raj"},
    {"branch_id": 4, "branch_name": "Delhi", "manager": "Neha Singh"},
    {"branch_id": 5, "branch_name": "Mumbai", "manager": "Rahul Verma"},
]

products = [
    {"product_id": 101, "product_name": "Laptop", "category": "Electronics", "price": 65000},
    {"product_id": 102, "product_name": "Mobile", "category": "Electronics", "price": 25000},
    {"product_id": 103, "product_name": "Headphones", "category": "Accessories", "price": 3000},
    {"product_id": 104, "product_name": "Shoes", "category": "Fashion", "price": 4000},
    {"product_id": 105, "product_name": "Watch", "category": "Fashion", "price": 5000},
    {"product_id": 106, "product_name": "Tablet", "category": "Electronics", "price": 35000},
    {"product_id": 107, "product_name": "Keyboard", "category": "Accessories", "price": 2000},
]

sales = [
    {"sale_id": 1, "branch_id": 1, "product_id": 101, "quantity": 5, "sale_date": "2025-01-15"},
    {"sale_id": 2, "branch_id": 2, "product_id": 102, "quantity": 8, "sale_date": "2025-01-20"},
    {"sale_id": 3, "branch_id": 3, "product_id": 103, "quantity": 15, "sale_date": "2025-02-05"},
    {"sale_id": 4, "branch_id": 4, "product_id": 104, "quantity": 6, "sale_date": "2025-02-10"},
    {"sale_id": 5, "branch_id": 5, "product_id": 105, "quantity": 9, "sale_date": "2025-02-15"},
    {"sale_id": 6, "branch_id": 2, "product_id": 106, "quantity": 3, "sale_date": "2025-03-01"},
    {"sale_id": 7, "branch_id": 1, "product_id": 103, "quantity": 12, "sale_date": "2025-03-05"},
    {"sale_id": 8, "branch_id": 3, "product_id": 104, "quantity": 10, "sale_date": "2025-03-07"},
    {"sale_id": 9, "branch_id": 4, "product_id": 102, "quantity": 7, "sale_date": "2025-03-12"},
    {"sale_id": 10, "branch_id": 5, "product_id": 105, "quantity": 5, "sale_date": "2025-03-20"},
    {"sale_id": 11, "branch_id": 1, "product_id": 107, "quantity": 20, "sale_date": "2025-04-01"},
    {"sale_id": 12, "branch_id": 2, "product_id": 101, "quantity": 6, "sale_date": "2025-04-02"},
    {"sale_id": 13, "branch_id": 3, "product_id": 106, "quantity": 4, "sale_date": "2025-04-03"},
    {"sale_id": 14, "branch_id": 4, "product_id": 103, "quantity": 11, "sale_date": "2025-04-04"},
    {"sale_id": 15, "branch_id": 5, "product_id": 104, "quantity": 9, "sale_date": "2025-04-05"},
]

print("1.Load all three lists (branches, products, sales) into pandas DataFrames.\n")
ae=pd.DataFrame(branches)
ac=pd.DataFrame(products)
ab=pd.DataFrame(sales)
print(ae,ac,ab)
print("________________compeleted1____________________\n\n")
print("2.Merge all three into one single sales_report DataFrame.\n")
j=pd.merge(ae,ab,on="branch_id",how="outer")
sales_report1=pd.merge(j,ac,on="product_id",how="outer")
print(sales_report1)
print("__________________compeleted2___________________\n\n")
print("3. Display only sales made in March 2025\n")
print("4.Find the total quantity sold by each branch.")
print(sales_report1.groupby("branch_id")["quantity"].sum())
print("_____________compeleted4________________________\n\n")
print("5.Find the total sales value (quantity * price) for each product.\n")
sales_report1["total_sales"]=sales_report1["quantity"]*sales_report1["price"]
print(sales_report1.groupby("product_id")["total_sales"].sum())
print("_________________compeleted5____________________\n\n")
print("6.Show all sales where quantity > 10.\n")
print(sales_report1[sales_report1["quantity"]>10])
print("________________compeleted6_______________________\n\n")
print("7.Sort the merged data by sale_date.\n")
k=sales_report1.sort_values("sale_date")
print(k)
print("________________compeleted7_______________________\n\n")
print("8.Add a column total_sale = quantity * price.\n")
sales_report1["total_sales"]=sales_report1["quantity"]*sales_report1["price"]
print(sales_report1)
print("________________compeleted8_______________________\n\n")
print("9.Find total sales per category (Electronics, Fashion, Accessories\n")
print(sales_report1.groupby("category")["total_sales"].sum())
print("________________compeleted9_______________________\n\n")
print("10.Find the top 3 branches with the highest total sales.\n")
print(sales_report1.groupby("branch_name")["total_sales"].agg("sum","max").head(3))
print("________________compeleted10_______________________\n\n")
print("11.Create a pivot table showing total sales by branch_name (rows) and category (columns).")
print("12.Which product had the highest number of sales overall?\n")
print(sales_report1.groupby("product_name")[["quantity"]].agg("sum","max").head(1))
print("________________compeleted12________________________")
print("13.Find the average price of products sold in each branch.\n")
print(sales_report1.groupby("branch_name")["price"].mean())
print("________________compeleted13________________________\n\n")
print("14.Find the manager of the branch that sold the most “Electronics” items.\n")
print(sales_report1[sales_report1["category"]=="Electronics"][["manager","category","quantity"]].max())
print("________________compeleted14________________________\n\n")


