l = [52633, 8137, 1024, 999]
for num in l:
    print(f"The factors of {num}:")
    for i in range(1, num + 1):
        if num % i == 0:
            print(i)
    print('-' * 20)