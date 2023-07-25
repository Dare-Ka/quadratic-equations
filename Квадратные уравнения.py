class Coefficient:
    def __init__(self, list):
        self.a = list[0]
        self.b = list[1]
        self.c = list[2]
    
    def discriminant(self, a, b, c):
        return self.b**2 - 4*self.a * self.c
    
    def solution(self):
        if self.discriminant(self.a, self.b, self.c) == 0:
            x = -self.b/(2*self.a)
            print(f'x = {x} -----> x = {round(x, 2)}') 
        else:
            x1 = (-self.b + self.discriminant(self.a, self.b, self.c)**0.5)/(2*self.a)
            x2 = (-self.b - self.discriminant(self.a, self.b, self.c)**0.5)/(2*self.a)
            print(f'discriminant = {self.discriminant(self.a, self.b, self.c)}')
            print(f'x1 = {x1} -----> x1 = {round(x1.real, 2) + round(x1.imag, 2)*1j}')
            print(f'x2 = {x2} -----> x2 = {round(x2.real, 2) + round(x2.imag, 2)*1j}')

coefficients = []
for i in input('Введите коэффициенты: ').split():
    coefficients.append(int(i))
coefficients = Coefficient(coefficients)
coefficients.solution()