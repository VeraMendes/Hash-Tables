# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next_1 = None
    def __str__(self):
        return f'<{self.key},{self.value}>'

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        # Start from an arbitrary large prime
        hash_value = 5381
        # Bit-shift and sum value for each character
        for char in key:
            hash_djb2 = ((hash_value << 5) + hash_value) + char
        return hash_djb2


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.
        '''
        # # hashmod the key to find the bucket
        # i = self._hash_mod(key)
        # # check if pair already exists in the bucket
        # pair = self.storage[i]

        # if pair is not None:
        #     # if so, overwrite the key/value and throw a warning
        #     if pair.key != key:
        #         print("Warning:Overwriting value")
        #         pair.key = key
        #     pair.value = value
        # else:
        #     # if not, create a new LikedPair and place it in the bucket
        #     self.storage[i] = LinkedPair(key, value)




    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.
        '''
#         i = self._hash_mod(key)
# ​
#         # Check if a pair exists in the bucket with matching keys
#         if self.storage[i] is not None and self.storage[i].key == key:
#             # If so, remove that pair
#             self.storage[i] = None
#         else:
#             # Else print warning
#             print("Warning: Key does not exist")


        i = self._hash_mod(key)
        node = self.storage[i]
  
        while node:
            if node.key == key:
                node = None
                return
            node = node.next_1
        print("Key was not found!")


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.
        '''
        # # get the index from hashmod
        # i = self._hash_mod(key)
        # #check if a pair exists in the bucket with matching keys
        # if self.storage[i] is not None and self.storage[key] == key:
        #     # if so, return the value
        #     return self.storage[i].value
        # else:
        #     # else return None
        #     return None

        while node:
            if node.key == key:
                return node.value
            node = node.next_1

        return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.
        '''
        pass



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
