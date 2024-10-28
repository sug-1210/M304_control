package main

import (
	"fmt"
	"math"
	"net/http"

	// "net/http"
	"strconv"
	"strings"
)

const (
	addressBaseBlockA    = 0x0000
	addressBaseBlockB    = 0x1000
	addressBaseBlockC    = 0x3000
	addressBaseBlockD    = 0x5000
	recordStepBlockBC    = 0x40
	recordStepBlockD     = 0x20
	blockSize            = 32
	responseCountBlockA  = 4
	responseCountBlockBC = 3
	responseCountBlockD  = 2
)

// 文字列を指定長に変換する(右埋め)
// s: 元の文字列, out_len: 出力文字列長, padchar: paddingに使う文字
func Padding(s string, out_len int, padchar string) string {
	padding := out_len - len(s)
	if padding > 0 {
		return strings.Repeat(padchar, padding) + s
	} else {
		return s
	}
}

// 整数を2桁16進数の文字列に変換する
func ByteArrange(n int) string {
	hexstr := fmt.Sprintf("%x", n)
	value := Padding(hexstr, 2, "0")
	return value
}

// 文字列を指定長の2桁16進数asciiコードの文字列に変換する
func StringArrange(s string, length int) string {
	rt := ""
	for _, r := range s {
		rt += Padding(fmt.Sprintf("%x", r), 2, "0")
	}
	for len(rt) < length {
		rt += "0"
	}
	return rt
}

// 32bit浮動小数点数を16進数に変換
func Float32Bin(f float32) string {
	bin := math.Float32bits(f)
	hexstr := fmt.Sprintf("%08x", bin)
	return hexstr
}

type BlockA struct {
	IpAddr         string
	LcUecsID       string
	LcMac          string
	FixDhcpFlag    int
	FixedIpAddress string
	FixedNetMask   string
	FixedDefGw     string
	FixedDns       string
	VenderName     string
	NodeName       string
}

func SendBlockA(blockAData BlockA) ([]*http.Response, error) {
	address := addressBaseBlockA
	ih_uecs_id := Padding(blockAData.LcUecsID, 12, "0")
	ih_mac := strings.Replace(blockAData.LcMac, ":", "", -1)
	ih_dhcpflg := ByteArrange(blockAData.FixDhcpFlag)
	ih_non := Padding("", 6, "0")
	sp_ip_addr := strings.Split(blockAData.FixedIpAddress, ".")
	ih_ip_addr := ""
	for _, v := range sp_ip_addr {
		addrInt, err := strconv.Atoi(v)
		if err != nil {
			return nil, err
		}
		ih_ip_addr += ByteArrange(addrInt)
	}

	sp_netmask := strings.Split(blockAData.FixedNetMask, ".")
	ih_netmask := ""
	for _, v := range sp_netmask {
		netmaskInt, err := strconv.Atoi(v)
		if err != nil {
			return nil, err
		}
		ih_netmask += ByteArrange(netmaskInt)
	}

	sp_defgw := strings.Split(blockAData.FixedDefGw, ".")
	ih_defgw := ""
	for _, v := range sp_defgw {
		defgwInt, err := strconv.Atoi(v)
		if err != nil {
			return nil, err
		}
		ih_defgw += ByteArrange(defgwInt)
	}

	sp_dns := strings.Split(blockAData.FixedDns, ".")
	ih_dns := ""
	for _, v := range sp_dns {
		dnsInt, err := strconv.Atoi(v)
		if err != nil {
			return nil, err
		}
		ih_dns += ByteArrange(dnsInt)
	}

	ih_vender_name := StringArrange(blockAData.VenderName, 32)
	ih_node_name := StringArrange(blockAData.NodeName, 32)

	ihtxt := ih_uecs_id + ih_mac + ih_dhcpflg + ih_non + ih_ip_addr + ih_netmask + ih_defgw + ih_dns + ih_vender_name + ih_node_name
	resps := make([]*http.Response, responseCountBlockA)
	for i := 0; i < responseCountBlockA; i++ {
		tp := i * blockSize
		iht := ""
		if len(ihtxt) < tp+blockSize {
			iht = ihtxt[tp:]
		} else {
			iht = ihtxt[tp:(tp + blockSize)]
		}
		sz := Padding(fmt.Sprintf("%x", len(iht)/2), 2, "0")
		addr := Padding(fmt.Sprintf("%x", address+(tp/2)), 4, "0")
		ih := ":" + sz + addr + "00" + iht + "FF"
		// 送信処理
		url := "http://" + blockAData.IpAddr + "/" + ih
		// fmt.Println(url)
		resp, err := http.Get(url)
		if err != nil {
			resps[i] = nil
			return resps, err
		}
		resps[i] = resp
		resp.Body.Close()
	}
	return resps, nil
}

