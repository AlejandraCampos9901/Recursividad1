_author_='Alejandra Campos contreras'

n = 5
def Suma(n):
    if n <= 2:
        return n
    else:
        return n + Suma(n - 1)
print(Suma(n))