######    0123456789012345678901234567890123456789012345678901234567890'
record = '....................100 .......513.25 ..........'
SHARES = slice(20, 23)
PRICE = slice(31, 37)
cost = int(record[SHARES]) * float(record[PRICE])
# cost = int(record[20:23]) * float(record[31:37])
print(cost)


a = slice(5, 50, 2)
s = 'HelloWorld'
a.indices(len(s)) # (5, 10, 2)

for i in range(*a.indices(len(s))):
  print(s[i])