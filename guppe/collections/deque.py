"""
Modulo Collections - Deque

https://docs.python.org/3/library/collections.html#collections.deque

Uma lista de alta performance

"""

# importando

from collections import deque

deq = deque('geek')

print(deq)

# Adicionando elementos no deque

deq.append('y')  # Adiciona no final
print(deq)

deq.appendleft('k')  # Adiciona no comeco
print(deq)

# Remove elementos
print(deq.pop())  # Remove e retorna o ultimo elemento
print(deq)

print(deq.popleft())  # Remove e retorna o primeiro elemento
print(deq)
