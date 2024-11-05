def odwracanie(L, left, right):
    if(left < right):
        L[left], L[right] = L[right], L[left]
        odwracanie(L, left + 1, right - 1)
    return L

L1 = odwracanie([0, 1, 2], 0, 2)
print(L1)
L2 = odwracanie([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20], 0, 6)
print(L2)
L3 = odwracanie([10, 20, 30, 40, 50, 60], 3, 5)
print(L3)