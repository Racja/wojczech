import math

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def get_real_complex(self):
        return self.real

    def get_imag_complex(self):
        return self.imag

    def conj_complex(self):
        self.imag = -self.imag

    def sum_complex(self, complex2):
        return Complex(self.real + complex2.real, self.imag + complex2.imag)

    def diff_complex(self, complex2):
        return Complex(self.real - complex2.real, self.imag - complex2.imag)

    def multi_complex(self, complex2):
        return Complex(self.real * complex2.real - self.imag * complex2.imag, self.real * complex2.imag + self.imag * complex2.real)

    def abs_complex(self):
        return math.sqrt(self.real * self.real + self.imag * self.imag)

while 1:
    print('''Kalkulator liczb zespolonych
    Proszę wybrać działanie
        1 - moduł
        2 - sprzężenie
        3 - dodawanie
        4 - odejmowanie
        5 - mnożenie
        6 - wyjscie''')

    a = int(input("Twoj wybor: "))
    print("Poprawne wprowadzenie liczb zespolonych : re + imag")

    if a == 1:
        re, im = input("Podaj liczbę: \nz1 = ").split(" + ")
        z1 = Complex(float(re), float(im))
        print("abs(z1) = ", z1.abs_complex())

    elif a == 2:
        re, im = input("Podaj liczbę: \nz1 = ").split(" + ")
        z1 = Complex(float(re), float(im))
        z1.conj_complex()
        print("conj(z1) = ", z1.get_real_complex(), " + ", z1.get_imag_complex(), "j")

    elif a == 3:
        re, im = input("Podaj pierwszą liczbę: \nz1 = ").split(" + ")
        z1 = Complex(float(re), float(im))
        re, im = input("Podaj drugą liczbę: \nz2 = ").split(" + ")
        z2 = Complex(float(re), float(im))
        sum_z1_z2 = z1.sum_complex(z2)
        print("z1 + z2 = ", sum_z1_z2.get_real_complex(), " + ", sum_z1_z2.get_imag_complex(), "j")

    elif a == 4:
        re, im = input("Podaj pierwszą liczbę: \nz1 = ").split(" + ")
        z1 = Complex(float(re), float(im))
        re, im = input("Podaj drugą liczbę: \nz2 = ").split(" + ")
        z2 = Complex(float(re), float(im))
        diff_z1_z2 = z1.diff_complex(z2)
        print("z1 - z2 = ", diff_z1_z2.get_real_complex(), " + ", diff_z1_z2.get_imag_complex(), "j")

    elif a == 5:
        re, im = input("Podaj pierwszą liczbę: \nz1 = ").split(" + ")
        z1 = Complex(float(re), float(im))
        re, im = input("Podaj drugą liczbę: \nz2 = ").split(" + ")
        z2 = Complex(float(re), float(im))
        multi_z1_z2 = z1.multi_complex(z2)
        print("z1 * z2 = ", multi_z1_z2.get_real_complex(), " + ", multi_z1_z2.get_imag_complex(), "j")

    elif a == 6:
        break

    else:
        print("Komenda o tym numerze nie istnieje")