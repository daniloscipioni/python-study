count = 0
index = 1

while count < 5:
    if index % 3 == 0:
        print(f"{index} é múltiplo de 3")
        count = count + 1
    index = index + 1

print("--------")
value = 10
while value >= 0:
    print(value)
    value = value - 1
print("FIM")

print("--------")

for number in range(0, 100001, 1000):
    print(number)

print("--------")
