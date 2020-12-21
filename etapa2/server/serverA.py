from src.HashTable import HashTable
from concurrent import futures
from protos.protofile_pb2_grpc import *
from protos.protofile_pb2 import *
import time, threading, asyncio
import sys

# def periodicalSave():
#     sem.acquire()
#     print('Salvando em arquivo...')
#     table.saveToDisk()
#     threading.Timer(float(sys.argv[1]), periodicalSave).start()
    
#     sem.release()

def periodicalPrint():
    sem.acquire()
    table.showTable()
    threading.Timer(5, periodicalPrint).start()
    
    sem.release()

table = HashTable('localhost:9090', ['localhost:9091', 'localhost:9092'])
sem = threading.Semaphore(11)
# periodicalSave()
periodicalPrint()


class DBServiceServicer(DBServiceServicer):
    def __init__ (self):

        self.t = table


    def GET(self, request, context):
        sem.acquire()
        
        ret = self.t.get(request.key.key)
        if ret[1] == None:
            value = None
        else:
            value = value = Value (
                version = ret[1][0],
                timestamp = ret[1][1],
                data = ret[1][2]
            )
        sem.release()
        return ResponseGET (
            status = ret[0],
            value = value
        )
        
    def SET(self, request, context):
        sem.acquire()
        
        key = request.key.key
        ts = request.timestamp
        data = request.data

        
        ret = self.t.set(key, ts, data)
        if ret[1] == None:
            value = None
        else:
            value = value = Value (
                version = ret[1][0],
                timestamp = ret[1][1],
                data = ret[1][2]
            )
        
        sem.release()
        return ResponseSET (
            status = ret[0],
            value = value
        )

        
    def DEL(self, request, context):
        sem.acquire()
        key = request.key.key
        version = request.version
        if not version:
            version = None

        
        ret = self.t.delete(key, version)
        if ret[1] == None:
            value = None
        else:
            value = value = Value (
                version = ret[1][0],
                timestamp = ret[1][1],
                data = ret[1][2]
            )
        sem.release()
        return ResponseDEL (
            status = ret[0],
            value = value
        )

        
            
    def TESTANDSET(self, request, context):
        sem.acquire()

        key = request.keyValue.key.key
        oldVers = request.version
        newVers = request.keyValue.value.version
        ts = request.keyValue.value.timestamp
        data = request.keyValue.value.data


        
        ret = self.t.testAndSet(key, (newVers, ts, data), oldVers)

        if ret[1] == None:
            value = None
        else:
            value = value = Value (
                version = ret[1][0],
                timestamp = ret[1][1],
                data = ret[1][2]
            )
        sem.release()
        return ResponseSET (
            status = ret[0],
            value = value
        )

        
            


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_DBServiceServicer_to_server(
        DBServiceServicer(), server)
    server.add_insecure_port('localhost:9090')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()

    