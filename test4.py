#from fastapi import FastAPI, Form
import struct
import requests

#app = FastAPI()

#@app.post("/test/")
def test_A(LC_UECS_ID,
                LC_MAC,
                FIX_DHCP_FLAG,
                FIXED_IPADDRESS,
                FIXED_NETMASK,
                FIXED_DEFGW,
                FIXED_DNS,
                VENDER_NAME,
                NODE_NAME):
    address = 0x0000
    ih_uecs_id = LC_UECS_ID.rjust(12, '0')
    ih_mac = LC_MAC.replace(':', '')
    ih_dhcpflg = byte_arrange(FIX_DHCP_FLAG)
    sp_ip_addr = FIXED_IPADDRESS.split('.')
    ih_ip_addr = ""
    for ip in sp_ip_addr:
        ih_ip_addr += byte_arrange(int(ip))
    sp_netmask = FIXED_NETMASK.split('.')
    ih_netmask = ""
    for netmask in sp_netmask:
        ih_netmask += byte_arrange(int(netmask))
    sp_defgw = FIXED_DEFGW.split('.')
    ih_defgw = ""
    for defgw in sp_defgw:
        ih_defgw += byte_arrange(int(defgw))
    sp_dns = FIXED_DNS.split('.')
    ih_dns = ""
    for dns in sp_dns:
        ih_dns += byte_arrange(int(dns))
    ih_vender_name = string_arrange(VENDER_NAME, 16)
    ih_node_name = string_arrange(NODE_NAME, 16)
    ihtxt = ih_uecs_id + ih_mac + ih_dhcpflg + ih_ip_addr + ih_netmask + ih_defgw + ih_dns + ih_vender_name + ih_node_name
    for i in range(4):
        tp = i*32
        iht = ihtxt[tp:(tp+32)]
        sz = hex(int(len(iht)/2)).replace('0x', '').rjust(2,'0')
        addr = hex(address+int(tp/2)).replace('0x', '').rjust(4, '0')
        ih = ":" + sz + addr + "00" + iht + "FF"
        #送信処理
        print(ih)
        print("\n")
    return 0

def test_B(B_ID,
                IP_ADDR,
                LC_VALID,
                LC_ROOM,
                LC_REGION,
                LC_ORDER,
                LC_PRIORITY,
                LC_LV,
                LC_CAST,
                LC_SR,
                LC_CCMTYPE,
                LC_UNIT,
                LC_STHR,
                LC_STMN,
                LC_EDHR,
                LC_EDMN,
                LC_INMN,
                LC_DUMN,
                LC_RLY_L,
                LC_RLY_H):
    address = 0x1000
    recstep = 0x40
    ih_valid = byte_arrange(1)
    ih_room = byte_arrange(LC_ROOM)
    ih_region = byte_arrange(LC_REGION)
    order_o = hex(LC_ORDER).replace('0x', '').rjust(4, '0')
    ih_order = order_o[2:4]+order_o[0:2]
    ih_priority = byte_arrange(LC_PRIORITY)
    ih_lv = byte_arrange(LC_LV)
    ih_cast = byte_arrange(LC_CAST)
    ih_sr = "52"
    ih_ccmtype = string_arrange(LC_CCMTYPE, 20)
    ih_unit = string_arrange(LC_UNIT, 10)
    ih_sthr = byte_arrange(LC_STHR)
    ih_stmn = byte_arrange(LC_STMN)
    ih_edhr = byte_arrange(LC_EDHR)
    ih_edmn = byte_arrange(LC_EDMN)
    ih_inmn = byte_arrange(LC_INMN)
    ih_dumn = byte_arrange(LC_DUMN)
    ih_rly_l = byte_arrange(LC_RLY_L)
    ih_rly_h = byte_arrange(LC_RLY_H)
    ihtxt = ih_valid+ih_room+ih_region+ih_order+ih_priority+ih_lv+ih_cast+ih_sr+ih_ccmtype+ih_unit+ih_sthr+ih_stmn+ih_edhr+ih_edmn+ih_inmn+ih_dumn+ih_rly_l+ih_rly_h
    for i in range(3):
        tp = i*32
        iht = ihtxt[tp:(tp+32)]
        sz = hex(int(len(iht)/2)).replace('0x', '').rjust(2,'0')
        addr = hex(B_ID*recstep+address+int(tp/2)).replace('0x', '').rjust(4, '0')
        ih = ":" + sz + addr + "00" + iht + "FF"
        #送信処理
        url = "http://" + IP_ADDR + "/" + ih
        requests.get(url)
        print(ih)
        print("\n")
    return 0

