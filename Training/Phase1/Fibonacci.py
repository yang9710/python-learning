'''
斐波那契数列的特点是数列的前两个数都是1，
从第三个数开始，每个数都是它前面两个数的和，
形如：1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, …。
'''
# 生成斐波那契数列（前20个数字）

def fibobacci(num):
  a, b = 0, 1
  for _ in range(num):
    a, b = b, a + b
    yield a

# for i in fibobacci(20):
#   print(i)

# 素数指的是只能被1和自身整除的正整数（不包括1）。

for i in range(2, 100):
  for j in range (2, i):
    if i % j == 0:
      break
  else:
    print(i)
