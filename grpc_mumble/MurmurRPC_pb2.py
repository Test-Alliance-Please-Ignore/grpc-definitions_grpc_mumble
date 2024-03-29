# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grpc_mumble/MurmurRPC.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bgrpc_mumble/MurmurRPC.proto\x12\tMurmurRPC\"\x06\n\x04Void\"K\n\x07Version\x12\x0f\n\x07version\x18\x01 \x01(\r\x12\x0f\n\x07release\x18\x02 \x01(\t\x12\n\n\x02os\x18\x03 \x01(\t\x12\x12\n\nos_version\x18\x04 \x01(\t\"\x16\n\x06Uptime\x12\x0c\n\x04secs\x18\x01 \x01(\x04\"\xe1\x03\n\x06Server\x12\n\n\x02id\x18\x01 \x02(\r\x12\x0f\n\x07running\x18\x02 \x01(\x08\x12!\n\x06uptime\x18\x03 \x01(\x0b\x32\x11.MurmurRPC.Uptime\x1a\xe1\x02\n\x05\x45vent\x12!\n\x06server\x18\x01 \x01(\x0b\x32\x11.MurmurRPC.Server\x12*\n\x04type\x18\x02 \x01(\x0e\x32\x1c.MurmurRPC.Server.Event.Type\x12\x1d\n\x04user\x18\x03 \x01(\x0b\x32\x0f.MurmurRPC.User\x12\'\n\x07message\x18\x04 \x01(\x0b\x32\x16.MurmurRPC.TextMessage\x12#\n\x07\x63hannel\x18\x05 \x01(\x0b\x32\x12.MurmurRPC.Channel\"\x9b\x01\n\x04Type\x12\x11\n\rUserConnected\x10\x00\x12\x14\n\x10UserDisconnected\x10\x01\x12\x14\n\x10UserStateChanged\x10\x02\x12\x13\n\x0fUserTextMessage\x10\x03\x12\x12\n\x0e\x43hannelCreated\x10\x04\x12\x12\n\x0e\x43hannelRemoved\x10\x05\x12\x17\n\x13\x43hannelStateChanged\x10\x06\x1a\x07\n\x05Query\x1a*\n\x04List\x12\"\n\x07servers\x18\x01 \x03(\x0b\x32\x11.MurmurRPC.Server\"}\n\x05\x45vent\x12!\n\x06server\x18\x01 \x01(\x0b\x32\x11.MurmurRPC.Server\x12#\n\x04type\x18\x02 \x01(\x0e\x32\x15.MurmurRPC.Event.Type\",\n\x04Type\x12\x11\n\rServerStopped\x10\x00\x12\x11\n\rServerStarted\x10\x01\"\xf3\x01\n\rContextAction\x12!\n\x06server\x18\x01 \x01(\x0b\x32\x11.MurmurRPC.Server\x12\x0f\n\x07\x63ontext\x18\x02 \x01(\r\x12\x0e\n\x06\x61\x63tion\x18\x03 \x01(\t\x12\x0c\n\x04text\x18\x04 \x01(\t\x12\x1e\n\x05\x61\x63tor\x18\x05 \x01(\x0b\x32\x0f.MurmurRPC.User\x12\x1d\n\x04user\x18\x06 \x01(\x0b\x32\x0f.MurmurRPC.User\x12#\n\x07\x63hannel\x18\x07 \x01(\x0b\x32\x12.MurmurRPC.Channel\",\n\x07\x43ontext\x12\n\n\x06Server\x10\x01\x12\x0b\n\x07\x43hannel\x10\x02\x12\x08\n\x04User\x10\x04\"\x80\x03\n\x0bTextMessage\x12!\n\x06server\x18\x01 \x01(\x0b\x32\x11.MurmurRPC.Server\x12\x1e\n\x05\x61\x63tor\x18\x02 \x01(\x0b\x32\x0f.MurmurRPC.User\x12\x1e\n\x05users\x18\x03 \x03(\x0b\x32\x0f.MurmurRPC.User\x12$\n\x08\x63hannels\x18\x04 \x03(\x0b\x32\x12.MurmurRPC.Channel\x12!\n\x05trees\x18\x05 \x03(\x0b\x32\x12.MurmurRPC.Channel\x12\x0c\n\x04text\x18\x06 \x01(\t\x1a\xb6\x01\n\x06\x46ilter\x12!\n\x06server\x18\x01 \x01(\x0b\x32\x11.MurmurRPC.Server\x12\x34\n\x06\x61\x63tion\x18\x02 \x01(\x0e\x32$.MurmurRPC.TextMessage.Filter.Action\x12\'\n\x07message\x18\x03 \x01(\x0b\x32\x16.MurmurRPC.TextMessage\"*\n\x06\x41\x63tion\x12\n\n\x06\x41\x63\x63\x65pt\x10\x00\x12\n\n\x06Reject\x10\x01\x12\x08\n\x04\x44rop\x10\x02\"\x84\x02\n\x03Log\x12!\n\x06server\x18\x01 \x01(\x0b\x32\x11.MurmurRPC.Server\x12\x11\n\ttimestamp\x18\x02 \x01(\x03\x12\x0c\n\x04text\x18\x03 \x01(\t\x1a\x44\n\x05Query\x12!\n\x06server\x18\x01 \x01(\x0b\x32\x11.MurmurRPC.Server\x12\x0b\n\x03min\x18\x02 \x01(\r\x12\x0b\n\x03max\x18\x03 \x01(\r\x1as\n\x04List\x12!\n\x06server\x18\x01 \x01(\x0b\x32\x11.MurmurRPC.Server\x12\r\n\x05total\x18\x02 \x01(\r\x12\x0b\n\x03min\x18\x03 \x01(\r\x12\x0b\n\x03max\x18\x04 \x01(\r\x12\x1f\n\x07\x65ntries\x18\x05 \x03(\x0b\x32\x0e.MurmurRPC.Log\"\xd1\x01\n\x06\x43onfig\x12!\n\x06server\x18\x01 \x01(\x0b\x32\x11.MurmurRPC.Server\x12-\n\x06\x66ields\x18\x02 \x03(\x0b\x32\x1d.MurmurRPC.Config.FieldsEntry\x1a-\n\x0b\x46ieldsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x46\n\x05\x46ield\x12!\n\x06server\x18\x01 \x01(\x0b\x32\x11.MurmurRPC.Server\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t\"\xc4\x02\n\x07\x43hannel\x12!\n\x06server\x18\x01 \x01(\x0b\x32\x11.MurmurRPC.Server\x12\n\n\x02id\x18\x02 \x01(\r\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\"\n\x06parent\x18\x04 \x01(\x0b\x32\x12.MurmurRPC.Channel\x12!\n\x05links\x18\x05 \x03(\x0b\x32\x12.MurmurRPC.Channel\x12\x13\n\x0b\x64\x65scription\x18\x06 \x01(\t\x12\x11\n\ttemporary\x18\x07 \x01(\x08\x12\x10\n\x08position\x18\x08 \x01(\x05\x1a*\n\x05Query\x12!\n\x06server\x18\x01 \x01(\x0b\x32\x11.MurmurRPC.Server\x1aO\n\x04List\x12!\n\x06server\x18\x01 \x01(\x0b\x32\x11.MurmurRPC.Server\x12$\n\x08\x63hannels\x18\x02 \x03(\x0b\x32\x12.MurmurRPC.Channel\"\xf5\x05\n\x04User\x12!\n\x06server\x18\x01 \x01(\x0b\x32\x11.MurmurRPC.Server\x12\x0f\n\x07session\x18\x02 \x01(\r\x12\n\n\x02id\x18\x03 \x01(\r\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x0c\n\x04mute\x18\x05 \x01(\x08\x12\x0c\n\x04\x64\x65\x61\x66\x18\x06 \x01(\x08\x12\x10\n\x08suppress\x18\x07 \x01(\x08\x12\x18\n\x10priority_speaker\x18\x08 \x01(\x08\x12\x11\n\tself_mute\x18\t \x01(\x08\x12\x11\n\tself_deaf\x18\n \x01(\x08\x12\x11\n\trecording\x18\x0b \x01(\x08\x12#\n\x07\x63hannel\x18\x0c \x01(\x0b\x32\x12.MurmurRPC.Channel\x12\x13\n\x0bonline_secs\x18\r \x01(\r\x12\x11\n\tidle_secs\x18\x0e \x01(\r\x12\x15\n\rbytes_per_sec\x18\x0f \x01(\r\x12#\n\x07version\x18\x10 \x01(\x0b\x32\x12.MurmurRPC.Version\x12\x16\n\x0eplugin_context\x18\x11 \x01(\x0c\x12\x17\n\x0fplugin_identity\x18\x12 \x01(\t\x12\x0f\n\x07\x63omment\x18\x13 \x01(\t\x12\x0f\n\x07texture\x18\x14 \x01(\x0c\x12\x0f\n\x07\x61\x64\x64ress\x18\x15 \x01(\x0c\x12\x10\n\x08tcp_only\x18\x16 \x01(\x08\x12\x16\n\x0eudp_ping_msecs\x18\x17 \x01(\x02\x12\x16\n\x0etcp_ping_msecs\x18\x18 \x01(\x02\x1a*\n\x05Query\x12!\n\x06server\x18\x01 \x01(\x0b\x32\x11.MurmurRPC.Server\x1aI\n\x04List\x12!\n\x06server\x18\x01 \x01(\x0b\x32\x11.MurmurRPC.Server\x12\x1e\n\x05users\x18\x02 \x03(\x0b\x32\x0f.MurmurRPC.User\x1ax\n\x04Kick\x12!\n\x06server\x18\x01 \x01(\x0b\x32\x11.MurmurRPC.Server\x12\x1d\n\x04user\x18\x02 \x01(\x0b\x32\x0f.MurmurRPC.User\x12\x1e\n\x05\x61\x63tor\x18\x03 \x01(\x0b\x32\x0f.MurmurRPC.User\x12\x0e\n\x06reason\x18\x04 \x01(\t\"\xbd\x01\n\x04Tree\x12!\n\x06server\x18\x01 \x01(\x0b\x32\x11.MurmurRPC.Server\x12#\n\x07\x63hannel\x18\x02 \x01(\x0b\x32\x12.MurmurRPC.Channel\x12!\n\x08\x63hildren\x18\x03 \x03(\x0b\x32\x0f.MurmurRPC.Tree\x12\x1e\n\x05users\x18\x04 \x03(\x0b\x32\x0f.MurmurRPC.User\x1a*\n\x05Query\x12!\n\x06server\x18\x01 \x01(\x0b\x32\x11.MurmurRPC.Server\"\x8e\x02\n\x03\x42\x61n\x12!\n\x06server\x18\x01 \x01(\x0b\x32\x11.MurmurRPC.Server\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0c\x12\x0c\n\x04\x62its\x18\x03 \x01(\r\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x0c\n\x04hash\x18\x05 \x01(\t\x12\x0e\n\x06reason\x18\x06 \x01(\t\x12\r\n\x05start\x18\x07 \x01(\x03\x12\x15\n\rduration_secs\x18\x08 \x01(\x03\x1a*\n\x05Query\x12!\n\x06server\x18\x01 \x01(\x0b\x32\x11.MurmurRPC.Server\x1aG\n\x04List\x12!\n\x06server\x18\x01 \x01(\x0b\x32\x11.MurmurRPC.Server\x12\x1c\n\x04\x62\x61ns\x18\x02 \x03(\x0b\x32\x0e.MurmurRPC.Ban\"\x96\x08\n\x03\x41\x43L\x12\x12\n\napply_here\x18\x03 \x01(\x08\x12\x12\n\napply_subs\x18\x04 \x01(\x08\x12\x11\n\tinherited\x18\x05 \x01(\x08\x12%\n\x04user\x18\x06 \x01(\x0b\x32\x17.MurmurRPC.DatabaseUser\x12#\n\x05group\x18\x07 \x01(\x0b\x32\x14.MurmurRPC.ACL.Group\x12\r\n\x05\x61llow\x18\x08 \x01(\r\x12\x0c\n\x04\x64\x65ny\x18\t \x01(\r\x1a\xd1\x01\n\x05Group\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tinherited\x18\x02 \x01(\x08\x12\x0f\n\x07inherit\x18\x03 \x01(\x08\x12\x13\n\x0binheritable\x18\x04 \x01(\x08\x12*\n\tusers_add\x18\x05 \x03(\x0b\x32\x17.MurmurRPC.DatabaseUser\x12-\n\x0cusers_remove\x18\x06 \x03(\x0b\x32\x17.MurmurRPC.DatabaseUser\x12&\n\x05users\x18\x07 \x03(\x0b\x32\x17.MurmurRPC.DatabaseUser\x1an\n\x05Query\x12!\n\x06server\x18\x01 \x01(\x0b\x32\x11.MurmurRPC.Server\x12\x1d\n\x04user\x18\x02 \x01(\x0b\x32\x0f.MurmurRPC.User\x12#\n\x07\x63hannel\x18\x03 \x01(\x0b\x32\x12.MurmurRPC.Channel\x1a\xa3\x01\n\x04List\x12!\n\x06server\x18\x01 \x01(\x0b\x32\x11.MurmurRPC.Server\x12#\n\x07\x63hannel\x18\x02 \x01(\x0b\x32\x12.MurmurRPC.Channel\x12\x1c\n\x04\x61\x63ls\x18\x03 \x03(\x0b\x32\x0e.MurmurRPC.ACL\x12$\n\x06groups\x18\x04 \x03(\x0b\x32\x14.MurmurRPC.ACL.Group\x12\x0f\n\x07inherit\x18\x05 \x01(\x08\x1a\x85\x01\n\x0eTemporaryGroup\x12!\n\x06server\x18\x01 \x01(\x0b\x32\x11.MurmurRPC.Server\x12#\n\x07\x63hannel\x18\x02 \x01(\x0b\x32\x12.MurmurRPC.Channel\x12\x1d\n\x04user\x18\x03 \x01(\x0b\x32\x0f.MurmurRPC.User\x12\x0c\n\x04name\x18\x04 \x01(\t\"\xf8\x01\n\nPermission\x12\x08\n\x04None\x10\x00\x12\t\n\x05Write\x10\x01\x12\x0c\n\x08Traverse\x10\x02\x12\t\n\x05\x45nter\x10\x04\x12\t\n\x05Speak\x10\x08\x12\x0c\n\x07Whisper\x10\x80\x02\x12\x0e\n\nMuteDeafen\x10\x10\x12\x08\n\x04Move\x10 \x12\x0f\n\x0bMakeChannel\x10@\x12\x19\n\x14MakeTemporaryChannel\x10\x80\x08\x12\x10\n\x0bLinkChannel\x10\x80\x01\x12\x10\n\x0bTextMessage\x10\x80\x04\x12\n\n\x04Kick\x10\x80\x80\x04\x12\t\n\x03\x42\x61n\x10\x80\x80\x08\x12\x0e\n\x08Register\x10\x80\x80\x10\x12\x12\n\x0cRegisterSelf\x10\x80\x80 \"\xf0\r\n\rAuthenticator\x1a\xc1\x05\n\x07Request\x12\x43\n\x0c\x61uthenticate\x18\x01 \x01(\x0b\x32-.MurmurRPC.Authenticator.Request.Authenticate\x12\x33\n\x04\x66ind\x18\x02 \x01(\x0b\x32%.MurmurRPC.Authenticator.Request.Find\x12\x35\n\x05query\x18\x03 \x01(\x0b\x32&.MurmurRPC.Authenticator.Request.Query\x12;\n\x08register\x18\x04 \x01(\x0b\x32).MurmurRPC.Authenticator.Request.Register\x12?\n\nderegister\x18\x05 \x01(\x0b\x32+.MurmurRPC.Authenticator.Request.Deregister\x12\x37\n\x06update\x18\x06 \x01(\x0b\x32\'.MurmurRPC.Authenticator.Request.Update\x1az\n\x0c\x41uthenticate\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12\x14\n\x0c\x63\x65rtificates\x18\x03 \x03(\x0c\x12\x18\n\x10\x63\x65rtificate_hash\x18\x04 \x01(\t\x12\x1a\n\x12strong_certificate\x18\x05 \x01(\x08\x1a \n\x04\x46ind\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x1a\x17\n\x05Query\x12\x0e\n\x06\x66ilter\x18\x01 \x01(\t\x1a\x31\n\x08Register\x12%\n\x04user\x18\x01 \x01(\x0b\x32\x17.MurmurRPC.DatabaseUser\x1a\x33\n\nDeregister\x12%\n\x04user\x18\x01 \x01(\x0b\x32\x17.MurmurRPC.DatabaseUser\x1a/\n\x06Update\x12%\n\x04user\x18\x01 \x01(\x0b\x32\x17.MurmurRPC.DatabaseUser\x1a\x9a\x08\n\x08Response\x12@\n\ninitialize\x18\x01 \x01(\x0b\x32,.MurmurRPC.Authenticator.Response.Initialize\x12\x44\n\x0c\x61uthenticate\x18\x02 \x01(\x0b\x32..MurmurRPC.Authenticator.Response.Authenticate\x12\x34\n\x04\x66ind\x18\x03 \x01(\x0b\x32&.MurmurRPC.Authenticator.Response.Find\x12\x36\n\x05query\x18\x04 \x01(\x0b\x32\'.MurmurRPC.Authenticator.Response.Query\x12<\n\x08register\x18\x05 \x01(\x0b\x32*.MurmurRPC.Authenticator.Response.Register\x12@\n\nderegister\x18\x06 \x01(\x0b\x32,.MurmurRPC.Authenticator.Response.Deregister\x12\x38\n\x06update\x18\x07 \x01(\x0b\x32(.MurmurRPC.Authenticator.Response.Update\x1a/\n\nInitialize\x12!\n\x06server\x18\x01 \x01(\x0b\x32\x11.MurmurRPC.Server\x1a\x88\x01\n\x0c\x41uthenticate\x12\x38\n\x06status\x18\x01 \x01(\x0e\x32(.MurmurRPC.Authenticator.Response.Status\x12\n\n\x02id\x18\x02 \x01(\r\x12\x0c\n\x04name\x18\x03 \x01(\t\x12$\n\x06groups\x18\x04 \x03(\x0b\x32\x14.MurmurRPC.ACL.Group\x1a-\n\x04\x46ind\x12%\n\x04user\x18\x01 \x01(\x0b\x32\x17.MurmurRPC.DatabaseUser\x1a/\n\x05Query\x12&\n\x05users\x18\x01 \x03(\x0b\x32\x17.MurmurRPC.DatabaseUser\x1ak\n\x08Register\x12\x38\n\x06status\x18\x01 \x01(\x0e\x32(.MurmurRPC.Authenticator.Response.Status\x12%\n\x04user\x18\x02 \x01(\x0b\x32\x17.MurmurRPC.DatabaseUser\x1a\x46\n\nDeregister\x12\x38\n\x06status\x18\x01 \x01(\x0e\x32(.MurmurRPC.Authenticator.Response.Status\x1a\x42\n\x06Update\x12\x38\n\x06status\x18\x01 \x01(\x0e\x32(.MurmurRPC.Authenticator.Response.Status\"I\n\x06Status\x12\x0f\n\x0b\x46\x61llthrough\x10\x00\x12\x0b\n\x07Success\x10\x01\x12\x0b\n\x07\x46\x61ilure\x10\x02\x12\x14\n\x10TemporaryFailure\x10\x03\"\x8d\x03\n\x0c\x44\x61tabaseUser\x12!\n\x06server\x18\x01 \x01(\x0b\x32\x11.MurmurRPC.Server\x12\n\n\x02id\x18\x02 \x01(\r\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\r\n\x05\x65mail\x18\x04 \x01(\t\x12\x0f\n\x07\x63omment\x18\x05 \x01(\t\x12\x0c\n\x04hash\x18\x06 \x01(\t\x12\x10\n\x08password\x18\x07 \x01(\t\x12\x13\n\x0blast_active\x18\x08 \x01(\t\x12\x0f\n\x07texture\x18\t \x01(\x0c\x1a:\n\x05Query\x12!\n\x06server\x18\x01 \x01(\x0b\x32\x11.MurmurRPC.Server\x12\x0e\n\x06\x66ilter\x18\x02 \x01(\t\x1aQ\n\x04List\x12!\n\x06server\x18\x01 \x01(\x0b\x32\x11.MurmurRPC.Server\x12&\n\x05users\x18\x02 \x03(\x0b\x32\x17.MurmurRPC.DatabaseUser\x1aK\n\x06Verify\x12!\n\x06server\x18\x01 \x01(\x0b\x32\x11.MurmurRPC.Server\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\t\"\xa4\x01\n\x14RedirectWhisperGroup\x12!\n\x06server\x18\x01 \x01(\x0b\x32\x11.MurmurRPC.Server\x12\x1d\n\x04user\x18\x02 \x01(\x0b\x32\x0f.MurmurRPC.User\x12$\n\x06source\x18\x03 \x01(\x0b\x32\x14.MurmurRPC.ACL.Group\x12$\n\x06target\x18\x04 \x01(\x0b\x32\x14.MurmurRPC.ACL.Group\"\xbd\x02\n\x05Group\x12!\n\x06server\x18\x01 \x01(\x0b\x32\x11.MurmurRPC.Server\x12#\n\x07\x63hannel\x18\x02 \x01(\x0b\x32\x12.MurmurRPC.Channel\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0f\n\x07inherit\x18\x04 \x01(\x08\x12\x13\n\x0binheritable\x18\x05 \x01(\x08\x12\x14\n\x0cuser_ids_add\x18\x06 \x03(\r\x12\x17\n\x0fuser_ids_remove\x18\x07 \x03(\r\x12\x17\n\x0fuser_ids_delete\x18\x08 \x03(\r\x1ap\n\x04List\x12!\n\x06server\x18\x01 \x01(\x0b\x32\x11.MurmurRPC.Server\x12#\n\x07\x63hannel\x18\x02 \x01(\x0b\x32\x12.MurmurRPC.Channel\x12 \n\x06groups\x18\x03 \x03(\x0b\x32\x10.MurmurRPC.Group\"\xe9\x01\n\x10TESTDatabaseUser\x12%\n\x04user\x18\x01 \x01(\x0b\x32\x17.MurmurRPC.DatabaseUser\x12\r\n\x05\x61lias\x18\x03 \x01(\t\x12\x10\n\x08password\x18\x04 \x01(\t\x12\x15\n\rpassword_salt\x18\x05 \x01(\t\x12\x1f\n\x17password_kdf_iterations\x18\x06 \x01(\r\x1aU\n\x04List\x12!\n\x06server\x18\x01 \x01(\x0b\x32\x11.MurmurRPC.Server\x12*\n\x05users\x18\x02 \x03(\x0b\x32\x1b.MurmurRPC.TESTDatabaseUser2\x80\x1c\n\x02V1\x12/\n\tGetUptime\x12\x0f.MurmurRPC.Void\x1a\x11.MurmurRPC.Uptime\x12\x31\n\nGetVersion\x12\x0f.MurmurRPC.Void\x1a\x12.MurmurRPC.Version\x12-\n\x06\x45vents\x12\x0f.MurmurRPC.Void\x1a\x10.MurmurRPC.Event0\x01\x12\x32\n\x0cServerCreate\x12\x0f.MurmurRPC.Void\x1a\x11.MurmurRPC.Server\x12>\n\x0bServerQuery\x12\x17.MurmurRPC.Server.Query\x1a\x16.MurmurRPC.Server.List\x12\x31\n\tServerGet\x12\x11.MurmurRPC.Server\x1a\x11.MurmurRPC.Server\x12\x31\n\x0bServerStart\x12\x11.MurmurRPC.Server\x1a\x0f.MurmurRPC.Void\x12\x30\n\nServerStop\x12\x11.MurmurRPC.Server\x1a\x0f.MurmurRPC.Void\x12\x32\n\x0cServerRemove\x12\x11.MurmurRPC.Server\x1a\x0f.MurmurRPC.Void\x12<\n\x0cServerEvents\x12\x11.MurmurRPC.Server\x1a\x17.MurmurRPC.Server.Event0\x01\x12\x44\n\x11ServerGetAllUsers\x12\x11.MurmurRPC.Server\x1a\x1c.MurmurRPC.DatabaseUser.List\x12=\n\x10\x43ontextActionAdd\x12\x18.MurmurRPC.ContextAction\x1a\x0f.MurmurRPC.Void\x12@\n\x13\x43ontextActionRemove\x12\x18.MurmurRPC.ContextAction\x1a\x0f.MurmurRPC.Void\x12K\n\x13\x43ontextActionEvents\x12\x18.MurmurRPC.ContextAction\x1a\x18.MurmurRPC.ContextAction0\x01\x12:\n\x0fTextMessageSend\x12\x16.MurmurRPC.TextMessage\x1a\x0f.MurmurRPC.Void\x12U\n\x11TextMessageFilter\x12\x1d.MurmurRPC.TextMessage.Filter\x1a\x1d.MurmurRPC.TextMessage.Filter(\x01\x30\x01\x12\x35\n\x08LogQuery\x12\x14.MurmurRPC.Log.Query\x1a\x13.MurmurRPC.Log.List\x12\x31\n\tConfigGet\x12\x11.MurmurRPC.Server\x1a\x11.MurmurRPC.Config\x12\x42\n\x0e\x43onfigGetField\x12\x17.MurmurRPC.Config.Field\x1a\x17.MurmurRPC.Config.Field\x12:\n\x0e\x43onfigSetField\x12\x17.MurmurRPC.Config.Field\x1a\x0f.MurmurRPC.Void\x12\x36\n\x10\x43onfigGetDefault\x12\x0f.MurmurRPC.Void\x1a\x11.MurmurRPC.Config\x12\x41\n\x0c\x43hannelQuery\x12\x18.MurmurRPC.Channel.Query\x1a\x17.MurmurRPC.Channel.List\x12\x34\n\nChannelGet\x12\x12.MurmurRPC.Channel\x1a\x12.MurmurRPC.Channel\x12\x34\n\nChannelAdd\x12\x12.MurmurRPC.Channel\x1a\x12.MurmurRPC.Channel\x12\x34\n\rChannelRemove\x12\x12.MurmurRPC.Channel\x1a\x0f.MurmurRPC.Void\x12\x37\n\rChannelUpdate\x12\x12.MurmurRPC.Channel\x1a\x12.MurmurRPC.Channel\x12=\n\x10\x43hannelGetGroups\x12\x12.MurmurRPC.Channel\x1a\x15.MurmurRPC.Group.List\x12\x38\n\tUserQuery\x12\x15.MurmurRPC.User.Query\x1a\x14.MurmurRPC.User.List\x12+\n\x07UserGet\x12\x0f.MurmurRPC.User\x1a\x0f.MurmurRPC.User\x12.\n\nUserUpdate\x12\x0f.MurmurRPC.User\x1a\x0f.MurmurRPC.User\x12\x31\n\x08UserKick\x12\x14.MurmurRPC.User.Kick\x1a\x0f.MurmurRPC.Void\x12\x33\n\tTreeQuery\x12\x15.MurmurRPC.Tree.Query\x1a\x0f.MurmurRPC.Tree\x12\x34\n\x07\x42\x61nsGet\x12\x14.MurmurRPC.Ban.Query\x1a\x13.MurmurRPC.Ban.List\x12/\n\x07\x42\x61nsSet\x12\x13.MurmurRPC.Ban.List\x1a\x0f.MurmurRPC.Void\x12\x31\n\x06\x41\x43LGet\x12\x12.MurmurRPC.Channel\x1a\x13.MurmurRPC.ACL.List\x12.\n\x06\x41\x43LSet\x12\x13.MurmurRPC.ACL.List\x1a\x0f.MurmurRPC.Void\x12\x42\n\x1a\x41\x43LGetEffectivePermissions\x12\x14.MurmurRPC.ACL.Query\x1a\x0e.MurmurRPC.ACL\x12\x46\n\x14\x41\x43LAddTemporaryGroup\x12\x1d.MurmurRPC.ACL.TemporaryGroup\x1a\x0f.MurmurRPC.Void\x12I\n\x17\x41\x43LRemoveTemporaryGroup\x12\x1d.MurmurRPC.ACL.TemporaryGroup\x1a\x0f.MurmurRPC.Void\x12^\n\x13\x41uthenticatorStream\x12!.MurmurRPC.Authenticator.Response\x1a .MurmurRPC.Authenticator.Request(\x01\x30\x01\x12P\n\x11\x44\x61tabaseUserQuery\x12\x1d.MurmurRPC.DatabaseUser.Query\x1a\x1c.MurmurRPC.DatabaseUser.List\x12\x43\n\x0f\x44\x61tabaseUserGet\x12\x17.MurmurRPC.DatabaseUser\x1a\x17.MurmurRPC.DatabaseUser\x12>\n\x12\x44\x61tabaseUserUpdate\x12\x17.MurmurRPC.DatabaseUser\x1a\x0f.MurmurRPC.Void\x12H\n\x14\x44\x61tabaseUserRegister\x12\x17.MurmurRPC.DatabaseUser\x1a\x17.MurmurRPC.DatabaseUser\x12\x42\n\x16\x44\x61tabaseUserDeregister\x12\x17.MurmurRPC.DatabaseUser\x1a\x0f.MurmurRPC.Void\x12M\n\x12\x44\x61tabaseUserVerify\x12\x1e.MurmurRPC.DatabaseUser.Verify\x1a\x17.MurmurRPC.DatabaseUser\x12\x44\n\x12\x44\x61tabaseUserGroups\x12\x17.MurmurRPC.DatabaseUser\x1a\x15.MurmurRPC.Group.List\x12K\n\x17RedirectWhisperGroupAdd\x12\x1f.MurmurRPC.RedirectWhisperGroup\x1a\x0f.MurmurRPC.Void\x12N\n\x1aRedirectWhisperGroupRemove\x12\x1f.MurmurRPC.RedirectWhisperGroup\x1a\x0f.MurmurRPC.Void\x12\x30\n\x0bGroupUpdate\x12\x10.MurmurRPC.Group\x1a\x0f.MurmurRPC.Void\x12\x30\n\x0bGroupDelete\x12\x10.MurmurRPC.Group\x1a\x0f.MurmurRPC.Void\x12.\n\x08GroupGet\x12\x10.MurmurRPC.Group\x1a\x10.MurmurRPC.Group\x12\x32\n\rGroupAddUsers\x12\x10.MurmurRPC.Group\x1a\x0f.MurmurRPC.Void\x12\x35\n\x10GroupDeleteUsers\x12\x10.MurmurRPC.Group\x1a\x0f.MurmurRPC.Void\x12\x38\n\x11GroupAddUsersMany\x12\x10.MurmurRPC.Group\x1a\x0f.MurmurRPC.Void(\x01\x12;\n\x14GroupDeleteUsersMany\x12\x10.MurmurRPC.Group\x1a\x0f.MurmurRPC.Void(\x01\x12[\n\x1cTESTDatabaseUserRegisterMany\x12\x1b.MurmurRPC.TESTDatabaseUser\x1a\x1c.MurmurRPC.DatabaseUser.List(\x01\x12Y\n\x1aTESTDatabaseUserUpdateMany\x12\x1b.MurmurRPC.TESTDatabaseUser\x1a\x1c.MurmurRPC.DatabaseUser.List(\x01')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'grpc_mumble.MurmurRPC_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CONFIG_FIELDSENTRY._options = None
  _CONFIG_FIELDSENTRY._serialized_options = b'8\001'
  _VOID._serialized_start=42
  _VOID._serialized_end=48
  _VERSION._serialized_start=50
  _VERSION._serialized_end=125
  _UPTIME._serialized_start=127
  _UPTIME._serialized_end=149
  _SERVER._serialized_start=152
  _SERVER._serialized_end=633
  _SERVER_EVENT._serialized_start=227
  _SERVER_EVENT._serialized_end=580
  _SERVER_EVENT_TYPE._serialized_start=425
  _SERVER_EVENT_TYPE._serialized_end=580
  _SERVER_QUERY._serialized_start=582
  _SERVER_QUERY._serialized_end=589
  _SERVER_LIST._serialized_start=591
  _SERVER_LIST._serialized_end=633
  _EVENT._serialized_start=635
  _EVENT._serialized_end=760
  _EVENT_TYPE._serialized_start=716
  _EVENT_TYPE._serialized_end=760
  _CONTEXTACTION._serialized_start=763
  _CONTEXTACTION._serialized_end=1006
  _CONTEXTACTION_CONTEXT._serialized_start=962
  _CONTEXTACTION_CONTEXT._serialized_end=1006
  _TEXTMESSAGE._serialized_start=1009
  _TEXTMESSAGE._serialized_end=1393
  _TEXTMESSAGE_FILTER._serialized_start=1211
  _TEXTMESSAGE_FILTER._serialized_end=1393
  _TEXTMESSAGE_FILTER_ACTION._serialized_start=1351
  _TEXTMESSAGE_FILTER_ACTION._serialized_end=1393
  _LOG._serialized_start=1396
  _LOG._serialized_end=1656
  _LOG_QUERY._serialized_start=1471
  _LOG_QUERY._serialized_end=1539
  _LOG_LIST._serialized_start=1541
  _LOG_LIST._serialized_end=1656
  _CONFIG._serialized_start=1659
  _CONFIG._serialized_end=1868
  _CONFIG_FIELDSENTRY._serialized_start=1751
  _CONFIG_FIELDSENTRY._serialized_end=1796
  _CONFIG_FIELD._serialized_start=1798
  _CONFIG_FIELD._serialized_end=1868
  _CHANNEL._serialized_start=1871
  _CHANNEL._serialized_end=2195
  _CHANNEL_QUERY._serialized_start=1471
  _CHANNEL_QUERY._serialized_end=1513
  _CHANNEL_LIST._serialized_start=2116
  _CHANNEL_LIST._serialized_end=2195
  _USER._serialized_start=2198
  _USER._serialized_end=2955
  _USER_QUERY._serialized_start=1471
  _USER_QUERY._serialized_end=1513
  _USER_LIST._serialized_start=2760
  _USER_LIST._serialized_end=2833
  _USER_KICK._serialized_start=2835
  _USER_KICK._serialized_end=2955
  _TREE._serialized_start=2958
  _TREE._serialized_end=3147
  _TREE_QUERY._serialized_start=1471
  _TREE_QUERY._serialized_end=1513
  _BAN._serialized_start=3150
  _BAN._serialized_end=3420
  _BAN_QUERY._serialized_start=1471
  _BAN_QUERY._serialized_end=1513
  _BAN_LIST._serialized_start=3349
  _BAN_LIST._serialized_end=3420
  _ACL._serialized_start=3423
  _ACL._serialized_end=4469
  _ACL_GROUP._serialized_start=3595
  _ACL_GROUP._serialized_end=3804
  _ACL_QUERY._serialized_start=3806
  _ACL_QUERY._serialized_end=3916
  _ACL_LIST._serialized_start=3919
  _ACL_LIST._serialized_end=4082
  _ACL_TEMPORARYGROUP._serialized_start=4085
  _ACL_TEMPORARYGROUP._serialized_end=4218
  _ACL_PERMISSION._serialized_start=4221
  _ACL_PERMISSION._serialized_end=4469
  _AUTHENTICATOR._serialized_start=4472
  _AUTHENTICATOR._serialized_end=6248
  _AUTHENTICATOR_REQUEST._serialized_start=4490
  _AUTHENTICATOR_REQUEST._serialized_end=5195
  _AUTHENTICATOR_REQUEST_AUTHENTICATE._serialized_start=4861
  _AUTHENTICATOR_REQUEST_AUTHENTICATE._serialized_end=4983
  _AUTHENTICATOR_REQUEST_FIND._serialized_start=4985
  _AUTHENTICATOR_REQUEST_FIND._serialized_end=5017
  _AUTHENTICATOR_REQUEST_QUERY._serialized_start=5019
  _AUTHENTICATOR_REQUEST_QUERY._serialized_end=5042
  _AUTHENTICATOR_REQUEST_REGISTER._serialized_start=5044
  _AUTHENTICATOR_REQUEST_REGISTER._serialized_end=5093
  _AUTHENTICATOR_REQUEST_DEREGISTER._serialized_start=5095
  _AUTHENTICATOR_REQUEST_DEREGISTER._serialized_end=5146
  _AUTHENTICATOR_REQUEST_UPDATE._serialized_start=5148
  _AUTHENTICATOR_REQUEST_UPDATE._serialized_end=5195
  _AUTHENTICATOR_RESPONSE._serialized_start=5198
  _AUTHENTICATOR_RESPONSE._serialized_end=6248
  _AUTHENTICATOR_RESPONSE_INITIALIZE._serialized_start=5642
  _AUTHENTICATOR_RESPONSE_INITIALIZE._serialized_end=5689
  _AUTHENTICATOR_RESPONSE_AUTHENTICATE._serialized_start=5692
  _AUTHENTICATOR_RESPONSE_AUTHENTICATE._serialized_end=5828
  _AUTHENTICATOR_RESPONSE_FIND._serialized_start=5830
  _AUTHENTICATOR_RESPONSE_FIND._serialized_end=5875
  _AUTHENTICATOR_RESPONSE_QUERY._serialized_start=5877
  _AUTHENTICATOR_RESPONSE_QUERY._serialized_end=5924
  _AUTHENTICATOR_RESPONSE_REGISTER._serialized_start=5926
  _AUTHENTICATOR_RESPONSE_REGISTER._serialized_end=6033
  _AUTHENTICATOR_RESPONSE_DEREGISTER._serialized_start=6035
  _AUTHENTICATOR_RESPONSE_DEREGISTER._serialized_end=6105
  _AUTHENTICATOR_RESPONSE_UPDATE._serialized_start=6107
  _AUTHENTICATOR_RESPONSE_UPDATE._serialized_end=6173
  _AUTHENTICATOR_RESPONSE_STATUS._serialized_start=6175
  _AUTHENTICATOR_RESPONSE_STATUS._serialized_end=6248
  _DATABASEUSER._serialized_start=6251
  _DATABASEUSER._serialized_end=6648
  _DATABASEUSER_QUERY._serialized_start=6430
  _DATABASEUSER_QUERY._serialized_end=6488
  _DATABASEUSER_LIST._serialized_start=6490
  _DATABASEUSER_LIST._serialized_end=6571
  _DATABASEUSER_VERIFY._serialized_start=6573
  _DATABASEUSER_VERIFY._serialized_end=6648
  _REDIRECTWHISPERGROUP._serialized_start=6651
  _REDIRECTWHISPERGROUP._serialized_end=6815
  _GROUP._serialized_start=6818
  _GROUP._serialized_end=7135
  _GROUP_LIST._serialized_start=7023
  _GROUP_LIST._serialized_end=7135
  _TESTDATABASEUSER._serialized_start=7138
  _TESTDATABASEUSER._serialized_end=7371
  _TESTDATABASEUSER_LIST._serialized_start=7286
  _TESTDATABASEUSER_LIST._serialized_end=7371
  _V1._serialized_start=7374
  _V1._serialized_end=10958
# @@protoc_insertion_point(module_scope)
