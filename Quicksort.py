#Python HW 1
#Translating a C++ quicksort algorithm to python
#HW1P3Brennan

def print_f(inp):
    for i in inp:
        print(i)

def partition (arr, p, r):
    pivot = arr[r]

    while (p < r):
        while (arr[p] < pivot):
            p += 1
        while (arr[r] > pivot):
            r -= 1
        if (arr[p] == arr[r]):
            p += 1
        elif (p < r):
            tmp = arr[p]
            arr[p] = arr [r]
            arr[r] = tmp

    return r


def quicksort (arr, p, r):
    if (p < r):
        j = partition(arr,p,r)
        quicksort(arr, p, j-1)
        quicksort(arr, j+1, r)



check = [500, 700, 800, 100, 300, 200, 900, 400, 1000, 600]
print('Input: ')
print_f(check)
quicksort(check, 0, 9)

print('Output: ')
print_f(check)




    
