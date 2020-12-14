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


z1 = Complex(1.0, -3.0)
z2 = Complex(-0.5, 10.0)

print("z1 = ", z1.get_real_complex(), " + ", z1.get_imag_complex(), "j" )
print("z2 = ", z2.get_real_complex(), " + ", z2.get_imag_complex(), "j" )
z1.conj_complex()
print("conj(z1) = ", z1.get_real_complex(), " + ", z1.get_imag_complex(), "j" )
print("abs(z1)", z1.abs_complex())
sum_z1_z2 = z1.sum_complex(z2)
print("z1 + z2 = ", sum_z1_z2.get_real_complex(), " + ", sum_z1_z2.get_imag_complex(), "j")
diff_z1_z2 = z1.diff_complex(z2)
print("z1 - z2 = ", diff_z1_z2.get_real_complex(), " + ", diff_z1_z2.get_imag_complex(), "j")
multi_z1_z2 = z1.multi_complex(z2)
print("z1 * z2 = ", multi_z1_z2.get_real_complex(), " + ", multi_z1_z2.get_imag_complex(), "j")
