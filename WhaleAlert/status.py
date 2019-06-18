# https://api.whale-alert.io/v1/status?api_key=c8NzK9pvEGCc1XW8hIcwLrrB1Kxi8649
"""
{
    "result": "success",
    "blockchain_count": 9,
    "blockchains": [
        {
            "name": "ethereum",
            "symbols": [
                "wtc",
                "ankr",
                "man",
                "nas",
                "omg",
                "qnt",
                "vest",
                "srn",
                "zil",
                "ctxc",
                "dent",
                "icn",
                "loom",
                "rhoc",
                "credo",
                "ppt",
                "req",
                "trx",
                "abt",
                "hot",
                "salt",
                "sub",
                "gvt",
                "iotx",
                "kcs",
                "meta",
                "pay",
                "theta",
                "ttc",
                "bat",
                "bnt",
                "cmt",
                "gnt",
                "mgo",
                "edo",
                "knc",
                "xyo",
                "appc",
                "eng",
                "mco",
                "pax",
                "zrx",
                "dgtx",
                "edr",
                "ethos",
                "icx",
                "storj",
                "wic",
                "iost",
                "qbit",
                "cnd",
                "fun",
                "la",
                "nec",
                "npxs",
                "thr",
                "aion",
                "tomo",
                "vibe",
                "bczero",
                "kin",
                "powr",
                "osa",
                "aoa",
                "enj",
                "gusd",
                "mft",
                "nexo",
                "cennz",
                "dai",
                "rlc",
                "tnb",
                "qkc",
                "tusd",
                "eth",
                "ht",
                "mtl",
                "storm",
                "usdc",
                "veri",
                "qash",
                "san",
                "bix",
                "bnb",
                "gnx",
                "leo",
                "lrc",
                "nuls",
                "xin",
                "mda",
                "iht",
                "mana",
                "link",
                "mxm",
                "agi",
                "cro",
                "eurs",
                "brd",
                "elf",
                "inb",
                "bhpc",
                "cvc",
                "snt",
                "cosm",
                "ae",
                "dgd",
                "hpt",
                "kan",
                "usdt",
                "wax",
                "btm",
                "dcn",
                "evx",
                "ncash",
                "tct",
                "trac",
                "rep",
                "dac",
                "drgn",
                "mkr",
                "ocn",
                "poly",
                "r",
                "lky",
                "tel"
            ],
            "status": "connected"
        },
        {
            "name": "stellar",
            "symbols": [
                "mobi",
                "slt",
                "repo",
                "xlm"
            ],
            "status": "connected"
        },
        {
            "name": "tron",
            "symbols": [
                "trx",
                "btt",
                "usdt"
            ],
            "status": "connected"
        },
        {
            "name": "binancechain",
            "symbols": [
                "bnb"
            ],
            "status": "connected"
        },
        {
            "name": "neo",
            "symbols": [
                "gas",
                "neo"
            ],
            "status": "connected"
        },
        {
            "name": "ripple",
            "symbols": [
                "xrp"
            ],
            "status": "connected"
        },
        {
            "name": "eos",
            "symbols": [
                "eos"
            ],
            "status": "connected"
        },
        {
            "name": "bitcoin",
            "symbols": [
                "btc",
                "usdt"
            ],
            "status": "connected"
        },
        {
            "name": "tezos",
            "symbols": [
                "xtz"
            ],
            "status": "connected"
        }
    ]
}
"""

# requests 모듈 설치
# https://shaeod.tistory.com/929

import json
import requests

api_key='c8NzK9pvEGCc1XW8hIcwLrrB1Kxi8649'
url = 'https://api.whale-alert.io/v1/status?api_key=' + api_key

res = requests.get(url)
# print(res.text)

toObj = json.loads(res.text)
# print(toObj)

result = toObj['result']
blockchain_count = int(toObj['blockchain_count'])

# print('result : ', toObj['result'])
# print('blockchains : ', toObj['blockchains'])

print('result : ', result)
print('blockchain_count : ', blockchain_count)


blockchains = toObj['blockchains']

for i in range(0,blockchain_count):
    print('coin Code : ', blockchains[i]['name'], '(', blockchains[i]['status'],')')
