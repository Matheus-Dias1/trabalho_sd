import protofile_pb2_grpc as pb2
import protofile_pb2 as pb
import grpc
import os

channel = grpc.insecure_channel('localhost:9090')
stub = pb2.DBServiceStub(channel)
os.system('cls')

def callGet():
    k = int(input('Key: '))
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
        input('\nPressione ENTER para continuar...')
    elif status == 'ERROR':
        print('\nA chava especificada não foi encontrada.\nPressione ENTER para continuar...')


def callSet():
    k = int(input('Key: '))
    ts = int(input('Timestamp: '))
    d = str.encode(input('Data: '))
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
        input('\nA entrada foi inserida com sucesso.\nPressione ENTER para continuar...')  
    elif status == 'ERROR':
        print('\nHá outra entrada com essa mesma chave.\nVersão: {}\nTimestamp: {}\nData: {}'.format(res.value.version, res.value.timestamp, res.value.data.decode()))
        input('\nPressione ENTER para continuar...')

def callDel():
    k = int(input('Key: '))
    vers = input('Versão (opcional): ')
    if vers == '':
        vers = None
    else:
        vers = int(vers)

    
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
            input('\nPressione ENTER para continuar...')
        elif status == 'ERROR':
            print('\nA chava especificada não foi encontrada.\nPressione ENTER para continuar...')
    else:
        if status == 'SUCCESS':
            print('\nEntrada excluída com sucesso.\nVersão: {}\nTimestamp: {}\nData: {}'.format(res.value.version, res.value.timestamp, res.value.data.decode()))
            input('\nPressione ENTER para continuar...')
        if status == 'ERROR_NE':
            input('Não foi encontrada nenhuma entrada com o valor de chave informada.\nPressione ENTER para continuar...')
        elif status == 'ERROR_WV': 
            input('Uma entrada com a chave especificada foi encontrada, mas não na versão informada.\nPressione ENTER para continuar...')

def callTestAndSet():
    k = int(input('Key: '))
    oldVers = int(input('Old version: '))
    ts = int(input('Timestamp: '))
    d = str.encode(input('Data: '))
    newVers = int(input('New version: '))
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
        input('\nPressione ENTER para continuar...')
    elif status == 'ERROR_NE':
        input('Não foi encontrada nenhuma entrada com o valor de chave informada.\nPressione ENTER para continuar...')
    elif status == 'ERROR_WV': 
        print('\nUma entrada foi encontrada com a chave especificada, mas em uma versão diferente da especificada\nVersão: {}\nTimestamp: {}\nData: {}'.format(res.value.version, res.value.timestamp, res.value.data.decode()))
        input('\nPressione ENTER para continuar...')

while True:
    op = input('\n\nEscolha uma opção:\n1 - GET\n2 - SET\n3 - DEL\n4 - TEST AND SET\n5 - SAIR\n\n').strip()
    
    if op == '1':
        os.system('cls')
        callGet()

    elif op == '2':
        os.system('cls')
        callSet()

    elif op == '3':
        os.system('cls')
        callDel()

    elif op == '4':
        os.system('cls')
        callTestAndSet()

    elif op == '5':
        break

    else:
        print('Opção inválida, escolha uma opção válida.\n')


