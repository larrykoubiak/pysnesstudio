from ctypes import (
    Union, Structure,
    c_uint8, c_uint16, c_uint32
)


class bitflag(Structure):
    _fields_ = [("value", c_uint8, 1)]


class _bitfields8(Structure):
    _fields_ = [
        ("B0", c_uint8, 1),
        ("B1", c_uint8, 1),
        ("B2", c_uint8, 1),
        ("B3", c_uint8, 1),
        ("B4", c_uint8, 1),
        ("B5", c_uint8, 1),
        ("B6", c_uint8, 1),
        ("B7", c_uint8, 1)
    ]


class bitfield8(Union):
    _fields_ = [("value", c_uint8), ("fields", _bitfields8)]


class _bitfields16(Structure):
    _fields_ = [
        ("B0", c_uint8, 1),
        ("B1", c_uint8, 1),
        ("B2", c_uint8, 1),
        ("B3", c_uint8, 1),
        ("B4", c_uint8, 1),
        ("B5", c_uint8, 1),
        ("B6", c_uint8, 1),
        ("B7", c_uint8, 1),
        ("B8", c_uint8, 1),
        ("B9", c_uint8, 1),
        ("BA", c_uint8, 1),
        ("BB", c_uint8, 1),
        ("BC", c_uint8, 1),
        ("BD", c_uint8, 1),
        ("BE", c_uint8, 1),
        ("BF", c_uint8, 1)
    ]


class bitfield16(Union):
    _fields_ = [("value", c_uint16), ("fields", _bitfields16)]


class reg8(Structure):
    _fields_ = [("value", c_uint8)]


class _reg16fields(Structure):
    _fields_ = [("L", c_uint8), ("H", c_uint8)]


class reg16(Union):
    _fields_ = [("value", c_uint16), ("fields", _reg16fields)]


class _reg24fields(Structure):
    _fields_ = [("L", c_uint8), ("H", c_uint8), ("B", c_uint8)]


class reg24(Union):
    _fields_ = [("value", c_uint32), ("fields", _reg24fields)]
