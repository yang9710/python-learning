# 求最大公约数
def gcd(x, y):
  (x, y) = (y, x) if x > y else (x, y)
  for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
      return factor

# 判断回文数
def is_palindr(num):
  tmp = num
  reversed_num = 0
  while tmp != 0:
    reversed_num = reversed_num * 10 + tmp % 10
    tmp //= 10
  return num == reversed_num

a, b = 5, 10
print(f'{a} * {b} = {a * b}')