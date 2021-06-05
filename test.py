def factorial(num):
    if num < 2:
        return 1
    return num * factorial(num - 1)

for n in range(10):
    print(f'faktorila cisla {n} by mohol byt {factorial(n)}')
