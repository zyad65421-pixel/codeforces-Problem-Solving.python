def print_numbers(n):
    for i in range(1, n + 1):
        print(i, end=" ")

n = int(input())
print_numbers(n)



# دي طريقة 


def print_numbers(n):
    for i in range(1, n + 1):
        if i == n:
            print(i)
        else:
            print(i, end=" ")

n = int(input())
print_numbers(n)


# دي طريقة 


def print_numbers(n):
    print(" ".join(str(i) for i in range(1, n + 1)))

n = int(input())
print_numbers(n)
