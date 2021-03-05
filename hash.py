class HashTable:
    def __init__(self):
        self.max = 23
        self.arr = [[] for i in range(self.max)]

    def get_hash(self, key):
        hash = 0
        for letter in key:
            hash += ord(letter)
        return hash % self.max

    def add(self, key, value):
        hash = self.get_hash(key)
        found = False
        for idx, elem in enumerate(self.arr[hash]):
            if elem[0] == key:
                self.arr[hash][idx] = (key, value)
                found = True
        if not found:
            self.arr[hash].append((key, value))

    def search(self, key):
        hash = self.get_hash(key)
        for elem in self.arr[hash]:
            if elem[0] == key:
                return elem[1]

    def delete(self, key):
        hash = self.get_hash(key)
        for idx, elem in enumerate(self.arr[hash]):
            if elem[0] == key:
                del self.arr[hash][idx]

hash_table = HashTable()
hash_table.add('Patrick', 'Lady Gaga')
hash_table.add('Dave', 'Thin Lizzy')
hash_table.add('Taylor', 'Hot Mulligan')
hash_table.add('Ilka', 'U2')
hash_table.add('Jeremiah', 'Offspring')
hash_table.add('Kenny', 'Blink 182')
hash_table.add('evaD', 'ELO')
hash_table.delete('evaD')
hash_table.delete('Dave')
print(hash_table.arr)