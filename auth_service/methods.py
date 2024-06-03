from enum import Enum


class MethodsEnum(str, Enum):
    CREATE_USER = "CreateUser"
    ORDINARY_UPDATE_USER = "OrdinaryUpdateUser"
    CREATE_SESSION = "CreateSession"
