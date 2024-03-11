import base64
import marshal
import zlib
import os, sys

def main():
    os.system('cls' if 'win' in sys.platform.lower() else 'clear')
    
    input_file_path = input("Masukkan path file input: ")
    output_file_path = input("Masukkan path file output: ")
    encrypt_method = input("Pilih metode enkripsi (low/hard): ")

    with open(input_file_path, 'r') as file:
        code = file.read()

    if encrypt_method == "low":
        encrypted_code = LowEncrypt(code)
    elif encrypt_method == "hard":
        encrypted_code = HardEncrypt(code)
    else:
        print("Metode enkripsi tidak valid. Gunakan 'low' atau 'hard'.")
        return

    with open(output_file_path, 'w') as output_file:
        output_file.write(encrypted_code)

    print(f"Enkripsi selesai. Hasil disimpan di '{output_file_path}'.")

def LowEncrypt(code):
    a = marshal.dumps(compile(code, '', 'exec'))
    b = zlib.compress(a)
    c = base64.b64encode(b).decode('utf-8')
    result = f"""exec(__import__("marshal").loads(__import__("zlib").decompress(__import__("base64").b64decode(b'{c[::-1]}'[::-1]))))"""
    return result

def HardEncrypt(code):
    a1 = marshal.dumps(compile(code, '', 'exec'))
    b1 = zlib.compress(a1)
    c1 = base64.b64encode(b1).decode('utf-8')
    d1 = Layering(c1[::-1])
    l1 = """exec(__import__("marshal").loads(__import__("zlib").decompress(__import__("base64").b64decode(b'==AbYuHWvV/vvf+/A+/Xr//fbjfpvdvzyaX/np7CEPagQf4xeAFw63Hn1/7wkVIoRIV+SKCZdLsELD6S/jUIU2KBd85X+xwMxXbAb/3xQYHMQdFAivMLbE+dCJ+ixDmgyJgG9DGSjWEZSDs5QQM1gYDchmqL/a2uhPaJPSVkamgXPjWM/UQ0oosAZIKKsl6h7ZnE8Kx2FK29Oj9gISrLNxF+TwqzkE9Rfo+JHiarlM3hMhCfN/ZjAotw+hxpa2o3aX6OyAwXdGssR1MuLvMDDPiGBvVNvikqaUqDT94ukFlBtIkRbcBcFZ8uTO/dyWJlBElhSqCpduFOrGBVqgh+wSUNcJWqvRtSDeRN/Hhv95BqijWT8tCCzArMdqwj1UzXuSJ5uZEBN344uE9hvfIu+fVv6c5Ka6ToHZVMp3gHy7IwHlT2lcXw+MgXoSbLjG2yRSS83YncXhXk6qpWnKJz83+JIFKmmRAuJbzylo90eEBS7PBJnglnqwaNkJW42bvBpgmkSD8xvnyfTmDqZnu6//QFqdN+kguXV/s2TjhQnxFinjXNYZUelSSSfd8s7yA+ylhiyuNNxJkW0Emt8/ZVFvofdvsRHP6p4cteEWyDDRlQbxGRKq2rrlRSK07V1RTCsaRJZ9jX4LBVyyc99bYFbO81N29AZ6gIFJJgi8ElZNYfeHaKTjmbsaV1EBLuzsYEBR5nww3kGpg4hEteRrSVanswahnl4ZOHo4XoIQsMX5+wMBj3jNFP+iui7ZsIFoKszJLqNE2KWanUZ2WIuxzZ3SDyfEY+VfSfLdTe62vOGKcCsA8CKQF4kfFLFD27yDogR/x0le+64KrHDQo9y70AUO2lEthe0i+TQtNsH2ONfVr17GCvF5NdA7k0z6uQyU4kWMFtHOnqMKLZxRTioG9PXJdXDE3xPc2ItdE7JHi1nJk5YEl92PG8NvkYo8/IPVIRD3uGNFNbFs6CxrEmbC58fqZk+RbhhrNIwFk7nZZ7rS1qTQMYDCmPQTqxI49zBA0LFHFhurPYtCsQ5wTG+O9NRG1NXIqRegcunx+sDrTVacjn550St7/DwFwFSIW+3LCVvGsMsFF/b4IhCRPLuLqKHIfiDrawQsFEP8B4Id+2nV04eG3XwMTbmmdrVM3ja21UzdVLLYimpTUKPs8sLNB1V2lsq2Hb/ihVBQ8n38N0Kxcd2UMeE/TXtxkJpYhD1kVmiPsEUr7RCcqVvjVnZNuaivp8orI+muLmkLaAygut/uUTCEEFWR1ur9oJXd81m3OQ6Uq9EBMA1oNpRuJ0NAdR7/t6W4wuAQajbVTmlmah1K3AHpMhBR/DIJ9J2dzCyQX8+ISbdRwVdhxQa/f5OmTeo4knJhy0BthLOOFDZzyOaOH04qoQStPjkokxKCfbXgcIgjF3q8dZkoXGUSzrMxqMZRRNeEsb2tF4uNwUeZw1Xkndo5vGNu94SQ+EPpylysmxqYloDa+eRcgZUr6dq0uJhHpBJMXaFHV/f37qzkaMy1XpzuHwhOaYrFFyxjqISZNJ3ful+YBL9hqjkibYugl07GbTl66MJ0EPS5JI56vuCtqg9iJVA8FlueHpLea69sXA5kBSGx3TjyS2hCbe7C7Lp88u3j0VUp1mtedZK7ZCU+NXNLevA0Kbb9OEbs3RVFUABm6aXs2kNGUKJ6L7MnDBE1k8H5EVWbGChfaFW0YZGI+si4yj+25DcaS3N9anv6coIk/xyAJHnoYPwzoH+Wt02bJk5xBKeP1xmonZbmGi9PvwUEtSeU7BRAz0LwtGiPMg/q8DmkzEIl9QDdTUnSaC3NFNzAd6+F+LVprarTRf0dIDfl1f1ETKxIyNhvYEcckhHGvkSTX6a7BWXErKMLCf5jemofDQ7obmIyCZM2BIs9bxreexDS4vlI3qv65AiUCToBuUn3+LigGqat5b8VXOxaC9WhAuC3GvtyFupdf/jrE0Qrvctd9eGCAO+laAavNdsUiEoBx+D0hNWRwtZ8EQLDH35OMyjdqFkCGAt7lUKz3UGX/1Kdv1phOGvVYQaeOpyU+s0RK2Bu0YzkNyaSmjQGvi3PmokCkMJquRfAQK9SR+hxWlmgWV4/BSSyRLPhY9dfvpMs2OxQSU5B5BZ/Y8YAE8XxNJ4aCz4dUhjV5V/hyaNr35gUE7/29/Q6wU+HU17X/YhFMwREnG4Zk31IlNnX+bUhuk1iIYX5QzUtmXs3xbKWyXDSJg0hiRUI24HBncpjVubK/WuZk5cQqg8SLUrB8xVMtb75LcsjqwGHkiDPzTZdTo0WTqnJxFpLQDRV5LWiqs8XQ/ebmjGi+xFj9NzylxoYRRu0In1efXBikiB31VuzevO4Q3HmnX0v49foAQhsfKqvXSiGBe+0dVjsWflQSp7VE8csJJ3PeG7PcqT+ZGviCTUgPhVl0gveimf3wOaHqtETuh3/zhbpwtwxFUkS2hQjz/okw2zLCkk9Bw8SQQUg/PRPBGgvgWpjsfBm68qj/cpm0vkyZMeWuOtAfcSQIrC4t6ykxCs7y4++YW69MT/I+70r3Pp0YoUsnlT8OCpwxhzbTC40okt+jij0kfKVQxI0hZuHtt070lTxUFTsv2effLEh9nbzLQ1e4lectjpMnRdRMAH+6z5ElrO3YvDZKQ1GPU6TJNglGvEibxWc1em9sPWjj+nlAIaU3giHTaYFW846Nz9tA3QfBwt0YOWWdK+CBoWXoFRep1r3lnM56HBF79eKAEdOj0+PMGSXCKw/bGLj04k+G6sD7POiPLaZnFYe92r8D6rGFP+1FrWhgSHpqhRPxbq5q2H+QMq7Qdig3WHp5pDpGYgb+VEgp9N5Tv46DH0QGbzDsbVzOrODkDi85GYb5nEOPU8D4nO2OqpEpHRhZK3+iLtmZam3JYrVtg1eyh7E/ebNeu5CorWBjHDi0DLb0u4ERbNq4nqpvxKRUPMTafIMabjMTtfzjyN15UUpLn1v17bsXFFJBh/yHdnYrgWOupXNK6BGb+Q0KuCi8O6B837yOidX0WS2NRIqq8izhT4l+txSqyeuwzSi49JGbWNZgFY5uFCIIwCEvPlUjNbVjXuQu6HKYmGMhz3A1pLYCWC1GTc+gPSDcdHUeuzH+L6y0phR1Mz8oRITfzWnxFIQICKbuMLgTLz+FKRgETZpa8Uc6kt5VaPf+fB7hAnEl5h5OC+HV47MGjEtKjl4cs3YdsFifFs5wevLlz/cwdTXRiLtgzbesBOOmfBnI4VC9lWUbZMo6kNWbbf96yDXnpT4y650YlKyzt9Et1SxWs8enm9jYtac1n4oiyqOBjJDk/HBE/SSa0ZfQfEaH8uMtLnsYVSMjJnOCCxRBYQc85MJwJKMHvHOf5eeSKMnCHMjqSMtXKAUVF9TpnTwliIdB5cr9rhG+WHVtcPutrItInWAZpyTW0/iCHQAkTQCEtAfEJQkg2OGBgmfr+HFfej8/+CM102TQFymmq/ttF8OcTRmXC9by+7Nk/fTyps//71/v015msD9648//P3rVeGy2//8I7Libp8/7r9//v8X1f1HJXR1Rzsc/EzRj5Vb9ccCK8gNflhuFlvfyKgZof3QYuB2HhZqLxOc0lVxJe'[::-1]))));"""
    l2 = f"""exec(__import__("marshal").loads(__import__("zlib").decompress(__import__("base64").b64decode(((_('{d1}')).encode('utf-8'))[::-1]))))"""
    l3 = 'import base64;' + l1 + l2
    a2 = marshal.dumps(compile(l3, '', 'exec'))
    b2 = zlib.compress(a2)
    c2 = base64.b64encode(b2).decode('utf-8')
    result = f"""exec(__import__("marshal").loads(__import__("zlib").decompress(__import__("base64").b64decode(b'{c2[::-1]}'[::-1]))))"""
    return(result)

def Layering(string):
    layering1 = '\\'.join([str(ord(i)) for i in string])                           #--> char to ascii
    layering2 = base64.b64encode(layering1.encode('utf-8')).decode('utf-8')        #--> ascii to base64
    layering3 = '\\'.join([str(ord(i)) for i in layering2])                        #--> base64 -> char to ascii
    layering4 = base64.b64encode(layering3.encode('utf-8')).decode('utf-8')        #--> ascii to base64
    layering5 = '\\'.join([str(ord(i)) for i in layering4])                        #--> base64 -> char to ascii
    layering6 = '\\'.join([str(hex(int(i))) for i in layering5.split('\\')])       #--> ascii to hex
    layering7 = base64.b64encode(layering6.encode('utf-8')).decode('utf-8')[::-1]  #--> hex to base64 (reversed)
    return(layering7)

if __name__ == '__main__':
    try:

        main()
    except (KeyboardInterrupt,Exception) as e:
        print(e)