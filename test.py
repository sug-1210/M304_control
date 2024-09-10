import struct
import binascii
from dataclasses import dataclass

@dataclass
class Data:
    ascii_data: str
    data_size: int
    address: str

def test_hex(x): #x : 文字(1字)　入力文字をascii(16進数)に変換
    ascii_code = ord(x)
    if ascii_code <= 15:
        ascii_code = "0" + hex(ascii_code).replace("0x", "")
    else:
        ascii_code = hex(ascii_code).replace("0x", "")
    return ascii_code

def int_hex(x): #intを16進数の文字列へ変換
    ascii_code = hex(x)
    ascii_code = ascii_code.replace("0x", "")
    return ascii_code

def string_binary(data, address): #dataをasciiに変換しintel hex formatで出力
    ascii_codes = [test_hex(char) for char in data] #asciiコードのリストを作成
    i = 0
    ascii_data = ""
    if len(ascii_codes) > 16: #16バイト以下か判断
        print("Error:Data length is over. Data length is less than 16 byte\n")
        return ascii_data
    while i < len(ascii_codes): #文字列に変換
        ascii_data = ascii_data + ascii_codes[i] #リストの各要素を結合させ文字列に変換
        i = i + 1
    intel_hex = ""
    intel_hex = intel_hex + ascii_data
    data1 = Data(intel_hex, len(ascii_codes)/2, address)
    return data1

#int
def int_binary(data, address):
    data = int_hex(data)
    ascii_codes = [test_hex(char) for char in data] #asciiコードのリストを作成
    i = 0
    ascii_data = ""
    if len(ascii_codes) > 16: #16バイト以下か判断
        print("Error:Data length is over. Data length is less than 16 byte\n")
        return ascii_data
    while i < len(ascii_codes): #文字列に変換
        ascii_data = ascii_data + ascii_codes[i] #リストの各要素を結合させ文字列に変換
        i = i + 1
    intel_hex = ""
    intel_hex = intel_hex + ascii_data
    data1 = Data(intel_hex, len(ascii_codes)/2, address)
    return data1

def int_bin2(data, address):
    if data < 16:
        intel_hex = "0" + hex(data).replace("0x", "")
    else:
        intel_hex = hex(data).replace("0x", "")
    data1 = Data(intel_hex, len(intel_hex)/2, address)
    return data1

#IEEEの単精度浮動小数
def float_binary(data, address):
    intel_hex = hex(struct.unpack('>I',struct.pack('>f',data))[0]).replace("0x","")
    data1 = Data(intel_hex, len(intel_hex)/2, address)
    return data1


print(string_binary("abcdefg","0x5000").ascii_data)
print(int_binary(123,"0x5000").ascii_data)
print(float_binary(1.23,"0x5000").ascii_data)