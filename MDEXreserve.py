#!/usr/bin/python3
# coding: utf-8
#获取交易对价格
import requests
import web3

w3 = web3.Web3()

headers = {"content-type": "application/json"}
url = "https://http-mainnet-node.huobichain.com/"

methodId = w3.sha3(text='getReserves()')[0:4].hex() + "000000000000000000000000"

def MDEXreserve(contractAddress,decimals1,decimals2):
    payload = {"jsonrpc":"2.0",
               "id":1,
               "method":"eth_call",
               "params":
                   [{"from":"0x0000000000000000000000000000000000000000",
                     "data":methodId,
                     "to":contractAddress},
                    "latest"]}

    response = requests.request("POST", url, json=payload, headers=headers)
    result = response.json()["result"]

    reserve0 = w3.toInt(hexstr=result[0:66])/decimals1
    reserve1 = w3.toInt(hexstr=result[67:130])/decimals2
    return reserve0,reserve1
