# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: newsGrpc.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0enewsGrpc.proto\"\x1b\n\x05Topic\x12\x12\n\ntopic_name\x18\x01 \x01(\t\" \n\x0cNewsHeadline\x12\x10\n\x08headline\x18\x01 \x01(\t\"r\n\x04News\x12\x10\n\x08headline\x18\x01 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x61te\x18\x03 \x01(\t\x12\x0f\n\x07\x61uthors\x18\x04 \x01(\t\x12\x19\n\x11short_description\x18\x05 \x01(\t\x12\x0c\n\x04link\x18\x06 \x01(\t\"!\n\nListOfNews\x12\x13\n\x04News\x18\x01 \x03(\x0b\x32\x05.News22\n\x08newsGrpc\x12&\n\x06Search\x12\r.NewsHeadline\x1a\x0b.ListOfNews\"\x00\x32\x34\n\x0bKafkaBroker\x12%\n\x08\x43onsumer\x12\x06.Topic\x1a\r.NewsHeadline\"\x00\x30\x01\x62\x06proto3')



_TOPIC = DESCRIPTOR.message_types_by_name['Topic']
_NEWSHEADLINE = DESCRIPTOR.message_types_by_name['NewsHeadline']
_NEWS = DESCRIPTOR.message_types_by_name['News']
_LISTOFNEWS = DESCRIPTOR.message_types_by_name['ListOfNews']
Topic = _reflection.GeneratedProtocolMessageType('Topic', (_message.Message,), {
  'DESCRIPTOR' : _TOPIC,
  '__module__' : 'newsGrpc_pb2'
  # @@protoc_insertion_point(class_scope:Topic)
  })
_sym_db.RegisterMessage(Topic)

NewsHeadline = _reflection.GeneratedProtocolMessageType('NewsHeadline', (_message.Message,), {
  'DESCRIPTOR' : _NEWSHEADLINE,
  '__module__' : 'newsGrpc_pb2'
  # @@protoc_insertion_point(class_scope:NewsHeadline)
  })
_sym_db.RegisterMessage(NewsHeadline)

News = _reflection.GeneratedProtocolMessageType('News', (_message.Message,), {
  'DESCRIPTOR' : _NEWS,
  '__module__' : 'newsGrpc_pb2'
  # @@protoc_insertion_point(class_scope:News)
  })
_sym_db.RegisterMessage(News)

ListOfNews = _reflection.GeneratedProtocolMessageType('ListOfNews', (_message.Message,), {
  'DESCRIPTOR' : _LISTOFNEWS,
  '__module__' : 'newsGrpc_pb2'
  # @@protoc_insertion_point(class_scope:ListOfNews)
  })
_sym_db.RegisterMessage(ListOfNews)

_NEWSGRPC = DESCRIPTOR.services_by_name['newsGrpc']
_KAFKABROKER = DESCRIPTOR.services_by_name['KafkaBroker']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _TOPIC._serialized_start=18
  _TOPIC._serialized_end=45
  _NEWSHEADLINE._serialized_start=47
  _NEWSHEADLINE._serialized_end=79
  _NEWS._serialized_start=81
  _NEWS._serialized_end=195
  _LISTOFNEWS._serialized_start=197
  _LISTOFNEWS._serialized_end=230
  _NEWSGRPC._serialized_start=232
  _NEWSGRPC._serialized_end=282
  _KAFKABROKER._serialized_start=284
  _KAFKABROKER._serialized_end=336
# @@protoc_insertion_point(module_scope)