type BlockB struct {
	BID        int
	IpAddr     string
	LcValid    int
	LcRoom     int
	LcRegion   int
	LcOrder    int
	LcPriority int
	LcLv       int
	LcCast     int
	LcSr       string
	LcCcmType  string
	LcUnit     string
	LcStHr     int
	LcStMn     int
	LcEdHr     int
	LcEdMn     int
	LcInMn     int
	LcDuMn     int
	LcRlyL     int
	LcRlyH     int
}

func SendBlockB(blockBData BlockB) ([]*http.Response, error) {
	address := addressBaseBlockB
	recstep := recordStepBlockBC
	ih_valid := ByteArrange(blockBData.LcValid)
	ih_room := ByteArrange(blockBData.LcRoom)
	ih_region := ByteArrange(blockBData.LcRegion)
	order_o := Padding(fmt.Sprintf("%x", blockBData.LcOrder), 4, "0")
	ih_order := order_o[2:4] + order_o[0:2]
	ih_priority := ByteArrange(blockBData.LcPriority)
	ih_lv := ByteArrange(blockBData.LcLv)
	ih_cast := ByteArrange(blockBData.LcCast)
	ih_sr := StringArrange(blockBData.LcSr, 2)
	ih_ccmtype := StringArrange(blockBData.LcCcmType, 40)
	ih_unit := StringArrange(blockBData.LcUnit, 20)
	ih_sthr := ByteArrange(blockBData.LcStHr)
	ih_stmn := ByteArrange(blockBData.LcStMn)
	ih_edhr := ByteArrange(blockBData.LcEdHr)
	ih_edmn := ByteArrange(blockBData.LcEdMn)
	ih_inmn := ByteArrange(blockBData.LcInMn)
	ih_dumn := ByteArrange(blockBData.LcDuMn)
	ih_rly_l := ByteArrange(blockBData.LcRlyL)
	ih_rly_h := ByteArrange(blockBData.LcRlyH)

	ihtxt := ih_valid + ih_room + ih_region + ih_order + ih_priority + ih_lv + ih_cast + ih_sr + ih_ccmtype + ih_unit + ih_sthr + ih_stmn + ih_edhr + ih_edmn + ih_inmn + ih_dumn + ih_rly_l + ih_rly_h
	resps := make([]*http.Response, responseCountBlockBC)
	for i := 0; i < responseCountBlockBC; i++ {
		tp := i * blockSize
		iht := ""
		if len(ihtxt) < tp+blockSize {
			iht = ihtxt[tp:]
		} else {
			iht = ihtxt[tp:(tp + blockSize)]
		}
		sz := Padding(fmt.Sprintf("%x", len(iht)/2), 2, "0")
		addr := Padding(fmt.Sprintf("%x", blockBData.BID*recstep+address+(tp/2)), 4, "0")
		ih := ":" + sz + addr + "00" + iht + "FF"
		// 送信処理
		url := "http://" + blockBData.IpAddr + "/" + ih
		// fmt.Println(url)
		resp, err := http.Get(url)
		if err != nil {
			resps[i] = nil
			return resps, err
		}
		resps[i] = resp
		resp.Body.Close()
	}
	return resps, nil
}

type BlockC struct {
	CID        int
	IpAddr     string
	LcValid    int
	LcRoom     int
	LcRegion   int
	LcOrder    int
	LcPriority int
	LcLv       int
	LcCast     int
	LcSr       string
	LcCcmType  string
	LcUnit     string
	LcStHr     int
	LcStMn     int
	LcEdHr     int
	LcEdMn     int
	LcInMn     int
	LcDuMn     int
	LcRlyL     int
	LcRlyH     int
}

