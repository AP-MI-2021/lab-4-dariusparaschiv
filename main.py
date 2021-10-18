import copy


def read_list():
    lst = []
    given_string = input("scrieti un sir de nr. separate prin virgula ")
    numbers_as_string = given_string.split(",")
    for x in numbers_as_string:
        lst.append(x)
    return lst


def is_prime(x):
    if x<2:
        return False
    for n in range(2, int(x**1/2)+1):
        if x %n == 0:
            return False
    return True


def test_is_prime():
    assert is_prime(1) is False
    assert is_prime(0) is False
    assert is_prime(5) is True
    assert is_prime(25) is False


def delete_prime(lst):
    '''
    Sterge numerele prime dintr o lista
    :param lst: lista cu numere intregi
    :return: lista fara numerele prime
    '''
    new_lst = []
    for x in lst:
        if not(is_prime(x)):
            new_lst.append(x)
    lst = copy.deepcopy(new_lst)
    return lst


def test_delete_prime():
    assert delete_prime([1, 4, 9]) == [1, 4, 9]
    assert delete_prime([1, 2]) == [1]
    assert delete_prime([]) == []


def arithmetic(lst, n):
    '''
    verifica daca media aritmetica a numerelor din sir sunt mai mari decat n
    :param lst: lista cu numere intregi
    :param n: numarul dat
    :return: True, daca media aritmetica a numerelor din sir sunt mai mari decat n, 0 in caz contrar
    '''
    k = 0
    s = 0
    for x in lst:
        k = k + 1
        s = s + x
    if k != 0:
        return s/k > n


def test_arithmetic():
    assert arithmetic([10, -3, 25, -1, 3, 25, 18], 10) is True
    assert arithmetic([10, 23], 25) is False


def printMenu():
    print("1. Citire lista")
    print("2. Elimina numerele prime")
    print("3. Verificati daca media aritmetica a numerelor este mai mare decat n")
    #print("4. Adauga dupa fiecare element numarul de divizor proprii")
    #print("5. Prelucrare lista")
    print("6. Iesire")
    print("7. Afisare lista")


def count_div(n):
    k = 0
    for i in range(1, n+1):
        if n % i == 0:
            k = k+1
    return k


def test_count_div():
    assert count_div(1) == 1
    assert count_div(2) == 2
    assert count_div(5) == 2
    assert count_div(10) == 4


def list_divi(lst):
    '''
    afiseaza lista obtinuta prin adaugarea dupa fiecare element nr de divizor
    :param lst: lista cu nr intregi
    :return: lista obtinuta prin adaugarea dupa fiecare element nr de divizor
    '''
    newlst=[]
    for x in lst:
        newlst.append((x))
        newlst.append(count_div(x))
    return newlst


def test_list_divi():
    assert list_divi([19, 5, 24, 12, 9]) == [19, 0, 5, 0, 24, 6, 12, 4, 9, 1]


def modify_list(lst):
    '''
    Afiseaza lista obtinuta din lista initialia in care nr sunt inlocuite cu un tuplu, unde
    pe prima pzitie este nr, pe a doua indexul elementului si pe a treia nr de aparitii.
    :param lst: lista cu numere
    :return: lista modificata
    '''


def main():
    test_is_prime()
    test_delete_prime()
    test_arithmetic()
    test_count_div()
    #test_list_divi()
    lst = []
    while True:
        printMenu()
        optiune = input("Alegeti o optiune: ")
        if optiune == '1':
            lst = read_list()
        elif optiune == '2':
            delete_prime(lst)
        elif optiune == "3":
            n = int(input("dati un nr"))
            if arithmetic((lst,n)):
                print("DA")
            else:
                print("NU")
        elif optiune == "4":
            break
        elif optiune == "6":
            break
        elif optiune == "7":
            print(lst)
        else:
            print("optiune invalida")


main()
