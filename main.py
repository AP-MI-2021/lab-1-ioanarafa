'''
Returneaza true daca n este prim si false daca nu.
'''
def is_prime(n):
   if n < 2:
       return False
   if n == 2:
       return True
   for i in range(2, int((n / 2) + 1)):
       if n % i == 0:
           return False
   return True


'''
Returneaza produsul numerelor din lista lst.
'''
def get_product(lst):
    p = 1
    for el in lst:
        p = p * el
    return p


'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''
def get_cmmdc_v1(x, y):
    z = 0
    while y != 0:
        z = x % y
        x = y
        y = z
    return x


'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''
def get_cmmdc_v2(x, y):
    z = y
    if x < y:
        z = x
    if z == 0:
        if x > y:
            return x
        return y
    for i in range(z, 1, -1):
        if x % i == 0 and y % i == 0:
            return i

def main():
    print("1. Returneaza true daca n este prim si false daca nu.")
    input1 = int(input('Numar de test: '))
    print("Rezultatul este: ", is_prime(input1))

    print("2. Returneaza produsul numerelor din lista lst.")
    a = []
    input2 = int(input(" Introduceti numarul de cifre= "))
    for i in range(0, input2):
        a.append(int(input()))
    print(get_product(a))

    print("3. Returneaza CMMDC a doua numere x si y folosind primul algoritm.")
    x = int(input("x="))
    y = y = int(input("y="))
    print(get_cmmdc_v1(x, y))

    print("4. Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.")
    m = int(input("x="))
    n = n = int(input("y="))
    print(get_cmmdc_v2(m, n))

if __name__ == '__main__':
    main()