func SendBlockC(blockCData BlockC) ([]*http.Response, error) {
	address := addressBaseBlockC
	recstep := recordStepBlockBC
	ih_valid := ByteArrange(blockCData.LcValid)
	ih_room := ByteArrange(blockCData.LcRoom)
	ih_region := ByteArrange(blockCData.LcRegion)
	order_o := Padding(fmt.Sprintf("%x", blockCData.LcOrder), 4, "0")
	ih_order := order_o[2:4] + order_o[0:2]
	ih_priority := ByteArrange(blockCData.LcPriority)
	ih_lv := ByteArrange(blockCData.LcLv)
	ih_cast := ByteArrange(blockCData.LcCast)
	ih_sr := StringArrange(blockCData.LcSr, 2)
	ih_ccmtype := StringArrange(blockCData.LcCcmType, 40)
	ih_unit := StringArrange(blockCData.LcUnit, 20)
	ih_sthr := ByteArrange(blockCData.LcStHr)
	ih_stmn := ByteArrange(blockCData.LcStMn)
	ih_edhr := ByteArrange(blockCData.LcEdHr)
	ih_edmn := ByteArrange(blockCData.LcEdMn)
	ih_inmn := ByteArrange(blockCData.LcInMn)
	ih_dumn := ByteArrange(blockCData.LcDuMn)
	ih_rly_l := ByteArrange(blockCData.LcRlyL)
	ih_rly_h := ByteArrange(blockCData.LcRlyH)

	ihtxt := ih_valid + ih_room + ih_region + ih_order + ih_priority + ih_lv + ih_cast + ih_sr + ih_ccmtype + ih_unit + ih_sthr + ih_stmn + ih_edhr + ih_edmn + ih_inmn + ih_dumn + ih_rly_l + ih_rly_h
	resps := make([]*http.Response, responseCountBlockBC)
	for i := 0; i < responseCountBlockBC; i++ {
		tp := i * blockSize
		iht := ""
		if len(ihtxt) < tp+blockSize {
			iht = ihtxt[tp:]
		} else {
			iht = ihtxt[tp:(tp + blockSize)]
		}
		sz := Padding(fmt.Sprintf("%x", len(iht)/2), 2, "0")
		addr := Padding(fmt.Sprintf("%x", blockCData.CID*recstep+address+(tp/2)), 4, "0")
		ih := ":" + sz + addr + "00" + iht + "FF"
		// 送信処理
		url := "http://" + blockCData.IpAddr + "/" + ih
		// fmt.Println(url)
		resp, err := http.Get(url)
		if err != nil {
			resps[i] = nil
			return resps, err
		}
		resps[i] = resp
		resp.Body.Close()
	}
	return resps, nil
}

type BlockD struct {
	DID            int
	IpAddr         string
	LcCopeValid    int
	LcCopeRoom     int
	LcCopeRegion   int
	LcCopeOrder    int
	LcCopePriority int
	LcCopeCcmType  string
	LcCopeOpe      int
	LcCopeFval     float32
}

