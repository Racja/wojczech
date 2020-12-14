import math

def quad_func(a, b, c):

    delta = b ** 2 - 4 * a * c

    if (delta == 0):
        x0 = -b / (2 * a)
        print("Równanie kwadratowe ma jedno rozwiązanie: \nx0 = ", x0)
    elif (delta > 0):
        x1 = (-b - math.sqrt(delta)) / (2 * a)
        x2 = (-b + math.sqrt(delta)) / (2 * a)
        print("Równanie kwadratowe ma dwa rozwiązania: \nx1 = ", x1, "\nx2 = ", x2)
    else:
        print("Równanie kwadratowe nie ma rowiązań rzeczywistych")

print("Podaj współczynniki funkcji kwadratowej")
a = float(input("a : "))
b = float(input("b : "))
c = float(input("c : "))
quad_func(a, b, c)
