import ast 
import asyncio
from pysyncobj import SyncObj, replicated


class HashTable(SyncObj):

    def __init__ (self, selfNodeAddr, otherNodeAddrs):
        self.table={}
        super(HashTable, self).__init__(selfNodeAddr, otherNodeAddrs)
        # print('Carregando de arquivo...')
        # f = open("tablefile", "r")
        # contents = f.read()
        # self.table = ast.literal_eval(contents)
        # f.close()
        
    def set(self, key, ts, data):
        if key in self.table:
            return ('ERROR', self.table[key])

        self.auxSet(key, ts, data)
        return ('SUCCESS', None)


    @replicated
    def auxSet(self, key, ts, data):
        self.table.update({key: (1, ts, data)})

    def get(self, key):
        if key in self.table:
            return ('SUCCESS', self.table[key]) 

        return ('ERROR', None)

    def delete(self, key, version = None):
        if not version:
            if key in self.table:
                removed = self.table[key]
                self.auxDelete(key)
                return ('SUCCESS', removed)

            return ('ERROR', None)

        if key in self.table:
            if self.table[key][0] == version:
                removed = self.table[key]
                self.auxDelete(key)
                return ('SUCCESS', removed)
            
            return ('ERROR_WV', self.table[key])

        return ('ERROR_NE', None)

    @replicated
    def auxDelete(self, key):
        self.table.pop(key)


    def testAndSet(self, key, newValue, version):
        # newValue[0]: version
        # newValue[1]: ts
        # newValue[2]: data

        if key in self.table:
            if self.table[key][0] == version:
                oldValue = self.table[key]
                self.auxTestAndSet(key, newValue)
                return ('SUCCESS', oldValue)

            return ('ERROR_WV', self.table[key])
        
        return ('ERROR_NE', None)

    @replicated
    def auxTestAndSet(self, key, newValue):
        self.table.update({key: newValue})


    def showTable(self):
        print(self.table)

    def saveToDisk(self):
        f = open("tablefile", "w")
        f.write(str(self.table))
        f.close()
    