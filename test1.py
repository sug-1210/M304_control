def test_hex(x): #x : 文字(1字)　入力文字をascii(16進数)に変換
    ascii_code = ord(x)
    if ascii_code <= 15:
        ascii_code = "0" + hex(ascii_code).replace("0x", "")
    else:
        ascii_code = hex(ascii_code).replace("0x", "")
    return ascii_code

def text_binary(): #入力文字列をasciiに変換
    x = input() #入力
    print(x)
    ascii_codes = [test_hex(char) for char in x] #ascii
    i = 0
    data = ["", len(ascii_codes)]
    if data[1] > 16: #16バイト以下か判断
        print("Error:Data length is over. Data length is less than 16 byte\n")
        return data
    while i < len(ascii_codes): #文字列に変換
        data[0] = data[0] + ascii_codes[i]
        i = i + 1
    return data



#おそらく間違っている方
def text_binary_reverse(): #入力文字列をasciiに変換
    x = input() #入力
    print(x)
    ascii_codes = [test_hex(char) for char in x] #ascii
    i = 0
    ascii_codes.reverse() #リストの反転 リトルエンディアンに
    data = ["", len(ascii_codes)]
    if data[1] > 16:
        print("Error:Data length is over. Data length is less than 16 byte\n")
        return
    while i < len(ascii_codes):
        data[0] = data[0] + ascii_codes[i]
        i = i + 1
        print(data[0])
    return data

a = text_binary()
print(a[0])
print(a[1])