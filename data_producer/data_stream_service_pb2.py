# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: data_stream_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19\x64\x61ta_stream_service.proto\"\x1b\n\x0bUserRequest\x12\x0c\n\x04list\x18\x01 \x01(\t\"\x10\n\x02ID\x12\n\n\x02id\x18\x01 \x01(\x05\"\x83\x01\n\x08UserData\x12\x0f\n\x02id\x18\x01 \x01(\x0b\x32\x03.ID\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08username\x18\x03 \x01(\t\x12\r\n\x05\x65mail\x18\x04 \x01(\t\x12\x14\n\x0cphone_number\x18\x05 \x01(\t\x12\x10\n\x08modified\x18\x06 \x01(\t\x12\x0f\n\x07\x63reated\x18\x07 \x01(\t\"\'\n\x0cUserDataList\x12\x17\n\x04list\x18\x01 \x03(\x0b\x32\t.UserData2W\n\nDataStream\x12\x1d\n\x0bGetUserByID\x12\x03.ID\x1a\t.UserData\x12*\n\x0bGetUserList\x12\x0c.UserRequest\x1a\r.UserDataListb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'data_stream_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_USERREQUEST']._serialized_start=29
  _globals['_USERREQUEST']._serialized_end=56
  _globals['_ID']._serialized_start=58
  _globals['_ID']._serialized_end=74
  _globals['_USERDATA']._serialized_start=77
  _globals['_USERDATA']._serialized_end=208
  _globals['_USERDATALIST']._serialized_start=210
  _globals['_USERDATALIST']._serialized_end=249
  _globals['_DATASTREAM']._serialized_start=251
  _globals['_DATASTREAM']._serialized_end=338
# @@protoc_insertion_point(module_scope)
