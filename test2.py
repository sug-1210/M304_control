import test1
def ascii_intelhex(x): #x : レコードタイプ 0or1
    if x == 0: #data_type->00
        data = test1.text_binary()
        intel_hex = ":"
        if data[1] <= 15: #0x1など表示を01と格納できるように処理
            intel_hex = intel_hex + "0" + hex(data[1]).replace("0x", "")
        else:
            intel_hex = intel_hex + hex(data[1]).replace("0x", "")
        print(intel_hex)
        intel_hex = intel_hex + "0000" #オフセットアドレス　一旦0000
        intel_hex = intel_hex + "00" #レコードタイプ
        intel_hex = intel_hex + data[0]
        intel_hex = intel_hex + "00" #チェックサムは使用しないため00
        print(intel_hex)

    else: #data_type->01
        intel_hex = ":00000001FF" #チェックサム部分は要変更
    result = [intel_hex, data[0], data[1]]
    return result

def intel_hex_reverse(x): #リトルエンディアンに対応させる
    intel_hex = ascii_intelhex(x)[0]
    length = ascii_intelhex(x)[2]
    intel_hex = intel_hex.replace(":", "")
    length = 5 + length #チェックサムないから一旦4、本当は5
    i = 0
    result = []
    result = list() #リスト初期化
    while i < length:
        result.append(intel_hex[2*i:2*i+2]) #2文字ずつリストに追加
        i = i + 1
    result.reverse() #リストを反転させリトルエンディアンに対応
    for num in range(length):
        print(result[num])
    return result


print(ascii_intelhex(0)[0])
print(intel_hex_reverse(0)[0])
