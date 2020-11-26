
class HashTable:

    def __init__ (self):
        self.table = {}

    
    def set(self, key, ts, data):
        if key in self.table:
            return ('ERROR', self.table[key])

        self.table.update({key: (1, ts, data)})
        return ('SUCCESS', None)

    def get(self, key):
        if key in self.table:
            return ('SUCCESS', self.table[key]) 

        return ('ERROR', None)

    def delete(self, key, version = None):
        if not version:
            if key in self.table:
                removed = self.table.pop(key)
                return ('SUCCESS', removed)

            return ('ERROR', None)

        if key in self.table:
            if self.table[key][0] == version:
                removed = self.table.pop(key)
                return ('SUCCESS', removed)
            
            return ('ERROR_WV', self.table[key])

        return ('ERROR_NE', None)

    def testAndSet(self, key, newValue, version):
        # newValue[0]: version
        # newValue[1]: ts
        # newValue[2]: data

        if key in self.table:
            if self.table[key][0] == version:
                oldValue = self.table[key]
                self.table.update({key: newValue})
                return ('SUCCESS', oldValue)

            return ('ERROR_WV', self.table[key])
        
        return ('ERROR_NE', None)

    def showTable(self):
        print(self.table)

    def saveToDisk(self):
        f = open("tablefile", "w")
        f.write(str(self.table))
        f.close()
    