def test_C(C_ID,
                IP_ADDR,
                LC_VALID,
                LC_ROOM,
                LC_REGION,
                LC_ORDER,
                LC_PRIORITY,
                LC_LV,
                LC_CAST,
                LC_SR,
                LC_CCMTYPE,
                LC_UNIT,
                LC_STHR,
                LC_STMN,
                LC_EDHR,
                LC_EDMN,
                LC_INMN,
                LC_DUMN,
                LC_RLY_L,
                LC_RLY_H):
    address = 0x3000
    recstep = 0x40
    ih_valid = byte_arrange(1)
    ih_room = byte_arrange(LC_ROOM)
    ih_region = byte_arrange(LC_REGION)
    order_o = hex(LC_ORDER).replace('0x', '').rjust(4, '0')
    ih_order = order_o[2:4]+order_o[0:2]
    ih_priority = byte_arrange(LC_PRIORITY)
    ih_lv = byte_arrange(LC_LV)
    ih_cast = byte_arrange(LC_CAST)
    ih_sr = "53"
    ih_ccmtype = string_arrange(LC_CCMTYPE, 20)
    ih_unit = string_arrange(LC_UNIT, 10)
    ih_sthr = byte_arrange(LC_STHR)
    ih_stmn = byte_arrange(LC_STMN)
    ih_edhr = byte_arrange(LC_EDHR)
    ih_edmn = byte_arrange(LC_EDMN)
    ih_inmn = byte_arrange(LC_INMN)
    ih_dumn = byte_arrange(LC_DUMN)
    ih_rly_l = byte_arrange(LC_RLY_L)
    ih_rly_h = byte_arrange(LC_RLY_H)
    ihtxt = ih_valid+ih_room+ih_region+ih_order+ih_priority+ih_lv+ih_cast+ih_sr+ih_ccmtype+ih_unit+ih_sthr+ih_stmn+ih_edhr+ih_edmn+ih_inmn+ih_dumn+ih_rly_l+ih_rly_h
    for i in range(3):
        tp = i*32
        iht = ihtxt[tp:(tp+32)]
        sz = hex(int(len(iht)/2)).replace('0x', '').rjust(2,'0')
        addr = hex(C_ID*recstep+address+int(tp/2)).replace('0x', '').rjust(4, '0')
        ih = ":" + sz + addr + "00" + iht + "FF"
        #送信処理
        url = "http://" + IP_ADDR + "/" + ih
        requests.get(url)
        print(ih)
        print("\n")
    return 0

