import pandas as pd
departments = [
    {"dept_id": 1, "dept_name": "Sales"},
    {"dept_id": 2, "dept_name": "HR"},
    {"dept_id": 3, "dept_name": "IT"},
    {"dept_id": 4, "dept_name": "Finance"},
]

employees = [
    {"emp_id": 101, "emp_name": "Karthik", "dept_id": 1, "salary": 55000, "join_date": "2022-06-15"},
    {"emp_id": 102, "emp_name": "Anjali", "dept_id": 1, "salary": 60000, "join_date": "2021-09-10"},
    {"emp_id": 103, "emp_name": "Ravi", "dept_id": 2, "salary": 45000, "join_date": "2023-01-20"},
    {"emp_id": 104, "emp_name": "Meena", "dept_id": 3, "salary": 75000, "join_date": "2020-05-12"},
    {"emp_id": 105, "emp_name": "Prakash", "dept_id": 4, "salary": 80000, "join_date": "2019-03-10"},
    {"emp_id": 106, "emp_name": "Divya", "dept_id": 3, "salary": 72000, "join_date": "2022-12-05"},
    {"emp_id": 107, "emp_name": "Suresh", "dept_id": 2, "salary": 48000, "join_date": "2023-07-01"},
]

performance = [
    {"emp_id": 101, "year": 2023, "rating": 4.2, "bonus": 12000},
    {"emp_id": 102, "year": 2023, "rating": 4.8, "bonus": 15000},
    {"emp_id": 103, "year": 2023, "rating": 3.5, "bonus": 8000},
    {"emp_id": 104, "year": 2023, "rating": 4.9, "bonus": 18000},
    {"emp_id": 105, "year": 2023, "rating": 4.6, "bonus": 16000},
    {"emp_id": 106, "year": 2023, "rating": 4.0, "bonus": 11000},
    {"emp_id": 107, "year": 2023, "rating": 3.8, "bonus": 9000},
]

print("1.Merge employees with departments.")
j=pd.DataFrame(departments)
b=pd.DataFrame(employees)
e=pd.DataFrame(performance)
c=pd.merge(b,j,on="dept_id",how="outer")
print(c)
print("______________compeleted1______________")
print(" 2 .Merge with performance to get a single DataFrame")
jk=pd.merge(c,e,on="emp_id",how="outer")
print(jk)
print("_____________compeleted2_______________")
print("3.Display all employees who joined after 2022.")
print([jk[jk["join_date"]>"2022-12-31"]])
print("_____________compeleted3_______________")
print("4.Find the total number of employees per department")
print(jk.groupby("dept_name")["emp_name"].count())
print("_____________compeleted4_______________")
print("5.Display all employees with a rating above 4.5.")
print([jk[jk["rating"]>4.5]])
print("_____________compeleted5_______________")
print("6.Find the average salary per department.")
print(jk.groupby("dept_name")["salary"].mean())
print("_____________compeleted6_______________")
print("7.Find the average rating by department.")
print(jk.groupby("dept_name")["rating"].mean())
print("_____________compeleted7_______________")
print("8.Calculate total bonus per department.")
print(jk.groupby("dept_name")["bonus"].sum())
print("_____________compeleted8_______________")
print("9.Add a new column total_income = salary + bonus.")
io=(jk["salary"])
ip=(jk["bonus"])
lp=(io+ip)
jk["total_income"]=lp
print(jk)
print("_____________compeleted9_______________")
print("10.Sort employees by rating (highest first).")
print(jk.sort_values(by=['rating'], ascending=False))
print("11.Find the top-rated employee in each department")
print(jk.groupby("dept_name")["rating"].max())
print("_____________compeleted11_______________")
