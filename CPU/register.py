class Register:
    def __init__(self, name="", regtype="", fields={}):
        self.__name = name
        self.__type = regtype
        self.__fields = fields

    @property
    def Name(self):
        return self.__name

    @property
    def Field(self):
        return self.__name.lower()

    @property
    def Type(self):
        return self.__type

    @property
    def Fields(self):
        return self.__fields
