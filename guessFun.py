import random

def randInRange ():
    while True:
        s1 = input("Podaj dwie liczby:\n")
        s2 = input()

        try:
            n1 = int(s1)
            n2 = int(s2)

        except ValueError:
            print("To nie sa prawidlowe liczby")
            continue
            
        if n1 > n2:
            print("Bledny przedzial")
        else:
            return random.randint(n1, n2)

def guess (number):
        while True:
            s = input("Podaj liczbe:\n")

            try:
                n = int(s)

            except ValueError:
                print("To nie jest prawidlowa liczba")
                continue
            
            if number == n:
                print("Brawo! Magiczna liczba to: ", number)
                return
            elif n < number:
                print("Magiczna liczba jest wieksza")
            else:
                print ("Magiczna liczba jest mniejsza")

guess(randInRange())