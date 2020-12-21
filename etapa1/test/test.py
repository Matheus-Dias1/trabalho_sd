import protofile_pb2_grpc as pb2
import protofile_pb2 as pb
import grpc
import os

channel = grpc.insecure_channel('localhost:9090')
stub = pb2.DBServiceStub(channel)


def callGet(k):
   
    key = pb.Key(
        key = k
    ) 
    message = pb.RequestGET(
        key = key
    )
    res = stub.GET(message)
    
    status = res.status
    if status == 'SUCCESS':
        print('\nSucesso ao recuperar chave.\nVersion: {}\nTimestamp: {}\nData: {}'.format(res.value.version, res.value.timestamp, res.value.data.decode()))
        print()
    elif status == 'ERROR':
        print('\nA chava especificada não foi encontrada.\n')


def callSet(k, ts, d):
    d = str.encode(d)
    key = pb.Key(
        key = k
    )
    
    message = pb.RequestSET(
        key = key,
        timestamp = ts,
        data = d
    )
    res = stub.SET(message)
    
    status = res.status
    if status == 'SUCCESS':
        print('\nA entrada foi inserida com sucesso.\n')  
    elif status == 'ERROR':
        print('\nHá outra entrada com essa mesma chave.\nVersão: {}\nTimestamp: {}\nData: {}'.format(res.value.version, res.value.timestamp, res.value.data.decode()))
        print('\n')

def callDel(k, vers):
    key = pb.Key(
        key = k
    )
    
    message = pb.RequestDEL(
        key = key,
        version = vers
    )
    res = stub.DEL(message)
    status = res.status

    if vers == None:
        if status == 'SUCCESS':
            print('\nEntrada excluída com sucesso.\nVersão: {}\nTimestamp: {}\nData: {}'.format(res.value.version, res.value.timestamp, res.value.data.decode()))
            print('\n')
        elif status == 'ERROR':
            print('\nA chava especificada não foi encontrada.\n')
    else:
        if status == 'SUCCESS':
            print('\nEntrada excluída com sucesso.\nVersão: {}\nTimestamp: {}\nData: {}'.format(res.value.version, res.value.timestamp, res.value.data.decode()))
            print('\n')
        if status == 'ERROR_NE':
            print('Não foi encontrada nenhuma entrada com o valor de chave informada.\n')
        elif status == 'ERROR_WV': 
            print('Uma entrada com a chave especificada foi encontrada, mas não na versão informada.\n')

def callTestAndSet(k, oldVers, ts, d, newVers):
    d = str.encode(d)
    key = pb.Key(
        key = k
    )
    value = pb.Value(
        version = newVers,
        timestamp = ts,
        data = d
    )
    keyValue = pb.KeyValue(
        key = key,
        value = value
    )
    
    message = pb.RequestTESTANDSET(
        keyValue = keyValue,
        version = oldVers
    )
    res = stub.TESTANDSET(message)
    
    status = res.status
    if status == 'SUCCESS':
        print('\nA nova entrada foi inserida com sucesso, sobrescrevendo a seguinte:\nVersão: {}\nTimestamp: {}\nData: {}'.format(res.value.version, res.value.timestamp, res.value.data.decode()))
        print('\n')
    elif status == 'ERROR_NE':
        print('Não foi encontrada nenhuma entrada com o valor de chave informada.\n')
    elif status == 'ERROR_WV': 
        print('\nUma entrada foi encontrada com a chave especificada, mas em uma versão diferente da especificada\nVersão: {}\nTimestamp: {}\nData: {}'.format(res.value.version, res.value.timestamp, res.value.data.decode()))
        print('\n')





# for i in range(1000):
#     callSet(i, 0, 'teste' + str(i))


# for i in range(1000):
#     callTestAndSet(i, 1, 2, 'atualizado'+ str(i), 2)

for i in range(1000):
    callGet(i)


    


