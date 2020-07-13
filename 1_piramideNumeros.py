def imprimirLinha(n):
    for i in range(1, n + 1):
        if (i != n):
            print(i, end=" ")
        else:
            print(i, end="")
    print()


def piramide(n):
    for i in range(1, n + 1):
        imprimirLinha(i)


n = int(input())
piramide(n)