func SendBlockD(blockDData BlockD) ([]*http.Response, error) {
	address := addressBaseBlockD
	recstep := recordStepBlockD
	ih_cope_valid := ByteArrange(blockDData.LcCopeValid)
	ih_cope_room := ByteArrange(blockDData.LcCopeRoom)
	ih_cope_region := ByteArrange(blockDData.LcCopeRegion)
	cope_order_o := Padding(fmt.Sprintf("%x", blockDData.LcCopeOrder), 4, "0")
	ih_cope_order := cope_order_o[2:4] + cope_order_o[0:2]
	ih_cope_priority := ByteArrange(blockDData.LcCopePriority)
	ih_cope_ccmtype := StringArrange(blockDData.LcCopeCcmType, 40)
	ih_cope_ope := ByteArrange(blockDData.LcCopeOpe)
	ih_cope_fval := Float32Bin(blockDData.LcCopeFval)

	ihtxt := ih_cope_valid + ih_cope_room + ih_cope_region + ih_cope_order + ih_cope_priority + ih_cope_ccmtype + ih_cope_ope + ih_cope_fval
	resps := make([]*http.Response, responseCountBlockD)
	for i := 0; i < responseCountBlockD; i++ {
		tp := i * blockSize
		iht := ""
		if len(ihtxt) < tp+blockSize {
			iht = ihtxt[tp:]
		} else {
			iht = ihtxt[tp:(tp + blockSize)]
		}
		sz := Padding(fmt.Sprintf("%x", len(iht)/2), 2, "0")
		addr := Padding(fmt.Sprintf("%x", blockDData.DID*recstep+address+(tp/2)), 4, "0")
		ih := ":" + sz + addr + "00" + iht + "FF"
		// 送信処理
		url := "http://" + blockDData.IpAddr + "/" + ih
		// fmt.Println(url)
		resp, err := http.Get(url)
		if err != nil {
			resps[i] = nil
			return resps, err
		}
		resps[i] = resp
		resp.Body.Close()
	}
	return resps, nil
}

func test_control() {
	print("A\n")
	blockA := BlockA{
		IpAddr:         "192.168.137.50",
		LcUecsID:       "10100C00000B",
		LcMac:          "02:A2:73:0B:00:2A",
		FixDhcpFlag:    255,
		FixedIpAddress: "192.168.38.50",
		FixedNetMask:   "255.255.255.0",
		FixedDefGw:     "192.168.11.1",
		FixedDns:       "192.168.11.1",
		VenderName:     "AMPSD",
		NodeName:       "TESTA123",
	}
	// send_BlockA("192.168.137.247", "10100C00000B", "02:A2:73:0B:00:2A", 0, "192.168.38.50", "255.255.255.0", "192.168.11.1", "192.168.11.1", "AMPSD", "TESTA123")
	SendBlockA(blockA)
	print("B\n")
	blockB := BlockB{
		BID:        0,
		IpAddr:     "192.168.137.50",
		LcValid:    1,
		LcRoom:     2,
		LcRegion:   2,
		LcOrder:    2,
		LcPriority: 1,
		LcLv:       3,
		LcCast:     1,
		LcSr:       "R",
		LcCcmType:  "InAirTemp",
		LcUnit:     "C",
		LcStHr:     0,
		LcStMn:     0,
		LcEdHr:     23,
		LcEdMn:     59,
		LcInMn:     1,
		LcDuMn:     1,
		LcRlyL:     252,
		LcRlyH:     252,
	}
	SendBlockB(blockB)
	// send_BlockB(1, "192.168.1.14", 1, 1, 1, 1, 15, 3, 0, "R", "InAirHumid", "%", 0, 0, 23, 59, 1, 1, 0, 255)
	print("C\n")
	blockC := BlockC{
		CID:        0,
		IpAddr:     "192.168.137.50",
		LcValid:    1,
		LcRoom:     2,
		LcRegion:   2,
		LcOrder:    2,
		LcPriority: 1,
		LcLv:       3,
		LcCast:     1,
		LcSr:       "S",
		LcCcmType:  "InAirTemp",
		LcUnit:     "C",
		LcStHr:     0,
		LcStMn:     0,
		LcEdHr:     23,
		LcEdMn:     59,
		LcInMn:     1,
		LcDuMn:     1,
		LcRlyL:     252,
		LcRlyH:     252,
	}
	SendBlockC(blockC)
	// send_BlockC(1, "192.168.1.14", 1, 1, 1, 1, 15, 3, 0, "R", "TEST789", "", 0, 0, 12, 00, 1, 1, 0, 255)
	print("D\n")

	var f float32 = 1.500
	blockD := BlockD{
		DID:            0,
		IpAddr:         "192.168.137.50",
		LcCopeValid:    1,
		LcCopeRoom:     2,
		LcCopeRegion:   2,
		LcCopeOrder:    2,
		LcCopePriority: 1,
		LcCopeCcmType:  "InAirTemp",
		LcCopeOpe:      0,
		LcCopeFval:     f,
	}
	SendBlockD(blockD)
}
