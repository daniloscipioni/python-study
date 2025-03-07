from collections import Counter

dict1: dict = {"a": 10, "b": 20, "c": 30}
dict2: dict = {"b": 5, "c": 15, "d": 25}

test = Counter(dict1)
test2 = Counter(dict2)
final = dict(Counter(dict1) + Counter(dict2))
final2 = Counter(dict1) + Counter(dict2)

print(test)
print(test2)
print('----------')
print(final)
print(final2)
