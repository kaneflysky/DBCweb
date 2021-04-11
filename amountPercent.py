#!/usr/bin/python3
# coding: utf-8

import requests
from web3 import Web3

w3 = Web3()
headers = {"content-type": "application/json"}
url = "https://http-mainnet-node.huobichain.com/"

lp = []

bankIndex = "1"

def Percent(bankIndex,myAddress):
    contractAddress = "0x37bb1e43326320a6b3eab40bd6c782ffa54230b1"
    methodId = w3.sha3(text="bidToUserStakeInfo(uint256,address)")[0:4].hex()
    bid = "000000000000000000000000000000000000000000000000000000000000000" + bankIndex + "000000000000000000000000"
    data = methodId + bid + myAddress
    
    amount = w3.toInt(hexstr= getResponse(data, contractAddress)[0:66])
    
    methodId = w3.sha3(text="indexToBank(uint256)")[0:4].hex()
    bid = "000000000000000000000000000000000000000000000000000000000000000" + bankIndex
    data = methodId + bid

    totalSupply = w3.toInt(hexstr=getResponse(data, contractAddress)[579:642])
    return amount/totalSupply
    # return results

def getResponse(data,contractAddress):
    payload = {"jsonrpc":"2.0",
            "id":12,
            "method":"eth_call",
            "params":[{"from":"0x0000000000000000000000000000000000000000",
                      "data":data,
                      "to":contractAddress},
                      "latest"]}
    response = requests.request("POST", url, json=payload, headers=headers)
    results = response.json()["result"]
    return results

