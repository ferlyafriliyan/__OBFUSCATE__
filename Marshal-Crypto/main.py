import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Protocol.KDF import PBKDF2
import marshal
import secrets

def generate_random_passphrase():
    return secrets.token_hex(16)  # Menghasilkan passphrase acak dengan panjang 16 karakter (32 digit hex)

def obfuscate_code(content, output_file):
    passphrase = generate_random_passphrase()
    salt = base64.b64decode('r46hLfgxSd0Vl76xD8UmdQ==')

    # Menggunakan marshal untuk mengompilasi kode Python
    compiled_code = marshal.dumps(compile(content, '<string>', 'exec'))

    # Enkripsi dengan AES
    key_iv = PBKDF2(passphrase, salt, dkLen=32, count=1000000)
    key = key_iv[:16]
    iv = key_iv[16:]

    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Menambahkan padding ke data sebelum dienkripsi
    padded_data = pad(compiled_code, AES.block_size)
    
    encrypted_code = cipher.encrypt(padded_data)

    # Encode hasil enkripsi ke base64
    encoded_encrypted_code = base64.b64encode(encrypted_code).decode('utf-8')

    # Membuat kode obfuscated yang akan ditulis ke file
    obfuscated_code = f'''_A='base64';from Crypto.Cipher import AES;from Crypto.Util.Padding import unpad,pad;from Crypto.Protocol.KDF import PBKDF2
passphrase='{passphrase}'
salt=__import__(_A).b64decode("{base64.b64encode(salt).decode('utf-8')}")
key_iv=PBKDF2(passphrase,salt,dkLen=32,count=1000000);key=key_iv[:16];iv=key_iv[16:]
cipher_text=__import__(_A).b64decode('{encoded_encrypted_code}')
exec(__import__('marshal').loads(unpad(AES.new(key, AES.MODE_CBC, iv).decrypt(cipher_text), AES.block_size)))
'''

    # Menyimpan kode obfuscated ke file
    with open(output_file, 'w') as file:
        file.write(obfuscated_code)

input_file = input(f'Input File : ')
with open(input_file, 'rb') as f:
    content = f.read()

output_file = 'output_obfuscated.py'

obfuscate_code(content, output_file)
