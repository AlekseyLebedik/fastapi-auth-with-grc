# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import session_pb2 as session__pb2


class SessionServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateSession = channel.unary_unary(
            "/session.SessionService/CreateSession",
            request_serializer=session__pb2.SessionRequest.SerializeToString,
            response_deserializer=session__pb2.SessionResponse.FromString,
        )
        self.ConditionSessionStream = channel.stream_stream(
            "/session.SessionService/ConditionSessionStream",
            request_serializer=session__pb2.ConditionSessionRequest.SerializeToString,
            response_deserializer=session__pb2.ConditionSessionResponse.FromString,
        )


class SessionServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateSession(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ConditionSessionStream(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_SessionServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "CreateSession": grpc.unary_unary_rpc_method_handler(
            servicer.CreateSession,
            request_deserializer=session__pb2.SessionRequest.FromString,
            response_serializer=session__pb2.SessionResponse.SerializeToString,
        ),
        "ConditionSessionStream": grpc.stream_stream_rpc_method_handler(
            servicer.ConditionSessionStream,
            request_deserializer=session__pb2.ConditionSessionRequest.FromString,
            response_serializer=session__pb2.ConditionSessionResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "session.SessionService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class SessionService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateSession(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/session.SessionService/CreateSession",
            session__pb2.SessionRequest.SerializeToString,
            session__pb2.SessionResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def ConditionSessionStream(
        request_iterator,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.stream_stream(
            request_iterator,
            target,
            "/session.SessionService/ConditionSessionStream",
            session__pb2.ConditionSessionRequest.SerializeToString,
            session__pb2.ConditionSessionResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
