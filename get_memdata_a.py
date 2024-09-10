#! /usr/bin/env python3
import requests
import struct
from bs4 import BeautifulSoup

class Block_A:
    def __init__(self, uecsid, macaddr, fix_dhcp_flag, fixed_ipaddress, fixed_netmask, fixed_defgw, fixed_dns, vender_name, node_name):
        self.uecsid = uecsid
        self.macaddr = macaddr
        self.fix_dhcp_flag = fix_dhcp_flag
        self.fixed_ipaddress = fixed_ipaddress
        self.fixed_netmask = fixed_netmask
        self.fixed_defgw = fixed_defgw
        self.fixed_dns = fixed_dns
        self.vender_name = vender_name
        self.node_name = node_name

def get_mem_data(data):
    #url = "http://192.168.1.14/L00100000"
    #data = requests.get(url)
    #soup = BeautifulSoup(data.content, 'html.parser')
    #pre_text = soup.find('pre').get_text()
    pre_text = data #test用
    pre_text = pre_text.replace('\n', '') #改行の削除
    pre_text = pre_text.replace('\r\n', '')
    while(True):
        uecsid = pre_text.split(' ', 6)
        uecsid_tmp = ''
        for i in range(6):
            uecsid_tmp += uecsid[i]
        #data_1.uecsid = uecsid[0]

        macaddr = uecsid[6].split(' ', 6)
        macaddr_tmp = ''
        for i in range(6):
            macaddr_tmp += macaddr[i]
            if i < 5:
                macaddr_tmp += ':'
        #data_1.macaddr = int(macaddr[0], 16)

        fix_dhcp_flag = macaddr[6].split(' ', 1)
        #data_1.fix_dhcp_flag = int(fix_dhcp_flag[0], 16)

        fixed_ipaddress = fix_dhcp_flag[1].split(' ', 4)
        fixed_ipaddress_tmp = ''
        for i in range(4):
            fixed_ipaddress_tmp += str(int(fixed_ipaddress[i], 16))
            if i < 3:
                fixed_ipaddress_tmp += '.'

        fixed_netmask = fixed_ipaddress[4].split(' ', 4)
        fixed_netmask_tmp = ''
        for i in range(4):
            fixed_netmask_tmp += str(int(fixed_netmask[i], 16))
            if i < 3:
                fixed_netmask_tmp += '.'
        #data_1.fixed_netmask = int(fixed_netmask[0], 16)

        fixed_defgw = fixed_netmask[4].split(' ', 4)
        fixed_defgw_tmp = ''
        for i in range(4):
            fixed_defgw_tmp += str(int(fixed_defgw[i], 16))
            if i < 3:
                fixed_defgw_tmp += '.'
        #data_1.fixed_defgw = int(fixed_defgw[0], 16)

        fixed_dns = fixed_defgw[4].split(' ', 4)
        fixed_dns_tmp = ''
        for i in range(4):
            fixed_dns_tmp += str(int(fixed_dns[i], 16))
            if i < 3:
                fixed_dns_tmp += '.'
        #data_1.fixed_dns = int(fixed_dns[0], 16)

        vender_name = fixed_dns[4].split(' ', 16)
        vender_name_tmp = ''
        for i in range(16):
            vender_name_tmp += chr(int(vender_name[i], 16))
        #data_1.vender_name = chr(int(vender_name[0], 16))

        node_name = vender_name[16].split(' ', 16)
        node_name_tmp = ''
        for i in range(16):
            node_name_tmp += chr(int(node_name[i], 16))
        #data_1.node_name = ccm_tmp

        data_1 = Block_A(uecsid_tmp, macaddr_tmp, fix_dhcp_flag[0], fixed_ipaddress_tmp, fixed_netmask_tmp, fixed_defgw_tmp, fixed_dns_tmp, vender_name_tmp, node_name_tmp)
        return data_1
        break


test_data = '01 10 0C 00 00 0B 02 a2 73 00 00 00 00 c0 a8 01 01 ff ff 01 01 0a 14 8f fe 85 05 06 01 41 42 43 44 41 42 43 44 41 42 43 44 41 42 43 44 45 46 47 48 45 46 47 48 45 46 47 48 45 46 47 48'
test = get_mem_data(test_data)
print(f'uecsid:{test.uecsid}, macaddr:{test.macaddr}, fix_dhcp_flag:{test.fix_dhcp_flag}, fixed_ipaddress:{test.fixed_ipaddress}, fixed_netmask:{test.fixed_netmask}, fixed_defgw:{test.fixed_defgw}, fixed_dns:{test.fixed_dns}, vender_name:{test.vender_name}, node_name:{test.node_name}')