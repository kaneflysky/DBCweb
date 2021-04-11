#!/usr/bin/python3
# coding: utf-8

import requests
import json
from web3 import Web3
from MDEXreserve import MDEXreserve  ##读取交易对价格 

w3 = Web3()
headers = {"content-type": "application/json"}
url = "https://http-mainnet-node.huobichain.com/"
lp = []

##获取Lp情况
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

##生成post数据
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

##更新blocklist
def importjson(url):
    blockList = []
    # url = "https://api.hecoinfo.com/api?module=account&action=txlist&address=0x2261E84B32f4C365464bfA54eF92A8c6a695FB74&startblock=3494080&endblock=999999999&sort=desc"
    response = requests.request("GET",url)
    results = response.json()
    
    blockList = [results["result"][4]["blockNumber"],results["result"][3]["blockNumber"],results["result"][2]["blockNumber"],results["result"][1]["blockNumber"],results["result"][0]["blockNumber"]]
    
    
    file = open('blockList.json', 'w')
    json.dump(blockList,file)
    file.close()

##获取日产情况
def dailyEarn(startBlock,payloads):
    Blockload = {"jsonrpc":"2.0","method":"eth_blockNumber","id":1,"params":[]}
    response = requests.request("POST", url, json=Blockload, headers=headers)
    results = response.json()
    lastBlock = int(eval(results["result"]))
    
    payload = payloads
    response = requests.request("POST", url, json=payload, headers=headers)
    results = response.json()
    earned = int(eval(results["result"]))/100000000
    dailyEarn = earned/(lastBlock - startBlock)*28800
    return dailyEarn,earned

##整合交易对情况数据
def symbolInfo(bankIndex,amountAddress,decimals1,decimals2,dailyEarn,mainSymbol,myAddress = "2261e84b32f4c365464bfa54ef92a8c6a695fb74",):
    symbolPrice = MDEXreserve(amountAddress,decimals1,decimals2)
    symbolPercent = Percent(bankIndex,myAddress)
    symbol1 = symbolPercent*symbolPrice[0]
    symbol2 = symbolPercent*symbolPrice[1]
    if mainSymbol==0:
        try:
            symbolAPY = dailyEarn[0]/symbol1*365/2
        except:
            symbolAPY = 0
        amount = symbolPrice[0]
    else:
        try:
            symbolAPY = dailyEarn[0]/symbol2*365/2
        except:
            symbolAPY = 0
        amount = symbolPrice[1]
    return symbol1,symbol2,symbolPercent,symbolAPY,dailyEarn,amount

