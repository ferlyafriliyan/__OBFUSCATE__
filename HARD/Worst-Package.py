import marshal
import zlib
import bz2
import lzma
import base64
import os
import sys
import platform

def read_file():
    input_file = input("Input File: ")
    with open(input_file, 'rb') as f:
        read_input = f.read()
    return read_input

def Banner():
    os.system('cls' if 'win' in sys.platform.lower() else 'clear')
    print(f"""
  ___ ___                  .___ ________ _____________________
 /   |   \_____ _______  __| _/ \_____  \\\______   \_   _____/
/    ~    \__  \\\_  __ \/ __ |   /   |   \|    |  _/|    __)  
\    Y    // __ \|  | \/ /_/ |  /    |    \    |   \|     \   
 \___|_  /(____  /__|  \____ |  \_______  /______  /\___  /   
       \/      \/           \/          \/       \/     \/    
""")

def obfuscate_and_save():
    content = read_file()
    # Compile the Python code
    compiled_code = compile(content, '', 'exec')
    # Marshal the compiled code
    marshaled_code = marshal.dumps(compiled_code)
    # Compress using zlib
    zlib_compressed = zlib.compress(marshaled_code)
    # Compress using bz2
    bz2_compressed = bz2.compress(zlib_compressed)
    # Compress using lzma
    lzma_compressed = lzma.compress(bz2_compressed)
    # Build the final obfuscated code
    __OBFUSCATE__1 = f'''#i/urs/bin/python3.11
try:
	__Minh_x_Uyen__=locals();__Botname__='@ChatGPT_bot';__Date_Obf__='2024-02-07 - Admin (UTC)';__Mode_ENC__='3.11.6 -> (main) - version: 1.0.2';__OBFUSCATION_BY__='MinhNguyen2412_x_NgocUyen1907'
	class PyObject:
		def PythonCodeObject(code):return code*2
		def Obfuscator(code_,_code):__Minh_x_Uyen__[code_]=_code;return __Minh_x_Uyen__[code_]
		def Windows(code):
			code_=[]
			while code:
				Minh_Nguyen=__import__('_bz2').BZ2Decompressor()
				try:__Minh_x_Uyen__=Minh_Nguyen.decompress;_code=__Minh_x_Uyen__(code)
				except OSError:
					if code_:break
					else:raise
				code_.append(_code);code=Minh_Nguyen.unused_data
			return b''.join(code_)
		def KaliLinux(code,format=__import__('_lzma').FORMAT_AUTO,memlimit=None,filters=None):
			code_=[]
			while True:
				Ngoc_Uyen=__import__('_lzma').LZMADecompressor(format,memlimit,filters)
				try:__Minh_x_Uyen__=Ngoc_Uyen.decompress;_code=__Minh_x_Uyen__(code)
				except OSError:
					if code_:break
					else:raise
				code_.append(_code);code=Ngoc_Uyen.unused_data
				if not code:break
			return b''.join(code_)
	__CodeObjectData__=PyObject.PythonCodeObject(__import__('math').floor(5)),PyObject.Obfuscator('__CodeObjectData__',{lzma_compressed});__import__('builtins').eval(__import__('marshal').loads(__import__('zlib').decompress(PyObject.Windows(PyObject.KaliLinux(__CodeObjectData__[__import__('math').floor(1)])))))
except MemoryError:print('MemoryError: >> GOOD LUCK!! , OBF by [NgocUyen x MinhNguyen] <<')
except Exception as e:__import__('logging').error(__import__('traceback').format_exc())'''

    a = marshal.dumps(compile(__OBFUSCATE__1.encode(), '', 'exec'))
    b = bz2.compress(a)

    __OBFUSCATE__2 = f'''#i/usr/bin/python3.11
try:exec(__import__('marshal').loads(__import__('bz2').BZ2Decompressor().decompress({repr(b[::-1])}[::-1])), globals())
except KeyboardInterrupt:print();__import__('sys').exit()
except Exception as e:__import__('logging').error(__import__('traceback').format_exc())'''

    c = marshal.dumps(compile(__OBFUSCATE__2.encode(), '', 'exec'))
    d = zlib.compress(c)
    e = base64.b64encode(d).decode()

    __OBFUSCATE__3 = f'''#i/urs/bin/python3.11
try:exec(__import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode({repr(e[::-1])}[::-1]))), globals())
except KeyboardInterrupt:print();__import__('sys').exit()
except Exception as e:__import__('logging').error(__import__('traceback').format_exc())'''

    f = marshal.dumps(compile(__OBFUSCATE__3.encode(), '', 'exec'))
    g = lzma.compress(f)
    h = bz2.compress(g)
    i = base64.b64encode(h)

    __OBFUSCATE__4 = f'''#i/usr/bin/python3.11
try:exec(__import__('marshal').loads(__import__('lzma').LZMADecompressor().decompress(__import__('bz2').BZ2Decompressor().decompress(__import__('base64').b64decode({repr(i[::-1])}[::-1])))), globals())
except KeyboardInterrupt:print();__import__('sys').exit()
except Exception as e:__import__('logging').error(__import__('traceback').format_exc())'''

    code = __OBFUSCATE__4.encode()
    j = compile(code, '', 'exec')
    k = marshal.dumps(j)
    l = bz2.compress(k)
    m = base64.b32hexencode(l)
    n = zlib.compress(m, level=zlib.Z_BEST_COMPRESSION)

    anti_skid = f'''

try:
    if OBFUSCATED_BY != '@Ferly Afriliyan':
        int('skid')
except:
    input("Gak usah Direcode Goblok !")
    __import__('sys').exit()

'''
    skid_ = compile(anti_skid, '', 'exec')
    o = marshal.dumps(skid_)
    p = bz2.compress(o)
    q = base64.b32hexencode(p)
    r = zlib.compress(q, level=zlib.Z_BEST_COMPRESSION)

    obfuscate_skid = f'''
eval(__import__('marshal').loads(__import__('_bz2').BZ2Decompressor().decompress(__import__('base64').b32hexdecode(__import__('zlib').decompress({repr(r[::-1])}[::-1])))), globals())'''
    
    __OBFUSCATE__5 = f'''
OBFUSCATED_BY = '@Ferly Afriliyan'
# try:
# 	if OBFUSCATED_BY!='@Ferly Afriliyan':int('skid')
# except:input('Gak usah Direcode Goblok !');__import__('sys').exit()
{obfuscate_skid};eval(__import__('marshal').loads(__import__('_bz2').BZ2Decompressor().decompress(__import__('base64').b32hexdecode(__import__('zlib').decompress({repr(n[::-1])}[::-1])))), globals())'''

    s = marshal.dumps(compile(__OBFUSCATE__5.encode(), '', 'exec'))
    t = zlib.compress(s)
    u = base64.b64encode(t).decode('utf-8')

    __OBFUSCATE__6 = f'''
__OBFUSCATE__BY = "Dapunta x Denventa."
try:exec(__import__("marshal").loads(__import__("zlib").decompress(__import__("base64").b64decode({repr(u[::-1])}[::-1]))), globals())
except KeyboardInterrupt:print();__import__('sys').exit()
except Exception as e:__import__('logging').error(__import__('traceback').format_exc())'''

    s = marshal.dumps(compile(__OBFUSCATE__6.encode(), '', 'exec'))
    t = zlib.compress(s)
    u = bz2.compress(t)
    v = lzma.compress(u)

    __OBFUSCATE__7 = f'''#i/urs/bin/python3.11
try:
	__Minh_x_Uyen__=locals();__Botname__='@ChatGPT_bot';__Date_Obf__='2024-02-07 - Admin (UTC)';__Mode_ENC__='3.11.6 -> (main) - version: 1.0.2';__OBFUSCATION_BY__='MinhNguyen2412_x_NgocUyen1907'
	class PyObject:
		def PythonCodeObject(code):return code*2
		def Obfuscator(code_,_code):__Minh_x_Uyen__[code_]=_code;return __Minh_x_Uyen__[code_]
		def Windows(code):
			code_=[]
			while code:
				Minh_Nguyen=__import__('_bz2').BZ2Decompressor()
				try:__Minh_x_Uyen__=Minh_Nguyen.decompress;_code=__Minh_x_Uyen__(code)
				except OSError:
					if code_:break
					else:raise
				code_.append(_code);code=Minh_Nguyen.unused_data
			return b''.join(code_)
		def KaliLinux(code,format=__import__('_lzma').FORMAT_AUTO,memlimit=None,filters=None):
			code_=[]
			while True:
				Ngoc_Uyen=__import__('_lzma').LZMADecompressor(format,memlimit,filters)
				try:__Minh_x_Uyen__=Ngoc_Uyen.decompress;_code=__Minh_x_Uyen__(code)
				except OSError:
					if code_:break
					else:raise
				code_.append(_code);code=Ngoc_Uyen.unused_data
				if not code:break
			return b''.join(code_)
	__CodeObjectData__=PyObject.PythonCodeObject(__import__('math').floor(5)),PyObject.Obfuscator('__CodeObjectData__',{v});__import__('builtins').eval(__import__('marshal').loads(__import__('zlib').decompress(PyObject.Windows(PyObject.KaliLinux(__CodeObjectData__[__import__('math').floor(1)])))))
except MemoryError:print('MemoryError: >> GOOD LUCK!! , OBF by [NgocUyen x MinhNguyen] <<')
except Exception as e:__import__('logging').error(__import__('traceback').format_exc())'''

    # Save the obfuscated code to a new file
    output_file = input("Output File: ")
    with open(output_file, 'w') as f:
        f.write(__OBFUSCATE__7)

if __name__ == '__main__':
    try:
        Banner()
        obfuscate_and_save()
    except KeyboardInterrupt:
        print()
        __import__('sys').exit()
    except Exception as e:
        __import__('logging').error(__import__('traceback').format_exc())