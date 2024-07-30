num = int(input('输入一个整数 = '))

reversed_num = 0

while num != 0:
  reversed_num = reversed_num * 10 + num % 10
  num //= 10

print(reversed_num)


"""
《百钱百鸡》问题
Version: 0.1
Author: 骆昊
"""
for x in range(0, 20):
    for y in range(0, 33):
        z = 100 - x - y
        if 5 * x + 3 * y + z / 3 == 100:
            print('公鸡: %d只, 母鸡: %d只, 小鸡: %d只' % (x, y, z))