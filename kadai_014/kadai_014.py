price1 = 100
price2 = 200

def total():
    global tax
    tax = 1.1
    return price1 + price2

print (total() * tax)
