"""
1. First, let's define what a sorting algorithm is. A sorting algorithm is a way to arrange a list of elements in a specific order. There are many different sorting algorithms, each with their own strengths and weaknesses.
2. Here is an example of how to implement the bubble sort algorithm in Python, with comments per line:
"""
# Define a function called bubble_sort that takes a list as an input parameter
def bubble_sort(lst):
    # Get the length of the list
    n = len(lst)
    # Traverse through all elements of the list
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Traverse the list from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    # Return the sorted list
    return lst
"""
3. The function bubble_sort takes a list lst as an input parameter.
4. The variable n is assigned the length of the list.
5. The first loop for i in range(n) is used to traverse through all elements of the list.
6. The second loop for j in range(0, n-i-1) is used to traverse the list from 0 to n-i-1. This loop ensures that the last i elements are already in place.
7. If the element found is greater than the next element, then the elements are swapped.
8. Finally, the sorted list is returned.
