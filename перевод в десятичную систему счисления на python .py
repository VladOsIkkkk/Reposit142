p = int(input("введите основание системы, p = "))

Np = int(input(f"Исходное число N{p} = "))

k = int(1)

N10 = int(0)

while not Np==0:
    N10 = N10 + (Np % 10) * k
    k = k * p
    Np = Np // 10
    
print("N10 = ", N10)
