import os
import sys
import marshal
import zlib

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
       
    #   b = marshal.dumps(code)
        b = marshal.dumps(compile(code, '', 'exec'))
        c = zlib.compress(b)
        d = __import__('bz2').compress(c)
        e = __import__('lzma').compress(d)

        result = f"""#i/urs/bin/python3.11
try:
    __Minh_x_Uyen__=locals()
    __Botname__ = '@ChatGPT_bot'
    __Date_Obf__ = '2024-01-01 - Admin (UTC)'
    __Mode_ENC__  = '3.11.6 -> (main) - version: 1.0.1'
    __OBFUSCATION_BY__ = 'MinhNguyen2412_x_NgocUyen1907'
    class PyObject:
        def PythonCodeObject(code: int) -> int:return code*2
        def Obfuscator(code_, _code: (...,)) -> (...,):__Minh_x_Uyen__[code_] = _code;return __Minh_x_Uyen__[code_]
        def Windows(code):
            code_ = []
            while code:
                Minh_Nguyen = __import__('_bz2').BZ2Decompressor()
                try:__Minh_x_Uyen__=Minh_Nguyen.decompress;_code = __Minh_x_Uyen__(code)
                except OSError:
                    if code_:break
                    else:raise
                code_.append(_code)
                code = Minh_Nguyen.unused_data
            return b"".join(code_)
        def KaliLinux(code, format=__import__('_lzma').FORMAT_AUTO, memlimit=None, filters=None):
            code_ = []
            while True:
                Ngoc_Uyen = __import__('_lzma').LZMADecompressor(format, memlimit, filters)
                try:__Minh_x_Uyen__=Ngoc_Uyen.decompress;_code = __Minh_x_Uyen__(code)
                except OSError:
                    if code_:break
                    else:raise
                code_.append(_code)
                code = Ngoc_Uyen.unused_data
                if not code:break
            return b"".join(code_)
    __CodeObjectData__ = PyObject.PythonCodeObject(__import__('math').floor(5)),PyObject.Obfuscator('__CodeObjectData__',{e})
    __import__('builtins').eval(__import__('marshal').loads(__import__('zlib').decompress(PyObject.Windows(PyObject.KaliLinux(__CodeObjectData__[__import__('math').floor(1)])))))
except Exception as e:__import__('logging').error(__import__('traceback').format_exc())"""
        return result

def Menu():
    print('[1] Encrypt\n[2] Exit!')
    x = int(input('Pilih : '))
    print('')
    if x == 1:
        file_path = input("Masukkan path file: ")
        ENC = Encrypt()
        ENC.InputCode(file_path)
        ENC.AskLoop()
    elif x == 2:
        exit()

if __name__ == '__main__':
    clear()
    Menu()
