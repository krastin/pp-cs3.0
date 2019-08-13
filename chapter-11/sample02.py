ten = set(range(10))
lows = {0, 1, 2, 3, 4}
odds = {1, 3, 5, 7, 9}
lows.add(9)
print(lows)
print(lows.difference(odds))
print(lows.intersection(odds))
print(lows.issubset(ten))
print(lows.issuperset(odds))
print(lows.remove(0))
print(lows.symmetric_difference(odds))
print(lows.union(odds))
lows.clear()
print(lows)