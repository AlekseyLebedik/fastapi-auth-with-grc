# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: user.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nuser.proto\x12\x04user\"\x95\x02\n\x0fUserPrivateMeta\x12\x18\n\x0b\x64ocument_id\x18\x01 \x01(\tH\x00\x88\x01\x01\x12!\n\x14\x64ocument_photo_links\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x18\n\x0bnationality\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x14\n\x07mac_ids\x18\x04 \x01(\tH\x03\x88\x01\x01\x12\x18\n\x0bverify_date\x18\x05 \x01(\tH\x04\x88\x01\x01\x12\x14\n\x07\x62r_date\x18\x06 \x01(\tH\x05\x88\x01\x01\x42\x0e\n\x0c_document_idB\x17\n\x15_document_photo_linksB\x0e\n\x0c_nationalityB\n\n\x08_mac_idsB\x0e\n\x0c_verify_dateB\n\n\x08_br_dateJ\x04\x08\n\x10\x10\"\xca\x02\n\x04User\x12\r\n\x05\x66name\x18\x01 \x01(\t\x12\r\n\x05lname\x18\x02 \x01(\t\x12\x1a\n\x05roles\x18\x03 \x03(\x0e\x32\x0b.user.ROLES\x12\x12\n\x05\x65mail\x18\x04 \x01(\tH\x01\x88\x01\x01\x12\x12\n\x05phone\x18\x05 \x01(\tH\x02\x88\x01\x01\x12\x18\n\x0bphone_token\x18\x06 \x01(\tH\x03\x88\x01\x01\x12\x12\n\x08password\x18\x07 \x01(\tH\x00\x12\x19\n\x0fhashed_password\x18\x08 \x01(\tH\x00\x12\x13\n\x06\x61vatar\x18\t \x01(\x0cH\x04\x88\x01\x01\x12/\n\x0bprivateMeta\x18\n \x01(\x0b\x32\x15.user.UserPrivateMetaH\x05\x88\x01\x01\x42\x12\n\x10password_variantB\x08\n\x06_emailB\x08\n\x06_phoneB\x0e\n\x0c_phone_tokenB\t\n\x07_avatarB\x0e\n\x0c_privateMeta\"\x97\x01\n\x17\x41vailableFieldsToUpdate\x12\x12\n\x05\x66name\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x12\n\x05lname\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x13\n\x06\x61vatar\x18\x03 \x01(\x0cH\x02\x88\x01\x01\x12\x14\n\x07\x62r_date\x18\x04 \x01(\tH\x03\x88\x01\x01\x42\x08\n\x06_fnameB\x08\n\x06_lnameB\t\n\x07_avatarB\n\n\x08_br_date\"r\n\rTotalResponse\x12\x0f\n\x07\x64\x65tails\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\x05\x12\x1a\n\x04user\x18\x03 \x01(\x0b\x32\n.user.UserH\x00\x12\x13\n\tcondition\x18\x04 \x01(\x08H\x00\x42\x0f\n\rresponse_data\"-\n\x11\x43reateUserRequest\x12\x18\n\x04user\x18\x01 \x01(\x0b\x32\n.user.User\"H\n\x19OrdinaryUpdateUserRequest\x12+\n\x04user\x18\x01 \x01(\x0b\x32\x1d.user.AvailableFieldsToUpdate\"`\n\x18\x43hangePhoneNumberRequest\x12\x14\n\x0cphone_number\x18\x01 \x01(\t\x12\x13\n\x0bverify_code\x18\x02 \x01(\x05\x12\x19\n\x11verify_with_email\x18\x03 \x01(\x08\"$\n\x11\x44\x65leteUserRequest\x12\x0f\n\x07user_id\x18\x03 \x01(\x05\"4\n\x19VerifyUserWithDocsRequest\x12\x11\n\tdocuments\x18\x01 \x03(\x0cJ\x04\x08\x05\x10\x0b\"2\n\x15\x43hangeUserRoleRequest\x12\x19\n\x04role\x18\x01 \x01(\x0e\x32\x0b.user.ROLES\"v\n UserDataValidationByAdminRequest\x12\x1d\n\x04user\x18\x01 \x01(\x0b\x32\n.user.UserH\x00\x88\x01\x01\x12*\n\nconclusion\x18\x03 \x01(\x0e\x32\x16.user.ADMIN_CONCLUSIONB\x07\n\x05_user\",\n\x16LightVerifyUserRequest\x12\x12\n\nverify_key\x18\x01 \x01(\x05*Q\n\x10\x41\x44MIN_CONCLUSION\x12\x13\n\x0fUNRELIABLE_DATA\x10\x00\x12\n\n\x06VERIFY\x10\x01\x12\x16\n\x12POOR_QUALITY_PHOTO\x10\x02\"\x04\x08\x07\x10\x0f*P\n\x05ROLES\x12\x14\n\x10ROLE_PORTAL_USER\x10\x00\x12\x15\n\x11ROLE_PORTAL_ADMIN\x10\x01\x12\x1a\n\x16ROLE_PORTAL_SUPERADMIN\x10\x02\x32\xcd\x04\n\x0bUserService\x12:\n\nCreateUser\x12\x17.user.CreateUserRequest\x1a\x13.user.TotalResponse\x12J\n\x12OrdinaryUpdateUser\x12\x1f.user.OrdinaryUpdateUserRequest\x1a\x13.user.TotalResponse\x12H\n\x11\x43hangePhoneNumber\x12\x1e.user.ChangePhoneNumberRequest\x1a\x13.user.TotalResponse\x12:\n\nDeleteUser\x12\x17.user.DeleteUserRequest\x1a\x13.user.TotalResponse\x12L\n\x12VerifyUserWithDocs\x12\x1f.user.VerifyUserWithDocsRequest\x1a\x13.user.TotalResponse(\x01\x12\x44\n\x0fLightVerifyUser\x12\x1c.user.LightVerifyUserRequest\x1a\x13.user.TotalResponse\x12\x42\n\x0e\x43hangeUserRole\x12\x1b.user.ChangeUserRoleRequest\x1a\x13.user.TotalResponse\x12X\n\x19UserDataValidationByAdmin\x12&.user.UserDataValidationByAdminRequest\x1a\x13.user.TotalResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'user_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_ADMIN_CONCLUSION']._serialized_start=1432
  _globals['_ADMIN_CONCLUSION']._serialized_end=1513
  _globals['_ROLES']._serialized_start=1515
  _globals['_ROLES']._serialized_end=1595
  _globals['_USERPRIVATEMETA']._serialized_start=21
  _globals['_USERPRIVATEMETA']._serialized_end=298
  _globals['_USER']._serialized_start=301
  _globals['_USER']._serialized_end=631
  _globals['_AVAILABLEFIELDSTOUPDATE']._serialized_start=634
  _globals['_AVAILABLEFIELDSTOUPDATE']._serialized_end=785
  _globals['_TOTALRESPONSE']._serialized_start=787
  _globals['_TOTALRESPONSE']._serialized_end=901
  _globals['_CREATEUSERREQUEST']._serialized_start=903
  _globals['_CREATEUSERREQUEST']._serialized_end=948
  _globals['_ORDINARYUPDATEUSERREQUEST']._serialized_start=950
  _globals['_ORDINARYUPDATEUSERREQUEST']._serialized_end=1022
  _globals['_CHANGEPHONENUMBERREQUEST']._serialized_start=1024
  _globals['_CHANGEPHONENUMBERREQUEST']._serialized_end=1120
  _globals['_DELETEUSERREQUEST']._serialized_start=1122
  _globals['_DELETEUSERREQUEST']._serialized_end=1158
  _globals['_VERIFYUSERWITHDOCSREQUEST']._serialized_start=1160
  _globals['_VERIFYUSERWITHDOCSREQUEST']._serialized_end=1212
  _globals['_CHANGEUSERROLEREQUEST']._serialized_start=1214
  _globals['_CHANGEUSERROLEREQUEST']._serialized_end=1264
  _globals['_USERDATAVALIDATIONBYADMINREQUEST']._serialized_start=1266
  _globals['_USERDATAVALIDATIONBYADMINREQUEST']._serialized_end=1384
  _globals['_LIGHTVERIFYUSERREQUEST']._serialized_start=1386
  _globals['_LIGHTVERIFYUSERREQUEST']._serialized_end=1430
  _globals['_USERSERVICE']._serialized_start=1598
  _globals['_USERSERVICE']._serialized_end=2187
# @@protoc_insertion_point(module_scope)
