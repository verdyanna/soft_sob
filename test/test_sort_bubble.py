def bubble_sort(arrayToSort):
    a = arrayToSort
    for i in range(len(a),0,-1):
        for j in range(1, i):
            if a[j-1] > a[j]:
                tmp = a[j-1]
                a[j-1] = a[j]
                a[j] = tmp
                print (a)
    return a
ary = [5, 0, 10, 4, 1, 5, 8, 4, 3, 12, 41]
print (bubble_sort(ary))