import test



def join_data(data1, data2):
    data = data1.ascii_data + data2.ascii_data
    data_length = data1.data_size + data2.data_size
    data3 = test.Data(data, data_length, data1.address)
    return data3

def make_intelhex(data):
    intelhex = ":"
    if data.data_length <= 15: #0x1など表示を01と格納できるように処理
        intelhex = intelhex + "0" + hex(data.data_length).replace("0x", "")
    else:
        intelhex = intelhex + hex(data.data_length).replace("0x", "")
    intelhex = intelhex + data.address + "00" + data.ascii_data + "00"
    return intelhex

data = join_data(test.string_binary("abcdef", "0x1000"), test.float_binary(1.23, "0x5000"))
print(data.ascii_data)

def int_binary2(data, address):
    if type(data) != int:
        print("Error:Non integer data\n")
        return 0
    intel_hex = hex(test.struct.unpack('>I',test.struct.pack('>f',data))[0]).replace("0x","")
    data1 = test.Data(intel_hex, len(intel_hex)/2, address)
    return data1