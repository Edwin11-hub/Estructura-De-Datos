# Edwin Yair Molina Cerón - 408873

def insertion_sort(A):
    N = len(A)
    for i in range(1, N):
        current = A[i]
        j = i - 1
        while j >= 0 and A[j] > current:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = current

# Lista
A = [61,82,67,4,98,20,37,85]
insertion_sort(A)
print(A)