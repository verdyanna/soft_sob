# У вас есть массив чисел. Напишите три функции, которые вычисляют сумму этих чисел: с for-циклом, с while-циклом, с рекурсией.
def sum_for_loop(a):
    s = 0
    for x in a:
        s += x
    return s

def sum_while_loop(a):
    s = 0
    n = len(a)
    while n:
        n -= 1
        s += a[n]
    return s

def sum_recursive(a):
    if len(a) == 0:
        return 0
    return a[0] + sum_recursive(a[1:])

if __name__ == '__main__':
    t = [5, 3, 4, 1, 7]
    for f in (sum_for_loop, sum_while_loop, sum_recursive):
        print(f(t))