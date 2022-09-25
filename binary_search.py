def binary_search(sequence, value):
    start_value = 0
    end_value = len(sequence) - 1
    while start_value <= end_value:
        midpoint = start_value + (end_value - start_value) // 2
        midpoint_value = sequence[midpoint]
        if midpoint_value == value:
            return midpoint
        elif value < midpoint_value:
            end_value = midpoint - 1
        else:
            start_value = midpoint + 1
    return None


value_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
value = 6
print(binary_search(value_list, value))
