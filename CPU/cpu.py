import json
from CPU.register import Register


class CPU:
    def __init__(self, name="", registers={}, filepath=None):
        self.__name = name
        self.__registers = registers
        if filepath is not None:
            self.Load(filepath)

    def serialize(self, o):
        if isinstance(o, CPU):
            return {'__CPU__': True, 'name': o.Name, 'registers': o.Registers}
        if isinstance(o, Register):
            return {'__Register__': True, 'name': o.Name,
                    'type': o.Type, 'fields': o.Fields}
        return json.JSONEncoder.default(self, o)

    def deserialize(self, o):
        if '__CPU__' in o:
            return CPU(o['name'], o['registers'])
        if '__Register__' in o:
            return Register(o['name'], o['type'], o['fields'])
        return o

    def Load(self, filepath):
        with open(filepath) as f:
            data = json.load(f, object_hook=self.deserialize)
            vars(self).update(data.__dict__)

    def Save(self, filepath):
        with open(filepath, 'w') as outfile:
            json.dump(self, default=self.serialize,
                      sort_keys=True, indent=4, fp=outfile)

    def GenerateCPU(self):
        result = "from CPU.regtypes import (\n\treg8, reg16, reg24,\n"
        result += "\tbitfield8, bitflag\n)"
        result += "\n\n\nclass " + self.Name + ":\n"
        result += "\tdef __init__(self):\n"
        for r in self.Registers.values():
            result += "\t\tself.__" + r.Field + " = " + r.Type + "()\n"
        result += "\n"
        for r in self.Registers.values():
            for f, p in r.Fields.items():
                result += "\t@property\n"
                result += "\tdef " + p + "(self):\n"
                result += "\t\treturn self.__" + r.Field + ".fields." + f
                result += "\n\n\t@" + p + ".setter\n"
                result += "\tdef " + p + "(self, val):\n"
                result += "\t\tself.__" + r.Field + ".fields." + f + " = val\n"
                result += "\n"
            result += "\t@property\n\tdef " + r.Name + "(self):\n"
            result += "\t\treturn self.__" + r.Field + ".value\n\n"
            result += "\t@" + r.Name + ".setter\n"
            result += "\tdef " + r.Name + "(self, val):\n"
            result += "\t\tself.__" + r.Field + ".value = val\n\n"
        result = result.replace('\t', '    ')[:-1]
        outputname = 'build/' + self.Name.lower() + '.py'
        with open(outputname, 'w') as outfile:
            outfile.write(result) 

    @property
    def Name(self):
        return self.__name

    @Name.setter
    def Name(self, val):
        self.__name = val

    @property
    def Registers(self):
        return self.__registers


if __name__ == '__main__':
    # cpu = CPU()
    # cpu.Name = "Ricoh5A22"
    # cpu.Registers['AB'] = Register('AB', 'reg16', {'H': 'ABH', 'L': 'ABL'})
    # cpu.Registers['DB'] = Register('DB', 'reg8')
    # cpu.Registers['PC'] = Register('PC', 'reg24',
    #                                {'B': 'PBR', 'H': 'PCH', 'L': 'PCL'})
    # cpu.Registers['P'] = Register('P', 'bitfield8',
    #                               {'B0': 'P_C',
    #                                'B1': 'P_Z',
    #                                'B2': 'P_I',
    #                                'B3': 'P_D',
    #                                'B4': 'P_X',
    #                                'B5': 'P_M',
    #                                'B6': 'P_V',
    #                                'B7': 'P_N'})
    # cpu.Registers['E'] = Register('E', 'bitflag')
    # cpu.Registers['S'] = Register('S', 'reg16', {'H': 'SH', 'L': 'SL'})
    # cpu.Registers['D'] = Register('D', 'reg16', {'H': 'DH', 'L': 'DL'})
    # cpu.Registers['X'] = Register('X', 'reg16', {'H': 'XH', 'L': 'XL'})
    # cpu.Registers['Y'] = Register('Y', 'reg16', {'H': 'YH', 'L': 'YL'})
    # cpu.Registers['C'] = Register('C', 'reg16', {'H': 'B', 'L': 'A'})
    # cpu.Registers['DBR'] = Register('DBR', 'reg8')
    # cpu.Save('test.json')
    cpu = CPU(filepath='test.json')
    cpu.GenerateCPU()
