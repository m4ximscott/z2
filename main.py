def arihmetic(a, b, c):
    if c == '*':
        print(a * b)
    elif c == '+':
        print(a + b)
    elif c == '-':
        print(a - b)
    elif c == "//":
        print(a / b)
    else:
        print('Неизвестная строка')

arihmetic(3, 2, "*")
