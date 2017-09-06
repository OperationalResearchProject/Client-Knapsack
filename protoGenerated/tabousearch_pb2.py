# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tabousearch.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import messages_pb2 as messages__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tabousearch.proto',
  package='ts',
  syntax='proto3',
  serialized_pb=_b('\n\x11tabousearch.proto\x12\x02ts\x1a\x0emessages.proto2\xba\x01\n\x12TabouSearchService\x12>\n\x0fInitTransaction\x12\x17.InitTransactionRequest\x1a\x10.FitnessResponse\"\x00\x12\x32\n\x0bSendFitness\x12\x0f.FitnessRequest\x1a\x10.FitnessResponse\"\x00\x12\x30\n\x0fStopTransaction\x12\x0c.StopRequest\x1a\r.StopResponse\"\x00\x62\x06proto3')
  ,
  dependencies=[messages__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_TABOUSEARCHSERVICE = _descriptor.ServiceDescriptor(
  name='TabouSearchService',
  full_name='ts.TabouSearchService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=42,
  serialized_end=228,
  methods=[
  _descriptor.MethodDescriptor(
    name='InitTransaction',
    full_name='ts.TabouSearchService.InitTransaction',
    index=0,
    containing_service=None,
    input_type=messages__pb2._INITTRANSACTIONREQUEST,
    output_type=messages__pb2._FITNESSRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SendFitness',
    full_name='ts.TabouSearchService.SendFitness',
    index=1,
    containing_service=None,
    input_type=messages__pb2._FITNESSREQUEST,
    output_type=messages__pb2._FITNESSRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='StopTransaction',
    full_name='ts.TabouSearchService.StopTransaction',
    index=2,
    containing_service=None,
    input_type=messages__pb2._STOPREQUEST,
    output_type=messages__pb2._STOPRESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_TABOUSEARCHSERVICE)

DESCRIPTOR.services_by_name['TabouSearchService'] = _TABOUSEARCHSERVICE

try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities


  class TabouSearchServiceStub(object):
    # missing associated documentation comment in .proto file
    pass

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.InitTransaction = channel.unary_unary(
          '/ts.TabouSearchService/InitTransaction',
          request_serializer=messages__pb2.InitTransactionRequest.SerializeToString,
          response_deserializer=messages__pb2.FitnessResponse.FromString,
          )
      self.SendFitness = channel.unary_unary(
          '/ts.TabouSearchService/SendFitness',
          request_serializer=messages__pb2.FitnessRequest.SerializeToString,
          response_deserializer=messages__pb2.FitnessResponse.FromString,
          )
      self.StopTransaction = channel.unary_unary(
          '/ts.TabouSearchService/StopTransaction',
          request_serializer=messages__pb2.StopRequest.SerializeToString,
          response_deserializer=messages__pb2.StopResponse.FromString,
          )


  class TabouSearchServiceServicer(object):
    # missing associated documentation comment in .proto file
    pass

    def InitTransaction(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def SendFitness(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def StopTransaction(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_TabouSearchServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'InitTransaction': grpc.unary_unary_rpc_method_handler(
            servicer.InitTransaction,
            request_deserializer=messages__pb2.InitTransactionRequest.FromString,
            response_serializer=messages__pb2.FitnessResponse.SerializeToString,
        ),
        'SendFitness': grpc.unary_unary_rpc_method_handler(
            servicer.SendFitness,
            request_deserializer=messages__pb2.FitnessRequest.FromString,
            response_serializer=messages__pb2.FitnessResponse.SerializeToString,
        ),
        'StopTransaction': grpc.unary_unary_rpc_method_handler(
            servicer.StopTransaction,
            request_deserializer=messages__pb2.StopRequest.FromString,
            response_serializer=messages__pb2.StopResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'ts.TabouSearchService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaTabouSearchServiceServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def InitTransaction(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def SendFitness(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def StopTransaction(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaTabouSearchServiceStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def InitTransaction(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()
    InitTransaction.future = None
    def SendFitness(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()
    SendFitness.future = None
    def StopTransaction(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()
    StopTransaction.future = None


  def beta_create_TabouSearchService_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('ts.TabouSearchService', 'InitTransaction'): messages__pb2.InitTransactionRequest.FromString,
      ('ts.TabouSearchService', 'SendFitness'): messages__pb2.FitnessRequest.FromString,
      ('ts.TabouSearchService', 'StopTransaction'): messages__pb2.StopRequest.FromString,
    }
    response_serializers = {
      ('ts.TabouSearchService', 'InitTransaction'): messages__pb2.FitnessResponse.SerializeToString,
      ('ts.TabouSearchService', 'SendFitness'): messages__pb2.FitnessResponse.SerializeToString,
      ('ts.TabouSearchService', 'StopTransaction'): messages__pb2.StopResponse.SerializeToString,
    }
    method_implementations = {
      ('ts.TabouSearchService', 'InitTransaction'): face_utilities.unary_unary_inline(servicer.InitTransaction),
      ('ts.TabouSearchService', 'SendFitness'): face_utilities.unary_unary_inline(servicer.SendFitness),
      ('ts.TabouSearchService', 'StopTransaction'): face_utilities.unary_unary_inline(servicer.StopTransaction),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_TabouSearchService_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('ts.TabouSearchService', 'InitTransaction'): messages__pb2.InitTransactionRequest.SerializeToString,
      ('ts.TabouSearchService', 'SendFitness'): messages__pb2.FitnessRequest.SerializeToString,
      ('ts.TabouSearchService', 'StopTransaction'): messages__pb2.StopRequest.SerializeToString,
    }
    response_deserializers = {
      ('ts.TabouSearchService', 'InitTransaction'): messages__pb2.FitnessResponse.FromString,
      ('ts.TabouSearchService', 'SendFitness'): messages__pb2.FitnessResponse.FromString,
      ('ts.TabouSearchService', 'StopTransaction'): messages__pb2.StopResponse.FromString,
    }
    cardinalities = {
      'InitTransaction': cardinality.Cardinality.UNARY_UNARY,
      'SendFitness': cardinality.Cardinality.UNARY_UNARY,
      'StopTransaction': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'ts.TabouSearchService', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
