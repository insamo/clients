# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: auth/rules.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import auth_pb2 as auth__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='auth/rules.proto',
  package='go.micro.auth',
  syntax='proto3',
  serialized_pb=_b('\n\x10\x61uth/rules.proto\x12\rgo.micro.auth\x1a\nauth.proto\"r\n\x04Rule\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04role\x18\x02 \x01(\t\x12)\n\x08resource\x18\x03 \x01(\x0b\x32\x17.go.micro.auth.Resource\x12%\n\x06\x61\x63\x63\x65ss\x18\x04 \x01(\x0e\x32\x15.go.micro.auth.Access\"o\n\rCreateRequest\x12\x0c\n\x04role\x18\x01 \x01(\t\x12)\n\x08resource\x18\x02 \x01(\x0b\x32\x17.go.micro.auth.Resource\x12%\n\x06\x61\x63\x63\x65ss\x18\x03 \x01(\x0e\x32\x15.go.micro.auth.Access\"\x10\n\x0e\x43reateResponse\"o\n\rDeleteRequest\x12\x0c\n\x04role\x18\x01 \x01(\t\x12)\n\x08resource\x18\x02 \x01(\x0b\x32\x17.go.micro.auth.Resource\x12%\n\x06\x61\x63\x63\x65ss\x18\x03 \x01(\x0e\x32\x15.go.micro.auth.Access\"\x10\n\x0e\x44\x65leteResponse\"\r\n\x0bListRequest\"2\n\x0cListResponse\x12\"\n\x05rules\x18\x01 \x03(\x0b\x32\x13.go.micro.auth.Rule*.\n\x06\x41\x63\x63\x65ss\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07GRANTED\x10\x01\x12\n\n\x06\x44\x45NIED\x10\x02\x32\xdc\x01\n\x05Rules\x12G\n\x06\x43reate\x12\x1c.go.micro.auth.CreateRequest\x1a\x1d.go.micro.auth.CreateResponse\"\x00\x12G\n\x06\x44\x65lete\x12\x1c.go.micro.auth.DeleteRequest\x1a\x1d.go.micro.auth.DeleteResponse\"\x00\x12\x41\n\x04List\x12\x1a.go.micro.auth.ListRequest\x1a\x1b.go.micro.auth.ListResponse\"\x00\x42\x0bZ\tauth;authb\x06proto3')
  ,
  dependencies=[auth__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_ACCESS = _descriptor.EnumDescriptor(
  name='Access',
  full_name='go.micro.auth.Access',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GRANTED', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DENIED', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=492,
  serialized_end=538,
)
_sym_db.RegisterEnumDescriptor(_ACCESS)

Access = enum_type_wrapper.EnumTypeWrapper(_ACCESS)
UNKNOWN = 0
GRANTED = 1
DENIED = 2



_RULE = _descriptor.Descriptor(
  name='Rule',
  full_name='go.micro.auth.Rule',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='go.micro.auth.Rule.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='role', full_name='go.micro.auth.Rule.role', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='resource', full_name='go.micro.auth.Rule.resource', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='access', full_name='go.micro.auth.Rule.access', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=47,
  serialized_end=161,
)


_CREATEREQUEST = _descriptor.Descriptor(
  name='CreateRequest',
  full_name='go.micro.auth.CreateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='role', full_name='go.micro.auth.CreateRequest.role', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='resource', full_name='go.micro.auth.CreateRequest.resource', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='access', full_name='go.micro.auth.CreateRequest.access', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=163,
  serialized_end=274,
)


_CREATERESPONSE = _descriptor.Descriptor(
  name='CreateResponse',
  full_name='go.micro.auth.CreateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=276,
  serialized_end=292,
)


_DELETEREQUEST = _descriptor.Descriptor(
  name='DeleteRequest',
  full_name='go.micro.auth.DeleteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='role', full_name='go.micro.auth.DeleteRequest.role', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='resource', full_name='go.micro.auth.DeleteRequest.resource', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='access', full_name='go.micro.auth.DeleteRequest.access', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=294,
  serialized_end=405,
)


_DELETERESPONSE = _descriptor.Descriptor(
  name='DeleteResponse',
  full_name='go.micro.auth.DeleteResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=407,
  serialized_end=423,
)


_LISTREQUEST = _descriptor.Descriptor(
  name='ListRequest',
  full_name='go.micro.auth.ListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=425,
  serialized_end=438,
)


_LISTRESPONSE = _descriptor.Descriptor(
  name='ListResponse',
  full_name='go.micro.auth.ListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rules', full_name='go.micro.auth.ListResponse.rules', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=440,
  serialized_end=490,
)

_RULE.fields_by_name['resource'].message_type = auth__pb2._RESOURCE
_RULE.fields_by_name['access'].enum_type = _ACCESS
_CREATEREQUEST.fields_by_name['resource'].message_type = auth__pb2._RESOURCE
_CREATEREQUEST.fields_by_name['access'].enum_type = _ACCESS
_DELETEREQUEST.fields_by_name['resource'].message_type = auth__pb2._RESOURCE
_DELETEREQUEST.fields_by_name['access'].enum_type = _ACCESS
_LISTRESPONSE.fields_by_name['rules'].message_type = _RULE
DESCRIPTOR.message_types_by_name['Rule'] = _RULE
DESCRIPTOR.message_types_by_name['CreateRequest'] = _CREATEREQUEST
DESCRIPTOR.message_types_by_name['CreateResponse'] = _CREATERESPONSE
DESCRIPTOR.message_types_by_name['DeleteRequest'] = _DELETEREQUEST
DESCRIPTOR.message_types_by_name['DeleteResponse'] = _DELETERESPONSE
DESCRIPTOR.message_types_by_name['ListRequest'] = _LISTREQUEST
DESCRIPTOR.message_types_by_name['ListResponse'] = _LISTRESPONSE
DESCRIPTOR.enum_types_by_name['Access'] = _ACCESS

Rule = _reflection.GeneratedProtocolMessageType('Rule', (_message.Message,), dict(
  DESCRIPTOR = _RULE,
  __module__ = 'auth.rules_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.auth.Rule)
  ))
_sym_db.RegisterMessage(Rule)

CreateRequest = _reflection.GeneratedProtocolMessageType('CreateRequest', (_message.Message,), dict(
  DESCRIPTOR = _CREATEREQUEST,
  __module__ = 'auth.rules_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.auth.CreateRequest)
  ))
_sym_db.RegisterMessage(CreateRequest)

CreateResponse = _reflection.GeneratedProtocolMessageType('CreateResponse', (_message.Message,), dict(
  DESCRIPTOR = _CREATERESPONSE,
  __module__ = 'auth.rules_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.auth.CreateResponse)
  ))
_sym_db.RegisterMessage(CreateResponse)

DeleteRequest = _reflection.GeneratedProtocolMessageType('DeleteRequest', (_message.Message,), dict(
  DESCRIPTOR = _DELETEREQUEST,
  __module__ = 'auth.rules_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.auth.DeleteRequest)
  ))
_sym_db.RegisterMessage(DeleteRequest)

DeleteResponse = _reflection.GeneratedProtocolMessageType('DeleteResponse', (_message.Message,), dict(
  DESCRIPTOR = _DELETERESPONSE,
  __module__ = 'auth.rules_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.auth.DeleteResponse)
  ))
_sym_db.RegisterMessage(DeleteResponse)

ListRequest = _reflection.GeneratedProtocolMessageType('ListRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTREQUEST,
  __module__ = 'auth.rules_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.auth.ListRequest)
  ))
_sym_db.RegisterMessage(ListRequest)

ListResponse = _reflection.GeneratedProtocolMessageType('ListResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTRESPONSE,
  __module__ = 'auth.rules_pb2'
  # @@protoc_insertion_point(class_scope:go.micro.auth.ListResponse)
  ))
_sym_db.RegisterMessage(ListResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z\tauth;auth'))
# @@protoc_insertion_point(module_scope)