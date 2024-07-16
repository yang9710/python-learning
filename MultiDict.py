from collections import defaultdict

d1 = defaultdict(list)
d1['a'].append(1)
d1['a'].append(2)
d1['b'].append(4)

d2 = defaultdict(set)
d2['a'].add(1)
d2['a'].add(2)
d2['b'].add(4)

d3 = {} # 一个普通的字典
d3.setdefault('a', []).append(1)
d3.setdefault('a', []).append(2)
d3.setdefault('b', []).append(4)

print(d1)
print(d2)
print(d3)