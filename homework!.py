students = {
    "Ali": [80, 90, 85],
    "Vali": [70, 60, 75],
    "Sami": [95, 88, 92]
}
for ism, son in students.items():
 average = sum(son) / len(son)
 print(f"{ism}: {average:1}")


products = [
    {"name":"olma", "price":120},
    {"name":"anor", "price":90},
    {"name":"banan", "price":150}
]
for product in products:
    if product["price"] > 100:
        print(f"{product['name']}: qimmat {product['price']}")


users = [
    {"name":"Ali", "age":20},
    {"name":"Vali", "age":16},
    {"name":"Sami", "age":25}
]



courses = {
    "python": ["Ali","Vali","Sami"],
    "django": ["Ali","Sami"],
    "ai": ["Vali","Sami","Jasur"]
}



numbers = [
    [4,7,2],
    [9,1,5],
    [3,8,6]
]



data = {
    "users":[
        {"name":"Ali", "active":True},
        {"name":"Vali", "active":False},
        {"name":"Sami", "active":True}
    ]
}


