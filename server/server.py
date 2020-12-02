from src.HashTable import HashTable
from concurrent import futures
from protos.protofile_pb2_grpc import *
from protos.protofile_pb2 import *
import time, threading
import sys

class DBServiceServicer(DBServiceServicer):
    def __init__ (self):
        self.t = HashTable()
        self.periodicalSave()

    def periodicalSave(self):
        self.t.saveToDisk()
        threading.Timer(int(sys.argv[1])*60, self.periodicalSave).start()

    def GET(self, request, context):
        ret = self.t.get(request.key.key)
        if ret[1] == None:
            value = None
        else:
            value = value = Value (
                version = ret[1][0],
                timestamp = ret[1][1],
                data = ret[1][2]
            )
        return ResponseGET (
            status = ret[0],
            value = value
        )

    def SET(self, request, context):
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

        return ResponseSET (
            status = ret[0],
            value = value
        )

    def DEL(self, request, context):
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

        return ResponseDEL (
            status = ret[0],
            value = value
        )

    def TESTANDSET(self, request, context):
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

        return ResponseSET (
            status = ret[0],
            value = value
        )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_DBServiceServicer_to_server(
        DBServiceServicer(), server)
    server.add_insecure_port('[::]:8080')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()

    