#basic functions
def greet_user():
        """Ask the user for their name and greet them"""
        name =input("enter your name: ")
        print(f"hello,{name} !welcome to the course")
greet_user()

#parameters vs arguments 

def calculate_total(price, quantity): 
    total= price * quantity
    return total

item_price = 19.99
item_quantity = 3
bill_total = calculate_total(item_price, item_quantity)
print("total bill:", bill_total)

#default parameters 

def checkout(amount, shipping=5.0):
    final_amount = amount + shipping
    return final_amount

print("order 1 total:", checkout(50))
print("order 2 total:", checkout(50, shipping= 10))

#keyword arguments

def register_student(name,program,year):
    print("-------student registration-------")
    print(f"name :{name}")
    print(f"program : {program}")
    print(f"year : {year}")
    print("-------------------------")


register_student("anu","computer science", 1)

register_student(year=2, name="raul", program="data science")

#args (Variable position Arguments)

def average_score(*scores):
    """Calculate average of any number of scores."""
    if not scores:
        print("no scores provided")
        return None

    Total=sum(scores)
    Avg= total/len(scores)
    print(f"scores: ¨{scores}")
    print(f"average: ¨{avg}")
    return Avg

average_score(80,90,75)
average_score(100,95)
average_score()

#Variable Keyword Args

def create_profile(**info):
    """create user profile with any number of attributes"""
    if not info:
        print("empty profile")
        return
    
    print("-----User Profile------")
    for key, value in info.items():
        print(f"{key.capitalize():}:{value}") 
        print("---------------")

create_profile(name="K", role="Professor", department="CS")
create_profile(name="Sam", ctiy="Sacramento")
create_profile()

#combining args and kwargs 

def log_event(event_type,*details,**metadata):
    """log an event with details and metadata"""
    print("===event log===")
    print(f"type: ¨{event_type}")

    if details:
        print(f"details:{details}")
    else:
        print("details:(none)")

    if metadata:
        print(f"metadata:")
        for key, value in metadata.items():
            print(f"{key}={value}")
        else:
            print("metadata:(none)")
        print("======================")

    log_event("LOGIN","success",user="K", ip="192.168.0.10")
    log_event("FILE_UPLOAD","report.pdf", size="2MB")
    log_event("PING")

#return to multiple values 
def analyze_sales(sales):
    """analyze sales data and return min, max, total and average."""
    if not sales:
        return None, None,0,0

    min_sale=min(sales)
    max_sale=max(sales)
    total=sum(sales)
    average=total/len(sales)
    return min_sale, max_sale, total, average 

week_sales=[120,150,90,200,175]
min_S, max_s, total_s, avg_s= analyze_sales(week_sales)

print(f"Min sale: ${min_S}")
print(f"Max sale: ${max_S}")
print(f"Total sale: ${total_S}")
print(f"Average sale: ${avg_S:2f}")

#scope: Local vs Global variables 

balance= 1000

def deposit_correct(amount):
    global balanace
    balance=balance + amount
    return balance

print("initial balance", balance)
deposit_correct(200)
print("After deposit:", balance)

#Higher-order functions 
def ten_percent_discount(amount):
    return amount*0.9

def flat_five_discount (amount):
    return amount -5 
    
def apply_disocunt(amount, discount_func):
    return new_amount

apply_discount(100, ten_percent_discount)
apply_discount(100, flat_five_discount)


#lamba functions 

square= lambda x: x**2
print(square(5))

products=[
    ("Notebook", 4.99)
    ("pen", 1.49)
    ("Backpack", 29.99)
    ("bottle", 9.99)
]

sorted_by_price= sorted(products, key=lambda item : item[1])
print("products sorted by price:")
for name, price in sorted_by_price 
    print(f"{name}:${price}")


#docstrings 

def celsius_to_farenheit(c):
    """
    convert temperature from celsius to farenheit 

    formula F=(C*9/5)+32

    args:
        c(float):temperature in celsius 

    returns:
        float: temperature in farenheit 

    """
    return (C*9/5)+32

    result= celsius_to_fahrenheit(37)
    print(f"37 C in fahrenheit={result}F")

    print("\nDocstring:")
    print(celsius_to_farenheit.__doc__)