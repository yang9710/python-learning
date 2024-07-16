from collections import namedtuple

# Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
# sub = Subscriber('jonesy@example.com', '2012-10-19')
# print(sub.addr, sub.joined)

def compute_cost_normal(records):
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]
    return total

Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
def compute_cost_named(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total

s = Stock('ACME', 100, 123.45, '', '')
# replace
s = s._replace(shares=75)
compute_cost_named([s])

# Create a prototype instance
stock_prototype = Stock('', 0, 0.0, None, None)

# Function to convert a dictionary to a Stock
def dict_to_stock(s):
    return stock_prototype._replace(**s)

a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}
print(dict_to_stock(a))
print(dict_to_stock(b))