# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v4/proto/resources/campaign_label.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v4/proto/resources/campaign_label.proto',
  package='google.ads.googleads.v4.resources',
  syntax='proto3',
  serialized_options=_b('\n%com.google.ads.googleads.v4.resourcesB\022CampaignLabelProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v4/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V4.Resources\312\002!Google\\Ads\\GoogleAds\\V4\\Resources\352\002%Google::Ads::GoogleAds::V4::Resources'),
  serialized_pb=_b('\n<google/ads/googleads_v4/proto/resources/campaign_label.proto\x12!google.ads.googleads.v4.resources\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1cgoogle/api/annotations.proto\"\xe9\x02\n\rCampaignLabel\x12\x45\n\rresource_name\x18\x01 \x01(\tB.\xe0\x41\x05\xfa\x41(\n&googleads.googleapis.com/CampaignLabel\x12Y\n\x08\x63\x61mpaign\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValueB)\xe0\x41\x05\xfa\x41#\n!googleads.googleapis.com/Campaign\x12S\n\x05label\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValueB&\xe0\x41\x05\xfa\x41 \n\x1egoogleads.googleapis.com/Label:a\xea\x41^\n&googleads.googleapis.com/CampaignLabel\x12\x34\x63ustomers/{customer}/campaignLabels/{campaign_label}B\xff\x01\n%com.google.ads.googleads.v4.resourcesB\x12\x43\x61mpaignLabelProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v4/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V4.Resources\xca\x02!Google\\Ads\\GoogleAds\\V4\\Resources\xea\x02%Google::Ads::GoogleAds::V4::Resourcesb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_CAMPAIGNLABEL = _descriptor.Descriptor(
  name='CampaignLabel',
  full_name='google.ads.googleads.v4.resources.CampaignLabel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v4.resources.CampaignLabel.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\005\372A(\n&googleads.googleapis.com/CampaignLabel'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='campaign', full_name='google.ads.googleads.v4.resources.CampaignLabel.campaign', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\005\372A#\n!googleads.googleapis.com/Campaign'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='label', full_name='google.ads.googleads.v4.resources.CampaignLabel.label', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\005\372A \n\036googleads.googleapis.com/Label'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('\352A^\n&googleads.googleapis.com/CampaignLabel\0224customers/{customer}/campaignLabels/{campaign_label}'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=222,
  serialized_end=583,
)

_CAMPAIGNLABEL.fields_by_name['campaign'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_CAMPAIGNLABEL.fields_by_name['label'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
DESCRIPTOR.message_types_by_name['CampaignLabel'] = _CAMPAIGNLABEL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CampaignLabel = _reflection.GeneratedProtocolMessageType('CampaignLabel', (_message.Message,), dict(
  DESCRIPTOR = _CAMPAIGNLABEL,
  __module__ = 'google.ads.googleads_v4.proto.resources.campaign_label_pb2'
  ,
  __doc__ = """Represents a relationship between a campaign and a label.
  
  
  Attributes:
      resource_name:
          Immutable. Name of the resource. Campaign label resource names
          have the form: ``customers/{customer_id}/campaignLabels/{campa
          ign_id}~{label_id}``
      campaign:
          Immutable. The campaign to which the label is attached.
      label:
          Immutable. The label assigned to the campaign.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v4.resources.CampaignLabel)
  ))
_sym_db.RegisterMessage(CampaignLabel)


DESCRIPTOR._options = None
_CAMPAIGNLABEL.fields_by_name['resource_name']._options = None
_CAMPAIGNLABEL.fields_by_name['campaign']._options = None
_CAMPAIGNLABEL.fields_by_name['label']._options = None
_CAMPAIGNLABEL._options = None
# @@protoc_insertion_point(module_scope)
