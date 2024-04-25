import hashlib

class HashTable:
    """
    The Hash table data structure stores elements in key-value pairs where
        i. Key- unique integer that is used for indexing the values
        ii. Value - data that are associated with keys
        
    eg: Python Dictionery
    
    When the hash function generates the same index for multiple keys, there will
    be a conflict (what value to be stored in that index). This is called a hash
    collision.
    
    We can resolve the hash collision using one of the following techniques.
        1.Collision resolution by chaining
        2.Open Addressing: Linear/Quadratic Probing and Double Hashing
    """

    def __init__(self, size, load_factor) -> None:
        """
        Initialize the HashTable object.
        
        Parameters:
        - size (int): The initial size of the hash table.
        - load_factor (float): The load factor threshold for resizing the hash
        table.
        """
        self.size = size
        self.load_factor = load_factor
        self.threshold = int(self.load_factor * self.size)
        self.count = 0
        self.table = [[] for i in range(self.size)]
        self.original_size = size

    def hash(self, key):
        """
        Compute the hash value of the given key using SHA-256.
        
        Parameters:
        - key (str): The key to be hashed.
        
        Returns:
        - int: The hash value of the key within the range of the hash table size.
        """
        h = hashlib.sha256(key.encode())
        return int(h.hexdigest(), 16) % self.size

    def _resize(self):
        """
        Resize the hash table by doubling its size and rehashing all existing key-value pairs.
        """
        new_size = self.size * 2
        new_table = [[] for i in range(new_size)]
        
        for bucket in self.table:
            for key, value in bucket:
                new_index = self.hash(key) % new_size
                new_table[new_index].append((key, value))
                
        self.size = new_size
        self.threshold = int(new_size * self.load_factor)
        self.table = new_table

    def __setitem__(self, key, value):
        """
        Insert a key-value pair into the hash table.

        Parameters:
        - key (str): The key to insert.
        - value: The value associated with the key.
        """
        index = self.hash(key)
        bucket = self.table[index]
        
        for k, _ in bucket:
            if k == key:
                # Update the value if the key already exists
                bucket[bucket.index((k, _))] = (key, value)
                return
        bucket.append((key, value))
        if len(bucket) == 1:
            self.count += 1
        if self.count > self.threshold:
            self._resize()

    def __getitem__(self, key):
        """
        Retrieve the value associated with the given key from the hash table.
        
        Parameters:
        - key (str): The key to retrieve the value for.
        
        Returns:
        - value: The value associated with the key.
        
        Raises:
        - KeyError: If the key is not found in the hash table.
        """
        index = self.hash(key)
        bucket = self.table[index]
        
        for idx, (k, _) in enumerate(bucket):
            if k == key:
                return bucket[idx]
        raise KeyError(f"Key({key}) not found in the hash table")

    def __delitem__(self, key):
        """
        Delete the key-value pair with the given key from the hash table.
        
        Parameters:
        - key (str): The key to delete.
        
        Raises:
        - KeyError: If the key is not found in the hash table.
        """
        index = self.hash(key)
        bucket = self.table[index]
        
        for idx, (k, _) in enumerate(bucket):
            if k == key:
                del bucket[idx]
                if len(bucket) == 0:
                    self.count -= 1
                return
        raise KeyError(f"Key({key}) not found in the hash table")

    def clear(self):
        """
        Clear the hash table by resetting it to its original size and state.
        """
        self.size = self.original_size
        self.threshold = int(self.size * self.load_factor)
        self.table = [[] for i in range(self.size)]
        self.count = 0


hash = HashTable(10, 0.75)
hash["apple"] = 2
hash["Apple"] = 3
hash["watch"] = 1
hash["apple"] = 4
print(hash["apple"])
del hash["apple"]
# del hash["Apple"]
hash.clear()
print(hash.table)
