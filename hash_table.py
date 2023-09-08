class HashTable:
    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hash = self.hashvalue(key, len(self.slots))
        
        if self.slots[hash] == None:
            self.slots[hash] = key
            self.data[hash] = data
        else:
            if self.slots[hash] == key:
                self.data[hash] = data #replace
            else:
                nextslot = self.rehash(hash, len(self.slots))
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(hash, len(self.slots))
                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data #replace

    def hashvalue(self, key, size):
        return key % size

    def rehash(self, oldhash, size):
        return (oldhash + 1) % size

    def get(self, key):
        startslot = self.hashvalue(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot

        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(key, len(self.slots))
                if position == startslot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        return self.put(key, data)

if __name__ == "__main__":
    H = HashTable(11)
    H[54] = "cat"
    H[26] = "dog"
    H[93] = "lion"
    H[17] = "tiger"
    print(H.slots)
    print(H.data)
