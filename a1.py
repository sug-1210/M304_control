#! /usr/bin/env python3
#coding: utf-8
#

# arguments are as following
#  id room region order priority ccm_type cmope fval

import sys
import struct

LC_CMPOPE_START    = 0x5000
LC_CMPOPE_REC_SIZE = 0x20

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
    return rt


##########################################################
if __name__ == '__main__':
    args = sys.argv

    id = int(args[1])
    room = int(args[2])
    region = int(args[3])
    order = int(args[4])
    priority = int(args[5])
    ccmtype = args[6]
    cmope = int(args[7])
    fval = float(args[8])
    addr  = hex(id*LC_CMPOPE_REC_SIZE+LC_CMPOPE_START).replace('0x','').rjust(4,'0')

    ih_valid    = byte_arrange(1)
    ih_room     = byte_arrange(room)
    ih_region   = byte_arrange(region)
    order_o     = hex(order).replace('0x','').rjust(4,'0')
    ih_order    = order_o[2:4]+order_o[0:2]
    ih_priority = byte_arrange(priority)
    ih_ccmtype  = string_arrange(ccmtype,20)
    ih_cmope    = byte_arrange(cmope)
    ih_fval     = hex(struct.unpack('>I',struct.pack('>f',fval))[0]).replace('0x','')
    ihtxt       = ih_valid+ih_room+ih_region+ih_order+ih_priority+ih_ccmtype+ih_cmope+ih_fval
    sz          = hex(int(len(ihtxt)/2)).replace('0x','').rjust(2,'0')
    
    ih =":"+sz+addr+"00"+ihtxt+"FF"

    print(ih)
    
