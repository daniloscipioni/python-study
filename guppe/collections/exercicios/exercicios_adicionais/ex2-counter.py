
from collections import Counter

texto = "python é incrível e python é poderoso"

count = dict(Counter(texto.split()))

print(count)
