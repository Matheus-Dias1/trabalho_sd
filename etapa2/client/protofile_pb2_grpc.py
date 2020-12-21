# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import protofile_pb2 as protos_dot_protofile__pb2


class DBServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SET = channel.unary_unary(
                '/demo.DBService/SET',
                request_serializer=protos_dot_protofile__pb2.RequestSET.SerializeToString,
                response_deserializer=protos_dot_protofile__pb2.ResponseSET.FromString,
                )
        self.GET = channel.unary_unary(
                '/demo.DBService/GET',
                request_serializer=protos_dot_protofile__pb2.RequestGET.SerializeToString,
                response_deserializer=protos_dot_protofile__pb2.ResponseGET.FromString,
                )
        self.DEL = channel.unary_unary(
                '/demo.DBService/DEL',
                request_serializer=protos_dot_protofile__pb2.RequestDEL.SerializeToString,
                response_deserializer=protos_dot_protofile__pb2.ResponseDEL.FromString,
                )
        self.TESTANDSET = channel.unary_unary(
                '/demo.DBService/TESTANDSET',
                request_serializer=protos_dot_protofile__pb2.RequestTESTANDSET.SerializeToString,
                response_deserializer=protos_dot_protofile__pb2.ResponseTESTANDSET.FromString,
                )


class DBServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SET(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not asdasdsda!')

    def GET(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DEL(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TESTANDSET(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DBServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SET': grpc.unary_unary_rpc_method_handler(
                    servicer.SET,
                    request_deserializer=protos_dot_protofile__pb2.RequestSET.FromString,
                    response_serializer=protos_dot_protofile__pb2.ResponseSET.SerializeToString,
            ),
            'GET': grpc.unary_unary_rpc_method_handler(
                    servicer.GET,
                    request_deserializer=protos_dot_protofile__pb2.RequestGET.FromString,
                    response_serializer=protos_dot_protofile__pb2.ResponseGET.SerializeToString,
            ),
            'DEL': grpc.unary_unary_rpc_method_handler(
                    servicer.DEL,
                    request_deserializer=protos_dot_protofile__pb2.RequestDEL.FromString,
                    response_serializer=protos_dot_protofile__pb2.ResponseDEL.SerializeToString,
            ),
            'TESTANDSET': grpc.unary_unary_rpc_method_handler(
                    servicer.TESTANDSET,
                    request_deserializer=protos_dot_protofile__pb2.RequestTESTANDSET.FromString,
                    response_serializer=protos_dot_protofile__pb2.ResponseTESTANDSET.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'demo.DBService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DBService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SET(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/demo.DBService/SET',
            protos_dot_protofile__pb2.RequestSET.SerializeToString,
            protos_dot_protofile__pb2.ResponseSET.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GET(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/demo.DBService/GET',
            protos_dot_protofile__pb2.RequestGET.SerializeToString,
            protos_dot_protofile__pb2.ResponseGET.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DEL(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/demo.DBService/DEL',
            protos_dot_protofile__pb2.RequestDEL.SerializeToString,
            protos_dot_protofile__pb2.ResponseDEL.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TESTANDSET(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/demo.DBService/TESTANDSET',
            protos_dot_protofile__pb2.RequestTESTANDSET.SerializeToString,
            protos_dot_protofile__pb2.ResponseTESTANDSET.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
