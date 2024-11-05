def sum_seq(sequence):
    total = 0
    for item in sequence:
        if isinstance(item, (list, tuple)):
            total += sum_seq(item)
        elif isinstance(item, (int, float)):
            total += item
    return total


result1 = sum_seq([1, 2, [3, 4, [5, 6]], (7, 8), 9])
print(result1)
result2 = sum_seq([[1,20], 31, [4, [3, 8]]])
print(result2)
result3 = sum_seq([12, [34], [[56], 78, [8, [9]]]])
print(result3)