from CPU.cpu import CPU


def main():
    cpu = CPU(filepath='json/Ricoh5A22.json')
    cpu.GenerateCPU()
    from build.ricoh5a22 import Ricoh5A22
    snescpu = Ricoh5A22()
    snescpu.C = 0xEEFF
    print("%02X" % snescpu.A)
    print("%02X" % snescpu.B)


if __name__ == '__main__':
    main()
