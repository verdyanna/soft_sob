n = [6,8,6,9,4,56]

for i in range(n-1):
    for j in range(i+1,n):
        if i == j:
            print("Есть одинаковые")
            quit()
print("Все элементы уникальны")