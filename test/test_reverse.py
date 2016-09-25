a = [4,8,6,7,4,92,145]
#1 способ
# a = [int(i) for i in a]
# for i in range(len(a)//2):
#     b = a[i]
#     a[i] = a[len(a)-i-1]
#     a[len(a)-i-1] = b

#2 способ
a.reverse()

# вернуть обратно
#a = a[::-1]
print(a)