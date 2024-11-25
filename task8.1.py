def sum_nested_list(nested_list):
    
    total = 0
    for element in nested_list:
        if isinstance(element, list):  # If the element is a list
            total += sum_nested_list(element)  # Recursively sum the nested list
        else:
            total += element  # If the element is a number, add it to the total
    return total

# Test the function with a sample nested list
nested_list = [1, [2, [3, 4], 5], 6, [7, 8]]
result = sum_nested_list(nested_list)
print(f"The total sum of all numbers is: {result}")
