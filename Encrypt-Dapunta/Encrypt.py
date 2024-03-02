import os
import sys
import re
import base64
import marshal
import zlib
import dis

def clear():
    os.system('clear' if 'linux' in sys.platform.lower() else 'cls')

class Encrypt():

    def __init__(self):
        self.code_list = []

    def InputCode(self, file_path):
        with open(file_path, 'rb') as file:
            self.code_list = file.read()

        self.code_string = self.code_list.decode('utf-8')

    def AskLoop(self):
        self.loop = int(input('Berapa Lapis : '))
        code = self.code_string
        for i in range(self.loop):
            code = self.ExeCrypt(code)
        self.result = code

        # Menyimpan hasil enkripsi ke file
        output_file_path = input("Masukkan path file output untuk menyimpan hasil enkripsi: ")
        with open(output_file_path, 'w') as output_file:
            output_file.write(self.result)

        print('\nHasil : \n{}\n'.format(self.result))
        print(f'Berhasil obfuscate file, Tersimpan di {output_file_path}')


    def ExeCrypt(self, code):
    #    b = marshal.dumps(code)
        b = marshal.dumps(compile(code, '', 'exec'))
        c = zlib.compress(b)
        d = base64.b64encode(c).decode('utf-8')
        result = f"""exec(__import__("marshal").loads(__import__("zlib").decompress(__import__("base64").b64decode(b'{d[::-1]}'[::-1]))), globals())"""
        return result

class Decrypt():

    def __init__(self):
        pass

    def InputString(self):
        a = input("Masukkan String : ")
        if 'exec(' in a:
            b = re.search(r"b'(.*?)'", str(a)).group(1)
        else:
            b = a
        if b.startswith('='):
            c = b[::-1]
        else:
            c = b
        self.code_string = c
        self.ExeDec()

    def ExeDec(self):
        a = base64.b64decode(self.code_string)
        b = zlib.decompress(a)
        c = marshal.loads(b)
        dis.dis(c)

def Menu():
    print('[1] Encrypt\n[2] Decrypt')
    x = int(input('Pilih : '))
    print('')
    if x == 1:
        file_path = input("Masukkan path file: ")
        ENC = Encrypt()
        ENC.InputCode(file_path)
        ENC.AskLoop()
    elif x == 2:
        DEC = Decrypt()
        DEC.InputString()

if __name__ == '__main__':
    clear()
    Menu()

