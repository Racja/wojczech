import random

random.seed()
numb = []

for i in range(0, 50):
    numb.append(int(random.random() * 100))

print("Liczby przed sortowaniem: \n", numb)

def sort_func(vector):
    size = len(vector)
    for i in range (size):
        for j in range(i+1, size):
            if vector[i] < vector[j]:
                pass
            else:
                n = vector[i]
                vector[i] = vector[j]
                vector[j] = n

sort_func(numb)
print("Posortowane liczby: \n", numb)
