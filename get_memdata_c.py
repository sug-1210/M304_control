#! /usr/bin/env python3
import requests
import struct
from bs4 import BeautifulSoup

class Block_C:
    def __init__(self, valid, room, region, order, priority, lv, cast, sr, ccm_type, unit, sthr, stmn, edhr, edmn, inmn, dumn, rly_l, rly_h, alignment, dummy):
        self.valid = valid
        self.room = room
        self.region = region
        self.order = order
        self.priority = priority
        self.lv = lv
        self.cast = cast
        self.sr = sr
        self.ccm_type = ccm_type
        self.unit = unit
        self.sthr = sthr
        self.stmn = stmn
        self.edhr = edhr
        self.edmn = edmn
        self.inmn = inmn
        self.dumn = dumn
        self.rly_l = rly_l
        self.rly_h = rly_h
        self.alignment = alignment
        self.dummy = dummy

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

        lv = priority[1].split(' ', 1)
        #data_1.lv = int(lv[0], 16)

        cast = lv[1].split(' ', 1)
        #data_1.cast = int(cast[0], 16)

        sr = cast[1].split(' ', 1)
        #data_1.sr = chr(int(sr[0], 16))

        ccm_type = sr[1].split(' ', 20)
        ccm_tmp = ''
        for i in range(20):
            ccm_tmp += chr(int(ccm_type[i], 16))
        #data_1.ccm_type = ccm_tmp

        unit = ccm_type[20].split(' ', 10)
        unit_tmp = ''
        for i in range(10):
            unit_tmp += chr(int(unit[i], 16))
        #data_1.unit = unit_tmp

        sthr = unit[10].split(' ', 1)
        #data_1.sthr = int(sthr[0], 16)

        stmn = sthr[1].split(' ', 1)
        #data_1.stmn = int(stmn[0], 16)

        edhr = stmn[1].split(' ', 1)
        #data_1.edhr = int(edhr[0], 16)

        edmn = edhr[1].split(' ', 1)
        #daat_1.edmn = int(edmn[0], 16)

        inmn = edmn[1].split(' ', 1)
        #data_1.inmn = int(inmn[0], 16)

        dumn = inmn[1].split(' ', 1)
        #data_1.dumn = int(dumn[0], 16)

        rly_l = dumn[1].split(' ', 1)
        #data_1.rly_l = int(rly_l[0], 16)

        rly_h = rly_l[1].split(' ', 1)
        #data_1.rly_h = int(rly_h[0], 16)

        alignment = rly_h[1].split(' ', 1)
        #data_1.alignment = alignment[0]

        dummy = alignment[1].split(' ', 16)
        dummy_tmp = ''
        for i in range(16):
            dummy_tmp += dummy[i]
        #data_1.dummy = dummy_tmp
        data_1 = Block_C(valid[0], int(room[0], 16), int(region[0], 16), int(order[1]+order[0], 16), int(priority[0], 16), int(lv[0], 16), int(cast[0], 16), chr(int(sr[0], 16)), ccm_tmp, unit_tmp, int(sthr[0], 16), int(stmn[0], 16), int(edhr[0], 16), int(edmn[0], 16), int(inmn[0], 16), int(dumn[0], 16), int(rly_l[0], 16), int(rly_h[0], 16), alignment[0], dummy_tmp)
        return data_1
        break


test_data = '01 02 03 01 00 11 05 06 52 54 65 73 74 44 61 74 61 00 00 00 00 00 00 00 00 00 00 00 00 25 25 25 25 25 25 25 25 25 25 01 35 17 3b 10 25 ff f0 00 aa bb cc dd ee ff gg hh ii jj kk ll mm nn oo pp'
test = get_mem_data(test_data)
print(f'valid:{test.valid}, room:{test.room}, region:{test.region}, order:{test.order}, priority:{test.priority}, lv:{test.lv}, cast:{test.cast}, sr:{test.sr}, ccm_type:{test.ccm_type}, unit:{test.unit}, sthr:{test.sthr}, stmn:{test.stmn}, edhr:{test.edhr}, edmn:{test.edmn}, inmn:{test.inmn}, dumn:{test.dumn}, rly_l:{test.rly_l}, rly_h:{test.rly_h}, alignment:{test.alignment}, dummy:{test.dummy}')