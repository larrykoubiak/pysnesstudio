from enum import Enum


class AddressingModeEnum(Enum):
    ADDRESSING_MODE_NOT_APPLICABLE = 0
    ADDRESSING_MODE_ABSOLUTE = 1
    ADDRESSING_MODE_ACCUMULATOR = 2
    ADDRESSING_MODE_ABSOLUTE_INDEXED_X = 3
    ADDRESSING_MODE_ABSOLUTE_INDEXED_Y = 4
    ADDRESSING_MODE_ABSOLUTE_LONG = 5
    ADDRESSING_MODE_ABSOLUTE_LONG_INDEXED_X = 6
    ADDRESSING_MODE_ABSOLUTE_INDIRECT = 7
    ADDRESSING_MODE_ABSOLUTE_INDIRECT_LONG = 8
    ADDRESSING_MODE_ABSOLUTE_INDEXED_INDIRECT_X = 9
    ADDRESSING_MODE_DIRECT_PAGE = 10
    ADDRESSING_MODE_DIRECT_PAGE_INDEXED_X = 11
    ADDRESSING_MODE_DIRECT_PAGE_INDEXED_Y = 12
    ADDRESSING_MODE_DIRECT_PAGE_INDIRECT = 13
    ADDRESSING_MODE_DIRECT_PAGE_INDIRECT_LONG = 14
    ADDRESSING_MODE_STACK_RELATIVE_INDIRECT_INDEXED_Y = 15
    ADDRESSING_MODE_DIRECT_PAGE_INDEXED_INDIRECT_X = 16
    ADDRESSING_MODE_STACK_RELATIVE = 17
    ADDRESSING_MODE_DIRECT_PAGE_INDIRECT_INDEXED_Y = 18
    ADDRESSING_MODE_DIRECT_PAGE_INDIRECT_LONG_INDEXED_Y = 19
    ADDRESSING_MODE_IMPLIED = 20
    ADDRESSING_MODE_PROGRAM_COUNTER_RELATIVE = 21
    ADDRESSING_MODE_PROGRAM_COUNTER_RELATIVE_LONG = 22
    ADDRESSING_MODE_STACK = 23
    ADDRESSING_MODE_STACK_ABSOLUTE = 24
    ADDRESSING_MODE_STACK_DIRECT_PAGE_INDIRECT = 25
    ADDRESSING_MODE_STACK_PROGRAM_COUNTER_RELATIVE = 26
    ADDRESSING_MODE_STACK_INTERRUPT = 27
    ADDRESSING_MODE_BLOCK_MOVE = 28
    ADDRESSING_MODE_IMMEDIATE = 29
    ADDRESSING_MODE_IMMEDIATE_STATUS = 30


class AddressingEnum(Enum):
    NA = 0
    ABSOLUTE = 1
    IMPLIED = 2
    ABSOLUTE_LONG = 3
    DIRECT_PAGE = 4
    STACK = 5
    PROGRAM_COUNTER = 6
    BLOCK = 7
    IMMEDIATE = 8


class IndirectionEnum(Enum):
    NA = 0
    DIRECT = 1
    INDIRECT = 2
    IMMEDIATE = 3


class IndexedEnum(Enum):
    NA = 0
    X = 1
    Y = 2


class AddressingMode:
    def __init__(self, element=None):
        self.__id = 0
        self.__constant = AddressingModeEnum.ADDRESSING_MODE_NOT_APPLICABLE
        self.__description = ""
        self.__format8bit = ""
        self.__format16bit = ""
        self.__inputlenght8bit = 0
        self.__inputlenght16bit = 0
        self.__addressing = AddressingEnum.NA
        self.__indirection = IndirectionEnum.NA
        self.__indexed = IndexedEnum.NA
        if element is not None:
            self.__parseElement(element)

    def __parseElement(self, element):
        self.__id == int(element.find('./Id').text)
        self.__constant = AddressingModeEnum[element.find('./Constant').text]
        self.__description = element.find('./Description').text
        self.__format8bit = element.find('./Format8Bit').text
        self.__format16bit = element.find('./Format16Bit').text
        self.__inputlenght8bit = int(element.find('./InputLength8Bit').text)
        self.__inputlenght16bit = int(element.find('./InputLength16Bit').text)
        self.__addressing = AddressingEnum[element.find('./Addressing').text.upper().replace(' ','_')]
        self.__indirection = IndirectionEnum[element.find('./Indirection').text.upper()]
        self.__indexed = IndexedEnum[element.find('./Indexed').text.upper()]

    @property
    def Id(self):
        return self.__id

    @property
    def Constant(self):
        return self.__constant

    @property
    def Description(self):
        return self.__description

    @property
    def Format8Bit(self):
        return self.__format8bit

    @property
    def Format16Bit(self):
        return self.__format16bit

    @property
    def InputLength8Bit(self):
        return self.__inputlenght8bit

    @property
    def InputLength16Bit(self):
        return self.__inputlenght16bit

    @property
    def Addressing(self):
        return self.__addressing

    @property
    def Indirection(self):
        return self.__indirection

    @property
    def Indexed(self):
        return self.__indexed

    def __str__(self):
        result = "AddressingMode"
        result += " Id=" + str(self.Id)
        result += " Constant=" + str(self.Constant)
        result += " Description='" + self.Description + "'"
        result += " Format8Bit='" + self.Format8Bit + "'"
        result += " Format16Bit='" + self.Format16Bit + "'"
        result += " InputLength8Bit=" + str(self.InputLength8Bit)
        result += " InputLength16Bit=" + str(self.InputLength16Bit)
        result += " Addressing=" + str(self.Addressing)
        result += " Indirection=" + str(self.Indirection)
        result += " Indexed=" + str(self.Indexed)
        return result

    def __repr__(self):
        return str(self)