def test_D(D_ID,
                IP_ADDR,
                LC_COPE_VALID,
                LC_COPE_ROOM,
                LC_COPE_REGION,
                LC_COPE_ORDER,
                LC_COPE_PRIORITY,
                LC_COPE_CCMTYPE,
                LC_COPE_OPE,
                LC_COPE_FVAL):
    address = 0x5000
    recstep = 0x20
    ih_cope_valid = byte_arrange(LC_COPE_VALID)
    ih_cope_room = byte_arrange(LC_COPE_ROOM)
    ih_cope_region = byte_arrange(LC_COPE_REGION)
    cope_order_o = hex(LC_COPE_ORDER).replace('0x', '').rjust(4, '0')
    ih_cope_order = cope_order_o[2:4] + cope_order_o[0:2]
    ih_cope_priority = byte_arrange(LC_COPE_PRIORITY)
    ih_cope_ccmtype = string_arrange(LC_COPE_CCMTYPE, 20)
    ih_cope_ope = byte_arrange(LC_COPE_OPE)
    ih_cope_fval = float_binary(LC_COPE_FVAL) #エンディアン?
    ihtxt = ih_cope_valid + ih_cope_room + ih_cope_region + ih_cope_order + ih_cope_priority + ih_cope_ccmtype + ih_cope_ope + ih_cope_fval
    for i in range(2):
        tp = i*32
        iht = ihtxt[tp:(tp+32)]
        sz = hex(int(len(iht)/2)).replace('0x', '').rjust(2,'0')
        addr = hex(D_ID*recstep+address+int(tp/2)).replace('0x', '').rjust(4, '0')
        ih = ":" + sz + addr + "00" + iht + "FF"
        url = "http://" + IP_ADDR + "/" + ih
        requests.get(url)
        print(ih)
        print("\n")
    return 0


#IEEEの単精度浮動小数
def float_binary(data):
    bin_data = hex(struct.unpack('>I',struct.pack('>f',data))[0]).replace("0x","")
    return bin_data

def byte_arrange(b):
    y = hex(b).replace('0x','').rjust(2,'0')
    return y

def string_arrange(s,l):
    rt = ""
    cnt= 0
    for c in s:
        if cnt>=l:
            return rt
        b = hex(ord(c)).replace('0x','').rjust(2,'0')
        rt += b
        cnt += 1
    while cnt < l:
        rt += "00"
        cnt += 1
    return rt


# def test_hex(x): #x : 文字(1字)　入力文字をascii(16進数)に変換
    # ascii_code = ord(x)
    # if ascii_code <= 15:
        # ascii_code = "0" + hex(ascii_code).replace("0x", "")
    # else:
        # ascii_code = hex(ascii_code).replace("0x", "")
    # return ascii_code

# def string_binary(data, x): #dataをasciiに変換しintel hex formatで出力
    # ascii_codes = [test_hex(char) for char in data] #asciiコードのリストを作成
    # i = 0
    # ascii_data = ""
    # while i < len(ascii_codes): #文字列に変換
        # ascii_data = ascii_data + ascii_codes[i] #リストの各要素を結合させ文字列に変換
        # i = i + 1
    # ascii_data = ascii_data.rjust(x, '0')
    # return ascii_data

# def int_bin(data, x):
    # bin_data = hex(data).replace("0x", "").rjust(x, '0')
    # return bin_data

#intel_hexへの変換
# def bin_intelhex(bin_data, address):
    # intel_hex = ":"
    # address = str(address).replace("0x", "").rjust(4, '0')
    # intel_hex = intel_hex + hex(len(bin_data)/2).replace("0x", "").rjust(2, '0') + address + "00" + bin_data + "FF"
    # return intel_hex

if __name__ == '__main__':
    print("A\n")
    test_A("10100C00000B", "02:A2:73:0B:00:2A", 0, "192.168.38.50", "255.255.255.0", "192.168.11.1", "192.168.11.1", "AMPSD", "TESTA123")
    print("B\n")
    test_B(0, "192.168.1.14", 1, 1, 1, 1, 15, 3, 0, 0, "InAirHumid", "%", 0, 0, 23, 59, 1, 1, 252, 0)
    test_B(1, "192.168.1.14", 1, 1, 1, 1, 15, 3, 0, 0, "InAirHumid", "%", 0, 0, 23, 59, 1, 1, 0, 255)
    print("C\n")
    test_C(0, "192.168.1.14", 1, 1, 1, 1, 15, 3, 0, 0, "TEST456", "", 0, 0, 23, 59, 1, 1, 252, 0)
    test_C(1, "192.168.1.14", 1, 1, 1, 1, 15, 3, 0, 0, "TEST789", "", 0, 0, 12, 00, 1, 1, 0, 255)
    print("D\n")
    test_D(0, "192.168.1.14", 1, 1, 1, 1, 15, "InAirHumid", 3, 50) 