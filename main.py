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


# '''
# Returneaza produsul numerelor din lista lst.
# '''
# def get_product(lst):
#   # codul vostru aici
#
#
# '''
# Returneaza CMMDC a doua numere x si y folosind primul algoritm.
# '''
# def get_cmmdc_v1(x, y):
#   # codul vostru aici
#
#
# '''
# Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
# '''
# def get_cmmdc_v2(x, y):
#   # codul vostru aici


def main():
    print("1. Returneaza true daca n este prim si false daca nu.")
    input1 = int(input('Numar de test: '))
    print("Rezultatul este: ", is_prime(input1))


if __name__ == '__main__':
    main()
