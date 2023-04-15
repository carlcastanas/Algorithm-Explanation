"""
1. Big-O Space Complexity refers to the amount of memory or space that an algorithm uses.
2. In Python, you can measure the space complexity of an algorithm by analyzing the amount of memory used by the program while it runs.
3. The amount of memory used by a Python program can be monitored using the sys module, which provides functions that allow you to inspect the system and the Python interpreter.
"""
import sys

# Define a function to calculate the sum of a list of integers
def sum_list(numbers):
    result = 0
    for number in numbers:
        result += number
    return result

# Create a list of integers
numbers = [1, 2, 3, 4, 5]

# Call the sum_list function and print the result
print(sum_list(numbers))

# Print the amount of memory used by the program
print(sys.getsizeof(numbers))

"""
4. In the example above, the sum_list function uses a constant amount of memory, since it only creates a single variable (result) to store the sum of the numbers. The amount of memory used by the program is proportional to the size of the numbers list, which is determined by the number of integers in the list and their size in memory.
5. The sys.getsizeof() function returns the size of an object in bytes. In this case, it returns the size of the numbers list, which includes the size of each integer in the list as well as any overhead required to store the list itself.
6. By analyzing the amount of memory used by a Python program, you can determine its space complexity and compare it to other algorithms to find the most efficient solution for a given problem.
