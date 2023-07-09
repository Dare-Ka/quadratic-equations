def discriminant(a, b, c):
  return b**2 - 4*a*c
def quadratic_equation(a, b, c):
  if discriminant(a, b, c) == 0:
    x = -b/(2*a)
    print(f'x = {x} -----> x = {round(x, 2)}')
    return x
  else:
    x1 = (-b + discriminant(a, b, c)**0.5)/(2*a)
    x2 = (-b - discriminant(a, b, c)**0.5)/(2*a)
    print(f'discriminant = {discriminant(a, b, c)}')
    print(f'x1 = {x1} -----> x1 = {round(x1.real, 2) + round(x1.imag, 2)*1j}')
    print(f'x2 = {x2} -----> x2 = {round(x2.real, 2) + round(x2.imag, 2)*1j}')
    return
a= float(input('Введите число a: '))
b = float(input('Введите число b: '))
c = float(input('Введите число c: '))
quadratic_equation(a, b, c)