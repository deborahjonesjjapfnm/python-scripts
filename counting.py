from collections import Counter

def count_elements(lst):
    element_counter = Counter(lst)
    return element_counter


my_list = [1, 2, 3, 4, 5, 1, 2, 3, 4, 1]
result = count_elements(my_list)
print("Counting duplicate elements in a list:")
for element, count in result.items():
    print(f"The element {element} occurs {count} times")
