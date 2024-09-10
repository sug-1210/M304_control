def test_hex(x): #x : 文字(1字)　入力文字をascii(16進数)に変換
    ascii_code = ord(x)
    if ascii_code <= 15:
        ascii_code = "0" + hex(ascii_code).replace("0x", "")
    else:
        ascii_code = hex(ascii_code).replace("0x", "")
    return ascii_code

def float_hex(x): #float(またはint)を16進数の文字列へ変換
    ascii_code = hex(x)
    ascii_code = ascii_code.replace("0x", "")
    return ascii_code

#data -> str or float(int), address -> str 0x----, rec_type -> 0 or 1
def string_binary(data, address, rec_type): #dataをasciiに変換しintel hex formatで出力
    print(data) #dataの表示
    if rec_type == 0: #レコードタイプ->00
        if (type(data) == float) or (type(data) == int): #dataの型を判定
            data = float_hex(data)
        ascii_codes = [test_hex(char) for char in data] #asciiコードのリストを作成
        i = 0
        ascii_data = ""
        if len(ascii_codes) > 16: #16バイト以下か判断
            print("Error:Data length is over. Data length is less than 16 byte\n")
            return ascii_data
        while i < len(ascii_codes): #文字列に変換
            ascii_data = ascii_data + ascii_codes[i] #リストの各要素を結合させ文字列に変換
            i = i + 1
        intel_hex = ":"
        if len(ascii_codes) <= 15: #0x1など表示を01と格納できるように処理
            intel_hex = intel_hex + "0" + hex(len(ascii_codes)).replace("0x", "")
        else:
            intel_hex = intel_hex + hex(len(ascii_codes)).replace("0x", "")
        intel_hex = intel_hex + address.replace("0x", "") #オフセットアドレス
        intel_hex = intel_hex + "00" #レコードタイプ
        intel_hex = intel_hex + ascii_data
        intel_hex = intel_hex + "00" #チェックサムは使用しないため00
    else: #レコードタイプ->01
        intel_hex = ":00" + address.replace("0x", "") + "0100"
    return intel_hex

print(string_binary("123", "0x5000", 0))


def int_binary(data, address, rec_type):
    print(data) #dataの表示
    if rec_type == 0: #レコードタイプ->00
        if (type(data) == float) or (type(data) == int): #dataの型を判定
            data = float_hex(data)
        ascii_codes = [test_hex(char) for char in data] #asciiコードのリストを作成
        i = 0
        ascii_data = ""
        if len(ascii_codes) > 16: #16バイト以下か判断
            print("Error:Data length is over. Data length is less than 16 byte\n")
            return ascii_data
        while i < len(ascii_codes): #文字列に変換
            ascii_data = ascii_data + ascii_codes[i] #リストの各要素を結合させ文字列に変換
            i = i + 1
        intel_hex = ":"
        if len(ascii_codes) <= 15: #0x1など表示を01と格納できるように処理
            intel_hex = intel_hex + "0" + hex(len(ascii_codes)).replace("0x", "")
        else:
            intel_hex = intel_hex + hex(len(ascii_codes)).replace("0x", "")
        intel_hex = intel_hex + address.replace("0x", "") #オフセットアドレス
        intel_hex = intel_hex + "00" #レコードタイプ
        intel_hex = intel_hex + ascii_data
        intel_hex = intel_hex + "00" #チェックサムは使用しないため00
    else: #レコードタイプ->01
        intel_hex = ":00" + address.replace("0x", "") + "0100"
    return intel_hex