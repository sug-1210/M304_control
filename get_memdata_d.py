#! /usr/bin/env python3
import requests
import struct
from bs4 import BeautifulSoup

class Block_D:
    def __init__(self, valid, room, region, order, priority, ccm_type, cmpope, fval, last):
        self.valid = valid
        self.room = room
        self.region = region
        self.order = order
        self.priority = priority
        self.ccm_type = ccm_type
        self.cmpope = cmpope
        self.fval = fval
        self.last = last

def get_mem_data(data):
    #url = "http://192.168.1.14/L00100000"
    #data = requests.get(url)
    #soup = BeautifulSoup(data.content, 'html.parser')
    #pre_text = soup.find('pre').get_text()
    pre_text = data #test用
    pre_text = pre_text.replace('\n', '') #改行の削除
    pre_text = pre_text.replace('\r\n', '')
    while(True):
        valid = pre_text.split(' ', 1)
        #data_1.valid = valid[0]

        room = valid[1].split(' ', 1)
        #data_1.room = int(room[0], 16)

        region = room[1].split(' ', 1)
        #data_1.region = int(region[0], 16)

        order = region[1].split(' ', 2)
        #data_1.order = int(order[0]+order[1], 16)

        priority = order[2].split(' ', 1)
        #data_1.priority = int(priority[0], 16)

        ccm_type = priority[1].split(' ', 20)
        ccm_tmp = ''
        for i in range(20):
            ccm_tmp += chr(int(ccm_type[i], 16))
        #data_1.ccm_type = ccm_tmp

        cmpope = ccm_type[20].split(' ', 1)
        #data_1.cmpope = int(cmpope[0], 16)

        fval = cmpope[1].split(' ', 4)
        #IEEE形式単精度浮動小数点の処理

        last = fval[4].split(' ', 1)
        #data_1.last = int(edhr[0], 16)

        data_1 = Block_D(valid[0], int(room[0], 16), int(region[0], 16), int(order[1]+order[0], 16), int(priority[0], 16), ccm_tmp, int(cmpope[0], 16), fval, last[0])
        return data_1
        break

test_data = ''
test = get_mem_data(test_data)
print(f'valid:{test.valid}, room:{test.room}, region:{test.region}, order:{test.order}, priority:{test.priority}, ccm_type:{test.ccm_type}, cmpope:{test.cmpope}, fval:{test.fval}, LAST:{test.last}')