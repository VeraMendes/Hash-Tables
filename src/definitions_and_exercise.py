"""
What is an array and how does it work?
* Stores a sequence of elements
* Each element must be the same data type
* Occupies a contiguous block of memory
* Can access access data in constant time with this equation: 
memory_address = starting_address + index * data_size

What is an hash function and how does it work?
* Deterministic: For a given input, the output will always be the same.
* Defined output range: For a hash table of size 16,
all keys must hash to a value 0-15. For smaller values,
this is usually accomplished using the modulo % operation.
* Predictable Speed: Hash functions for hash tables should
be lightning fast while cryptographic hashes (like bcrypt) should be very slow.
* Non-invertible: You should not be able to reconstruct the
input value from the output. This trait is important in cryptographic
hashes but not necessary for general hash tables.

What is a hash table and how does it work?
* Hash Tables have an underlying Array structure
* This is why they are as fast at accessing elements as arrays
* The main difference is that Hash Tables are indexed using a hash function in an unordered fashion, whereas arrays are indexed via contiguous ordered indices
* HashTable code is fairly similar to DynamicArray code
"""

# whiteboard
# Add up and print the sum of the all of the minimum elements of each inner array:
arr = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]

# 4 + (-1) + 9 + (-56) + 201 + 18 = 175

# 6 elements
# find the minimum value of each array inside the bigger array
# sum these elements up

# [8,4] = arr[0]
# 8 = arr[0][0]


def minimum_numbers_sum(array):
    # access every element of the array
    minimum_values_storage = 0
    for element in array:    # O(n) 6
        # access the min value of that element
        minimum_value = min(element)   # O(n) 
        # sum the min values for all the elements
        minimum_values_storage += minimum_value
    return minimum_values_storage


print(minimum_numbers_sum(arr))
