# import streamlit as st
from DBCfoo import symbolInfo,dailyEarn,importjson
# from time import sleep,strftime,localtime
import json
import streamlit as st
from MDEXreserve import MDEXreserve
import pandas as pd
# import streamlit.components.v1 as components
# import DBCjson

# # 从文件中读取block编码数据
blockList = []
file = open('blockList.json', mode='r')
blockList = json.loads(file.readline())
file.close()

# now = strftime("%Y-%m-%d %H:%M:%S", localtime())
payloads = {"jsonrpc":"2.0","id":9,"method":"eth_call","params":[{"from":"0x0000000000000000000000000000000000000000","data":"0xe39c08fc00000000000000000000000000000000000000000000000000000000000000010000000000000000000000002261e84b32f4c365464bfa54ef92a8c6a695fb74","to":"0x37bb1e43326320a6b3eab40bd6c782ffa54230b1"},"latest"]}
DBCHUSDdailyEarn = dailyEarn(int(blockList[0]),payloads)
payloads = {"jsonrpc":"2.0","id":9,"method":"eth_call","params":[{"from":"0x0000000000000000000000000000000000000000","data":"0xe39c08fc00000000000000000000000000000000000000000000000000000000000000020000000000000000000000002261e84b32f4c365464bfa54ef92a8c6a695fb74","to":"0x37bb1e43326320a6b3eab40bd6c782ffa54230b1"},"latest"]}
DBCHTdailyEarn = dailyEarn(int(blockList[1]),payloads)
payloads = {"jsonrpc":"2.0","id":9,"method":"eth_call","params":[{"from":"0x0000000000000000000000000000000000000000","data":"0xe39c08fc00000000000000000000000000000000000000000000000000000000000000030000000000000000000000002261e84b32f4c365464bfa54ef92a8c6a695fb74","to":"0x37bb1e43326320a6b3eab40bd6c782ffa54230b1"},"latest"]}
DBCMDXdailyEarn = dailyEarn(int(blockList[2]),payloads)
payloads = {"jsonrpc":"2.0","id":9,"method":"eth_call","params":[{"from":"0x0000000000000000000000000000000000000000","data":"0xe39c08fc00000000000000000000000000000000000000000000000000000000000000050000000000000000000000002261e84b32f4c365464bfa54ef92a8c6a695fb74","to":"0x37bb1e43326320a6b3eab40bd6c782ffa54230b1"},"latest"]}
DBCBAGdailyEarn = dailyEarn(int(blockList[3]),payloads)
payloads = {"jsonrpc":"2.0","id":9,"method":"eth_call","params":[{"from":"0x0000000000000000000000000000000000000000","data":"0xe39c08fc00000000000000000000000000000000000000000000000000000000000000040000000000000000000000002261e84b32f4c365464bfa54ef92a8c6a695fb74","to":"0x37bb1e43326320a6b3eab40bd6c782ffa54230b1"},"latest"]}
DBCCORdailyEarn = dailyEarn(int(blockList[4]),payloads)
total = DBCHUSDdailyEarn[0]+DBCHTdailyEarn[0]+DBCMDXdailyEarn[0]+DBCBAGdailyEarn[0]+DBCCORdailyEarn[0]
Earned =  DBCHUSDdailyEarn[1]+DBCHTdailyEarn[1]+DBCMDXdailyEarn[1]+DBCBAGdailyEarn[1]+DBCCORdailyEarn[1]

# if st.button("刷新（领取奖励后点刷新）"):
#     DBCjson.importjson()
#     st.write('刷新成功')
li = st.text_input('BlockList')
if li != "":
    url = "https://api.hecoinfo.com/api?module=account&action=txlist&address=0x2261E84B32f4C365464bfA54eF92A8c6a695FB74&startblock=" + li + "&endblock=999999999&sort=desc"
    importjson(url)
    st.write('刷新成功')
# if address != '输入地址':
#     DBCHUSD_Info = symbolInfo("1","0xa6ac028e989378E4757DDdE89bB265eDA5191b23",100000000,100000000,DBCHUSDdailyEarn,0,address)
#     DBCHT_Info = symbolInfo("2","0x87644aDb4b828cC377408751f775efA54AFB4fEf",1000000000000000000,100000000,DBCHTdailyEarn,1,address)
#     DBCMDX_Info = symbolInfo("3","0x3Aa67b6Fdc40B136BAb4aF8A23DAF0d0Ba27D756",1000000000000000000,100000000,DBCMDXdailyEarn,1,address)
#     DBCBAG_Info = symbolInfo("5","0x23D7EfEb1b44f21A75258f0FD31F837Ed2C952ea",100000000,1000000000000000000,DBCBAGdailyEarn,0,address)
# else:
#     DBCHUSD_Info = symbolInfo("1","0xa6ac028e989378E4757DDdE89bB265eDA5191b23",100000000,100000000,DBCHUSDdailyEarn,0)
#     DBCHT_Info = symbolInfo("2","0x87644aDb4b828cC377408751f775efA54AFB4fEf",1000000000000000000,100000000,DBCHTdailyEarn,1)
#     DBCMDX_Info = symbolInfo("3","0x3Aa67b6Fdc40B136BAb4aF8A23DAF0d0Ba27D756",1000000000000000000,100000000,DBCMDXdailyEarn,1)
#     DBCBAG_Info = symbolInfo("5","0x23D7EfEb1b44f21A75258f0FD31F837Ed2C952ea",100000000,1000000000000000000,DBCBAGdailyEarn,0)

