class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hashfunction(self, key):
        return key % self.size

    def rehash(self, oldhash):
        return (oldhash+1) % self.size

    def put(self, key, data):
        hashValue = self.hashfunction(key)

        if self, slots[hashValue] == None:
            self.slots[hashValue] = key
            self.data[hashValue] = data
        else:
            if self.slots[hashValue] == key:
                self.data[hashValue] = data
            else:
                nextslot = self.rehash(hashValue)
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextsolt = self.rehash(nextsolt)

                if self.slots[nextsolt] == None:
                    self.slots[nextsolt] = key
                    self.data[nextsolt] = data
                else:
                    self.data[nextsolt] = data

    def get(self, key):
        startslot = self.hashfunction(key)

        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and not found and not stop:
            if sle.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position)
                if position == startslot:
                    stop = True
        return data