DBCHUSD_Info = symbolInfo("1","0xa6ac028e989378E4757DDdE89bB265eDA5191b23",pow(10,8),pow(10,8),DBCHUSDdailyEarn,1)
DBCHT_Info = symbolInfo("2","0x87644aDb4b828cC377408751f775efA54AFB4fEf",pow(10,18),pow(10,8),DBCHTdailyEarn,1)
DBCMDX_Info = symbolInfo("3","0x3Aa67b6Fdc40B136BAb4aF8A23DAF0d0Ba27D756",pow(10,18),pow(10,8),DBCMDXdailyEarn,1)
DBCCOR_Info = symbolInfo("4","0xa07B65103C0955d0Ac159946FAaBBF52EdE0459e",pow(10,18),pow(10,8),DBCCORdailyEarn,1)
DBCBAG_Info = symbolInfo("5","0x23D7EfEb1b44f21A75258f0FD31F837Ed2C952ea",pow(10,8),pow(10,18),DBCBAGdailyEarn,0)
    
DBCPrice = (DBCHUSD_Info[0]/DBCHUSD_Info[1])
assets = (DBCHUSD_Info[1]+DBCHT_Info[1]+DBCMDX_Info[1]+DBCBAG_Info[1])*2*DBCPrice

# st.write('Hello, world!')
def show(name,info,col,symbol1,symbol2):
    with col:
        name = "### " + name
        st.markdown(name)
        if symbol1 == "DBC":
            assets = info[1] * DBCPrice * 2
        else:
            assets = info[0] * DBCPrice * 2
        st.markdown('dailyEarn：{:.0f}'.format(info[4][0]))
        st.markdown('PCT：{:.1%}；APY：{:.1%}'.format(info[2],info[3]))
        st.markdown('{:.1f} {} + {:.1f} {} = ${:.0f} '.format(info[1],symbol1,info[0],symbol2,assets))
        # st.markdown('symbol1：{:.1f}；   symbol2：{:.1f}'.format(info[1],info[0]))
        # my_bar = st.progress(0)
        # percent = int(info[2]*100)
        # for percent_complete in range(percent):
        #     sleep(0.02)
        #     my_bar.progress(percent_complete + 1)

col1, col2 = st.beta_columns(2)
data = [{"name":"DBCHUSD","symbol1":"DBC","symbol2":"HUSD","data":DBCHUSD_Info,"col":col1},
        {"name":"DBCHT","symbol1":"DBC","symbol2":"HT","data":DBCHT_Info,"col":col2},
        {"name":"DBCMDX","symbol1":"DBC","symbol2":"MDX","data":DBCMDX_Info,"col":col1},
        {"name":"DBCBAG","symbol1":"BAG","symbol2":"DBC","data":DBCBAG_Info,"col":col2},
        {"name":"DBCCOR","symbol1":"DBC","symbol2":"COR","data":DBCCOR_Info,"col":col1},
        ]
for i in data:
    show(i["name"],i["data"],i["col"],i["symbol1"],i["symbol2"])

allpool = DBCHUSD_Info[5]+DBCHT_Info[5]+DBCMDX_Info[5]+DBCCOR_Info[5]+DBCBAG_Info[5]
st.markdown("### 总池情况")

# pd.set_option('display.float_format',
#       lambda x: '{:.1%}'.format(x) if x < 1 else '{:,.0f}'.format(x))

pools = pd.DataFrame(
    [
    [DBCHUSD_Info[5],DBCHUSD_Info[5]/allpool],
    [DBCHT_Info[5],DBCHT_Info[5]/allpool],
    [DBCMDX_Info[5],DBCMDX_Info[5]/allpool],
    [DBCBAG_Info[5],DBCBAG_Info[5]/allpool,],
    [DBCCOR_Info[5],DBCCOR_Info[5]/allpool],
    [allpool,0],
    ],
    index=["HUSD","HT","MDX","BAG","COR","ALL"],
    columns=["数量","占比"]
    )
pools["占比"] = pools["占比"].apply(lambda x:'{:.1%}'.format(x))
pools["数量"] = pools["数量"].apply(lambda x:'{:,.0f}'.format(x))
# pools = pools.apply(lambda x: '{:.1%}'.format(x) if x < 1 else '{:,.0f}'.format(x))
    
st.table(pools)
# st.markdown('''
#             |名称|数量|占比|
#             | --- | --- |--- |
#             | HUSD|{:.0f} |{:.1%}|
#             | HT |  {:.0f} | {:.1%}|
#             | MDX|{:.0f} |{:.1%}|
#             | BAG| {:.0f} |{:.1%}|
#             | COR|{:.0f}  |{:.1%}|
#             |total|{:.0f}|  |
#             '''
#             .format(DBCHUSD_Info[5],DBCHUSD_Info[5]/allpool,DBCHT_Info[5],DBCHT_Info[5]/allpool, \
#                     DBCMDX_Info[5],DBCMDX_Info[5]/allpool,DBCBAG_Info[5],DBCBAG_Info[5]/allpool, \
#                     DBCCOR_Info[5],DBCCOR_Info[5]/allpool,allpool))

st.markdown("### total:")
st.markdown("日收：${:.0f} || 日收：{:.0f} || 待收：{:.1f} ||  总资产：${:.0f}".format(total*(DBCPrice),total,Earned,assets))

DBSreserve = MDEXreserve("0x3dfD44E24F36d04ec1E1B79Aa6f912cC4f7d2107",pow(10,8),pow(10,8))
DBSPrice = DBSreserve[0]/DBSreserve[1]

st.markdown("* DBC：${:.3f} || DBS：${:.3f} ".format(DBCPrice,DBSPrice))
