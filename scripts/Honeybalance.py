# xDai - Honeyswap balancer

from brownie import accounts, web3, Contract
import requests
import json
import pickle
import time
import pprint
import sys
import math
import pprint

acct = accounts.load(your_account_name)

portfolio = {
    'XDAI': 0.10,
    'WXDAI': 0.20,
    'HNY': 0.70
}
prices = {}

ercAddresses = {}
contracts = {}
priceOfETH = {}

balances = {}
balancesusd = {}
Contracts = {}
decimals = {}

ercAddresses['HNY'] = "0x71850b7e9ee3f13ab46d67167341e4bdc905eef9"
ercAddresses['WXDAI'] = "0xe91d153e0b41518a2ce8dd3d7944fa863463a97d"
ercAddresses['STAKE'] = "0xb7d311e2eb55f2f68a9440da38e7989210b9a05e"
ercAddresses['xMOON'] = "0x1e16aa4df73d29c029d94ceda3e3114ec191e25a"

UniswapV2Factory = "0xA818b4F111Ccac7AA31D0BCc0806d64F2E0737D7"
UniswapV2Router02 = "0x1C232F01118CB8B424793ae03F870aa7D0ac7f77"

UniswapV2Factoryabi = json.loads('[{"type": "constructor", "stateMutability": "nonpayable", "payable": false, "inputs": [{"type": "address", "name": "_feeToSetter", "internalType": "address"}]}, {"type": "event", "name": "PairCreated", "inputs": [{"type": "address", "name": "token0", "internalType": "address", "indexed": true}, {"type": "address", "name": "token1", "internalType": "address", "indexed": true}, {"type": "address", "name": "pair", "internalType": "address", "indexed": false}, {"type": "uint256", "name": "", "internalType": "uint256", "indexed": false}], "anonymous": false}, {"type": "function", "stateMutability": "view", "payable": false, "outputs": [{"type": "address", "name": "", "internalType": "address"}], "name": "allPairs", "inputs": [{"type": "uint256", "name": "", "internalType": "uint256"}], "constant": true}, {"type": "function", "stateMutability": "view", "payable": false, "outputs": [{"type": "uint256", "name": "", "internalType": "uint256"}], "name": "allPairsLength", "inputs": [], "constant":true}, {"type": "function", "stateMutability": "nonpayable", "payable": false, "outputs": [{"type": "address", "name": "pair", "internalType": "address"}], "name": "createPair", "inputs": [    {"type": "address", "name": "tokenA", "internalType": "address"}, {"type": "address", "name": "tokenB", "internalType": "address"}], "constant": false}, {"type": "function", "stateMutability": "view", "payable": false, "outputs": [{"type": "address", "name": "", "internalType": "address"}], "name": "feeTo", "inputs": [], "constant":true}, {"type": "function", "stateMutability": "view", "payable": false, "outputs": [{"type": "address", "name": "", "internalType": "address"}], "name": "feeToSetter", "inputs": [], "constant":true}, {"type": "function", "stateMutability": "view", "payable": false, "outputs": [{"type": "address", "name": "", "internalType": "address"}], "name": "getPair", "inputs": [{"type": "address", "name": "", "internalType": "address"}, {"type": "address", "name": "", "internalType": "address"}], "constant": true}, {"type": "function", "stateMutability": "nonpayable", "payable": false, "outputs": [], "name":"setFeeTo", "inputs":[{"type": "address", "name": "_feeTo", "internalType": "address"}], "constant": false}, {"type": "function", "stateMutability": "nonpayable", "payable": false, "outputs": [], "name":"setFeeToSetter", "inputs":[{"type": "address", "name": "_feeToSetter", "internalType": "address"}], "constant": false}]')
UniswapV2Router02abi = json.loads('[{"type": "constructor", "stateMutability": "nonpayable", "inputs": [{"type": "address", "name": "_factory", "internalType": "address"}, {"type": "address", "name": "_WETH", "internalType": "address"}]}, {"type": "function", "stateMutability": "view", "outputs": [{"type": "address", "name": "", "internalType": "address"}], "name": "WETH", "inputs": []}, {"type": "function", "stateMutability": "nonpayable", "outputs": [{"type": "uint256", "name": "amountA", "internalType": "uint256"}, {"type": "uint256", "name": "amountB", "internalType": "uint256"}, {"type": "uint256", "name": "liquidity", "internalType": "uint256"}], "name": "addLiquidity", "inputs": [{"type": "address", "name": "tokenA", "internalType": "address"}, {"type": "address", "name": "tokenB", "internalType": "address"}, {"type": "uint256", "name": "amountADesired", "internalType": "uint256"}, {"type": "uint256", "name": "amountBDesired", "internalType": "uint256"}, {"type": "uint256", "name": "amountAMin", "internalType": "uint256"}, {"type": "uint256", "name": "amountBMin", "internalType": "uint256"}, {"type": "address", "name": "to", "internalType": "address"}, {"type": "uint256", "name": "deadline", "internalType": "uint256"}]}, {"type": "function", "stateMutability": "payable", "outputs": [{"type": "uint256", "name": "amountToken", "internalType": "uint256"}, {"type": "uint256", "name": "amountETH", "internalType": "uint256"}, {"type": "uint256", "name": "liquidity", "internalType": "uint256"}], "name": "addLiquidityETH", "inputs": [{"type": "address", "name": "token", "internalType": "address"}, {"type": "uint256", "name": "amountTokenDesired", "internalType": "uint256"}, {"type": "uint256", "name": "amountTokenMin", "internalType": "uint256"}, {"type": "uint256", "name": "amountETHMin", "internalType": "uint256"}, {"type": "address", "name": "to", "internalType": "address"}, {"type": "uint256", "name": "deadline", "internalType": "uint256"}]}, {"type": "function", "stateMutability": "view", "outputs": [{"type": "address", "name": "", "internalType": "address"}], "name": "factory", "inputs": []}, {"type": "function", "stateMutability": "pure", "outputs": [{"type": "uint256", "name": "amountIn", "internalType": "uint256"}], "name": "getAmountIn", "inputs": [{"type": "uint256", "name": "amountOut", "internalType": "uint256"}, {"type": "uint256", "name": "reserveIn", "internalType": "uint256"}, {"type": "uint256", "name": "reserveOut", "internalType": "uint256"}]}, {"type": "function", "stateMutability": "pure", "outputs": [{"type": "uint256", "name": "amountOut", "internalType": "uint256"}], "name": "getAmountOut", "inputs": [{"type": "uint256", "name": "amountIn", "internalType": "uint256"}, {"type": "uint256", "name": "reserveIn", "internalType": "uint256"}, {"type": "uint256", "name": "reserveOut", "internalType": "uint256"}]}, {"type": "function", "stateMutability": "view", "outputs": [{"type": "uint256[]", "name": "amounts", "internalType": "uint256[]"}], "name": "getAmountsIn", "inputs": [{"type": "uint256", "name": "amountOut", "internalType": "uint256"}, {"type": "address[]", "name": "path", "internalType": "address[]"}]}, {"type": "function", "stateMutability": "view", "outputs": [{"type": "uint256[]", "name": "amounts", "internalType": "uint256[]"}], "name": "getAmountsOut", "inputs": [{"type": "uint256", "name": "amountIn", "internalType": "uint256"}, {"type": "address[]", "name": "path", "internalType": "address[]"}]}, {"type": "function", "stateMutability": "pure", "outputs": [{"type": "uint256", "name": "amountB", "internalType": "uint256"}], "name": "quote", "inputs": [{"type": "uint256", "name": "amountA", "internalType": "uint256"}, {"type": "uint256", "name": "reserveA", "internalType": "uint256"}, {"type": "uint256", "name": "reserveB", "internalType": "uint256"}]}, {"type": "function", "stateMutability": "nonpayable", "outputs": [{"type": "uint256", "name": "amountA", "internalType": "uint256"}, {"type": "uint256", "name": "amountB", "internalType": "uint256"}], "name": "removeLiquidity", "inputs": [{"type": "address", "name": "tokenA", "internalType": "address"}, {"type": "address", "name": "tokenB", "internalType": "address"}, {"type": "uint256", "name": "liquidity", "internalType": "uint256"}, {"type": "uint256", "name": "amountAMin", "internalType": "uint256"}, {"type": "uint256", "name": "amountBMin", "internalType": "uint256"}, {"type": "address", "name": "to", "internalType": "address"}, {"type": "uint256", "name": "deadline", "internalType": "uint256"}]}, {"type": "function", "stateMutability": "nonpayable", "outputs": [{"type": "uint256", "name": "amountToken", "internalType": "uint256"}, {"type": "uint256", "name": "amountETH", "internalType": "uint256"}], "name": "removeLiquidityETH", "inputs": [{"type": "address", "name": "token", "internalType": "address"}, {"type": "uint256", "name": "liquidity", "internalType": "uint256"}, {"type": "uint256", "name": "amountTokenMin", "internalType": "uint256"}, {"type": "uint256", "name": "amountETHMin", "internalType": "uint256"}, {"type": "address", "name": "to", "internalType": "address"}, {"type": "uint256", "name": "deadline", "internalType": "uint256"}]}, {"type": "function", "stateMutability": "nonpayable", "outputs": [{"type": "uint256", "name": "amountETH", "internalType": "uint256"}], "name": "removeLiquidityETHSupportingFeeOnTransferTokens", "inputs": [{"type": "address", "name": "token", "internalType": "address"}, {"type": "uint256", "name": "liquidity", "internalType": "uint256"}, {"type": "uint256", "name": "amountTokenMin", "internalType": "uint256"}, {"type": "uint256", "name": "amountETHMin", "internalType": "uint256"}, {"type": "address", "name": "to", "internalType": "address"}, {"type": "uint256", "name": "deadline", "internalType": "uint256"}]}, {"type": "function", "stateMutability": "nonpayable", "outputs": [{"type": "uint256", "name": "amountToken", "internalType": "uint256"}, {"type": "uint256", "name": "amountETH", "internalType": "uint256"}], "name": "removeLiquidityETHWithPermit", "inputs": [{"type": "address", "name": "token", "internalType": "address"}, {"type": "uint256", "name": "liquidity", "internalType": "uint256"}, {"type": "uint256", "name": "amountTokenMin", "internalType": "uint256"}, {"type": "uint256", "name": "amountETHMin", "internalType": "uint256"}, {"type": "address", "name": "to", "internalType": "address"}, {"type": "uint256", "name": "deadline", "internalType": "uint256"}, {   "type": "bool", "name": "approveMax", "internalType": "bool"}, {"type": "uint8", "name": "v", "internalType": "uint8"}, {"type": "bytes32", "name": "r", "internalType": "bytes32"}, {"type": "bytes32", "name": "s", "internalType": "bytes32"}]}, {"type": "function", "stateMutability": "nonpayable", "outputs": [{"type": "uint256", "name": "amountETH", "internalType": "uint256"}], "name": "removeLiquidityETHWithPermitSupportingFeeOnTransferTokens", "inputs": [{"type": "address", "name": "token", "internalType": "address"}, {"type": "uint256", "name": "liquidity", "internalType": "uint256"}, {"type": "uint256", "name": "amountTokenMin", "internalType": "uint256"}, {"type": "uint256", "name": "amountETHMin", "internalType": "uint256"}, {"type": "address", "name": "to", "internalType": "address"}, {"type": "uint256", "name": "deadline", "internalType": "uint256"}, {"type": "bool", "name": "approveMax", "internalType": "bool"}, {"type": "uint8", "name": "v", "internalType": "uint8"}, {"type": "bytes32", "name": "r", "internalType": "bytes32"}, {"type": "bytes32", "name": "s", "internalType": "bytes32"}]}, {"type": "function", "stateMutability": "nonpayable", "outputs": [{"type": "uint256", "name": "amountA", "internalType": "uint256"}, {"type": "uint256", "name": "amountB", "internalType": "uint256"}], "name": "removeLiquidityWithPermit", "inputs": [{"type": "address", "name": "tokenA", "internalType": "address"}, {"type": "address", "name": "tokenB", "internalType": "address"}, {"type": "uint256", "name": "liquidity", "internalType": "uint256"}, {"type": "uint256", "name": "amountAMin", "internalType": "uint256"}, {"type": "uint256", "name": "amountBMin", "internalType": "uint256"}, {"type": "address", "name": "to", "internalType": "address"}, {"type": "uint256", "name": "deadline", "internalType": "uint256"}, {"type": "bool", "name": "approveMax", "internalType": "bool"}, {"type": "uint8", "name": "v", "internalType": "uint8"}, {"type": "bytes32", "name": "r", "internalType": "bytes32"}, {"type": "bytes32", "name": "s", "internalType": "bytes32"}]}, {"type": "function", "stateMutability": "payable", "outputs": [{"type": "uint256[]", "name": "amounts", "internalType": "uint256[]"}], "name": "swapETHForExactTokens", "inputs": [{"type": "uint256", "name": "amountOut", "internalType": "uint256"}, {"type": "address[]", "name": "path", "internalType": "address[]"}, {"type": "address", "name": "to", "internalType": "address"}, {"type": "uint256", "name": "deadline", "internalType": "uint256"}]}, {"type": "function", "stateMutability": "payable", "outputs": [{"type": "uint256[]", "name": "amounts", "internalType": "uint256[]"}], "name": "swapExactETHForTokens", "inputs": [{"type": "uint256", "name": "amountOutMin", "internalType": "uint256"}, {"type": "address[]", "name": "path", "internalType": "address[]"}, {"type": "address", "name": "to", "internalType": "address"}, {"type": "uint256", "name": "deadline", "internalType": "uint256"}]}, {"type": "function", "stateMutability": "payable", "outputs": [], "name":"swapExactETHForTokensSupportingFeeOnTransferTokens", "inputs":[{"type": "uint256", "name": "amountOutMin", "internalType": "uint256"}, {"type": "address[]", "name": "path", "internalType": "address[]"}, {"type": "address", "name": "to", "internalType": "address"}, {"type": "uint256", "name": "deadline", "internalType": "uint256"}]}, {"type": "function", "stateMutability": "nonpayable", "outputs": [{"type": "uint256[]", "name": "amounts", "internalType": "uint256[]"}], "name": "swapExactTokensForETH", "inputs": [{"type": "uint256", "name": "amountIn", "internalType": "uint256"}, {"type": "uint256", "name": "amountOutMin", "internalType": "uint256"}, {"type": "address[]", "name": "path", "internalType": "address[]"}, {"type": "address", "name": "to", "internalType": "address"}, {"type": "uint256", "name": "deadline", "internalType": "uint256"}]}, {"type": "function", "stateMutability": "nonpayable", "outputs": [], "name":"swapExactTokensForETHSupportingFeeOnTransferTokens", "inputs":[{"type": "uint256", "name": "amountIn", "internalType": "uint256"}, {"type": "uint256", "name": "amountOutMin", "internalType": "uint256"}, {"type": "address[]", "name": "path", "internalType": "address[]"}, {"type": "address", "name": "to", "internalType": "address"}, {"type": "uint256", "name": "deadline", "internalType": "uint256"}]}, {"type": "function", "stateMutability": "nonpayable", "outputs": [{"type": "uint256[]", "name": "amounts", "internalType": "uint256[]"}], "name": "swapExactTokensForTokens", "inputs": [{"type": "uint256", "name": "amountIn", "internalType": "uint256"}, {"type": "uint256", "name": "amountOutMin", "internalType": "uint256"}, {"type": "address[]", "name": "path", "internalType": "address[]"}, {"type": "address", "name": "to", "internalType": "address"}, {"type": "uint256", "name": "deadline", "internalType": "uint256"}]}, {"type": "function", "stateMutability": "nonpayable", "outputs": [], "name":"swapExactTokensForTokensSupportingFeeOnTransferTokens", "inputs":[{"type": "uint256", "name": "amountIn", "internalType": "uint256"}, {"type": "uint256", "name": "amountOutMin", "internalType": "uint256"}, {"type": "address[]", "name": "path", "internalType": "address[]"}, {"type": "address", "name": "to", "internalType": "address"}, {"type": "uint256", "name": "deadline", "internalType": "uint256"}]}, {"type": "function", "stateMutability": "nonpayable", "outputs": [{"type": "uint256[]", "name": "amounts", "internalType": "uint256[]"}], "name": "swapTokensForExactETH", "inputs": [{"type": "uint256", "name": "amountOut", "internalType": "uint256"}, {"type": "uint256", "name": "amountInMax", "internalType": "uint256"}, {"type": "address[]", "name": "path", "internalType": "address[]"}, {"type": "address", "name": "to", "internalType": "address"}, {"type": "uint256", "name": "deadline", "internalType": "uint256"}]}, {"type": "function", "stateMutability": "nonpayable", "outputs": [{"type": "uint256[]", "name": "amounts", "internalType": "uint256[]"}], "name": "swapTokensForExactTokens", "inputs": [{"type": "uint256", "name": "amountOut", "internalType": "uint256"}, {"type": "uint256", "name": "amountInMax", "internalType": "uint256"}, {"type": "address[]", "name": "path", "internalType": "address[]"}, {"type": "address", "name": "to", "internalType": "address"}, {"type": "uint256", "name": "deadline", "internalType": "uint256"}]}, {"type": "receive", "stateMutability": "payable"}]')
UniswapV2Pairabi = json.load(open('scripts/abi/IUniswapV2Pairabi.json', 'r'))

web3.eth.defaultAccount = acct.address
accAddress = acct.address
print(accAddress)
# print(web3.eth.chainId)


def getContracts():
    global Contracts
    for key, value in ercAddresses.items():
        address = web3.toChecksumAddress(value)
        abi = json.loads(getABI(address)['result'])
        Contracts[key] = Contract.from_abi(key, address, abi)


def getABI(contract_address):
    url_eth = "https://blockscout.com/poa/xdai/api"
    API_ENDPOINT = url_eth + \
        "?module=contract&action=getabi&address="+str(contract_address)
    r = requests.get(url=API_ENDPOINT)
    response = r.json()
    return response


def convertToNormal(bignumber, decimal):
    return bignumber / 10 ** decimal


def backtoWack(smallnumber, decimal):
    return int(smallnumber * 10 ** decimal)


def getBalances():
    global balances, decimals
    for key, value in portfolio.items():
        balance = 0
        if key == 'XDAI':
            balance = acct.balance()
        else:
            balance = Contracts[key].balanceOf(accAddress, {"from": acct})
        decimals[key] = 18
        balances[key] = convertToNormal(balance, decimals[key])

    pprint.pprint(balances)

# def getBalances():
#     global balances, decimals, ercAddresses
#     url_eth = "https://blockscout.com/poa/xdai/api"

#     API_ENDPOINT = url_eth + \
#         "?module=account&action=tokenlist&address={}".format(accAddress)
#     r = requests.get(url=API_ENDPOINT)
#     response = r.json()
#     if response["status"] == "1":
#         arrTokens = response["result"]
#         for iToken in arrTokens:
#             balance = int(iToken['balance'])
#             sym = iToken['symbol']
#             decimals[sym] = int(iToken['decimals'])
#             balances[sym] = convertToNormal(balance, decimals[sym])
#             ercAddresses[sym] = iToken['contractAddress']

#     #  xdai balance
#     API_ENDPOINT = url_eth + \
#         "?module=account&action=balance&address={}".format(accAddress)
#     r = requests.get(url=API_ENDPOINT)
#     response = r.json()
#     if response["status"] == "1":
#         balances["XDAI"] = convertToNormal(int(response["result"]), 18)
#         decimals["XDAI"] = 18
#         ercAddresses["XDAI"] = "0xe91d153e0b41518a2ce8dd3d7944fa863463a97d"

#     # for key, value in ercAddresses.items():
#     #     sym = key
#     #     contract_address = value
#     #     API_ENDPOINT = url_eth + \
#     #         "?module=account&action=tokenbalance&contractaddress={}&address={}".format(
#     #             contract_address, accAddress)
#     #     r = requests.get(url=API_ENDPOINT)
#     #     response = r.json()
#     #     if response["status"] == "1":
#     #         balances[sym] = int(response["result"])
#     print(balances)

# def getPrices():
#     global prices
#     priceData = requests.get(
#         "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd")
#     pricesInfo = priceData.json()
#     for priceItem in pricesInfo:
#         sym = priceItem['symbol'].upper()
#         if sym in baseAssets:
#             prices[sym] = priceItem['current_price']
#     pprint.pprint(prices)


def getAddresses():
    global contracts
    for key, value in ercAddresses.items():
        contracts[key] = web3.toChecksumAddress(value)


# honeyswapFactory_contract = web3.toChecksumAddress(UniswapV2Factory)
# print(honeyswapFactory_contract)
# # load our contract
# honeyswapFactory_join = web3.eth.contract(
#     address=honeyswapFactory_contract, abi=UniswapV2Factoryabi)

# contract_response = honeyswapFactory_join.functions.allPairsLength().call()
# print(contract_response)

honeyswap_contract = web3.toChecksumAddress(UniswapV2Router02)
# load our contract
honeyswap_join = web3.eth.contract(
    address=honeyswap_contract, abi=UniswapV2Router02abi)
Honeyswap_Contract = Contract.from_abi(
    "Honeyswap", honeyswap_contract, UniswapV2Router02abi)

# # find liquidity share value
# UNIV2 = "0x4505b262dc053998c10685dc5f9098af8ae5c8ad"
# univ2_contract = web3.toChecksumAddress(UNIV2)
# # load our contract
# univ2_join = web3.eth.contract(
#     address=univ2_contract, abi=UniswapV2Pairabi)
# # ress = convertToNormal(univ2_join.functions.kLast().call(), 18)
# ress2 = univ2_join.functions.getReserves().call()
# # print(ress)
# #  WxDai reserve in hny-wxdai pool
# # hard hack to calc pool value in usd
# reserve0 = convertToNormal(ress2[0], 18)
# reserve1 = convertToNormal(ress2[1], 18)
# totalLiq = reserve1 * 2
# shareVal = totalLiq / math.sqrt(reserve1 * reserve0)


def main():
    getContracts()
    # get native balances
    getBalances()
    # convert to checksum address
    getAddresses()
    # quote for 1 asset in usd
    amountIn = 1 * 10 ** 18
    # use WXDAI as common market measure (assume WXDAI = $1)
    quote = 'WXDAI'
    # wxdai_abi = json.loads(getABI(contracts['WXDAI'])['result'])
    # print(wxdai_abi)
    # wxdai_contract = Contract.from_abi("WXDAI", contracts['WXDAI'], wxdai_abi)
    wxdai_contract = Contracts["WXDAI"]
    # wxdai_contract = web3.eth.contract(
    #     address=contracts['WXDAI'], abi=wxdai_abi)

    for key, value in balances.items():
        asset = key
        if asset != 'WXDAI' and asset != 'XDAI' and asset != 'UNI-V2':
            print(asset)
            path = []
            path.append(contracts[asset])
            path.append(contracts[quote])

            amounts = honeyswap_join.functions.getAmountsOut(
                amountIn, path).call()
            # print(amounts)
            amountOut = amounts[-1]
            print(convertToNormal(amountOut, decimals[asset]))
            prices[asset] = convertToNormal(amountOut, decimals[asset])
    prices['XDAI'] = 1.0
    prices['WXDAI'] = 1.0
    # prices['UNI-V2'] = shareVal
    pprint.pprint(prices)
    total = 0
    for key, value in balances.items():
        if key != 'UNI-V2':
            asset = key
            balancesusd[asset] = value * prices[asset]
            total = total + balancesusd[asset]

    pprint.pprint(balancesusd)
    print(total)
    # get difference
    diffs = {}
    for key, value in portfolio.items():
        adjshare = total * value
        currshare = balancesusd[key]
        diff = adjshare - currshare
        diffs[key] = diff
    diffs = dict(sorted(diffs.items(), key=lambda x: x[1]))
    print('Adjustments ')
    pprint.pprint(diffs)

    # WXDAI as base
    # fill first
    if diffs['XDAI'] < -1.0:
        # swap xDai for wxDai
        dummydiff = 0 - diffs['XDAI']
        if dummydiff > 1.0:
            amountWei = backtoWack(dummydiff, 18)
            print(amountWei)
            tx_hash = wxdai_contract.deposit(
                {"from": acct,   "value": amountWei})
    for key, value in diffs.items():
        if key != 'XDAI' and key != 'WXDAI' and key != 'UNI-V2':
            if value < -1.0:
                asset_contract = Contracts[key]
                pathAddresses = []
                pathAddresses.append(contracts[key])
                pathAddresses.append(contracts[quote])
                toAdrress = web3.toChecksumAddress(accAddress)
                amountOut = 0-value
                amountOutWei = backtoWack(amountOut, 18)
                amountInMax = amountOut / prices[key]
                # slippage 1 %
                amountInMax = amountInMax + amountInMax * 0.01
                amountInMaxWei = backtoWack(amountInMax, 18)
                # 2 hour deadline
                deadline = int(time.time() + 60 * 60 * 2)
                print(
                    key,
                    amountOutWei,
                    amountInMaxWei,
                    pathAddresses,
                    toAdrress,
                    deadline)
                if key == 'HNY':
                    asset_contract.approve(
                        honeyswap_contract, 0, {"from": acct})
                asset_contract.approve(
                    honeyswap_contract, amountInMaxWei, {"from": acct})
                Honeyswap_Contract.swapTokensForExactTokens(
                    amountOutWei,
                    amountInMaxWei,
                    pathAddresses,
                    toAdrress,
                    deadline,
                    {"from": acct, "gas_limit": 12487782, "gas_price": 1000000000})
    for key, value in diffs.items():
        if key != 'XDAI' and key != 'WXDAI' and key != 'UNI-V2':
            if value > 1.0:
                pathAddresses = []
                pathAddresses.append(contracts[quote])
                pathAddresses.append(contracts[key])
                toAdrress = web3.toChecksumAddress(accAddress)
                amountOutMin = value / prices[key]
                # slippage 1 %
                amountOutMin = amountOutMin - amountOutMin * 0.01
                amountOutMinWei = backtoWack(amountOutMin, 18)
                amountIn = value
                amountInWei = backtoWack(amountIn, 18)
                # 2 hour deadline
                deadline = int(time.time() + 60 * 60 * 2)
                print(
                    key,
                    amountInWei,
                    amountOutMinWei,
                    pathAddresses,
                    toAdrress,
                    deadline)
                wxdai_contract.approve(
                    honeyswap_contract, amountInWei, {"from": acct})
                Honeyswap_Contract.swapExactTokensForTokens(
                    amountInWei,
                    amountOutMinWei,
                    pathAddresses,
                    toAdrress,
                    deadline,
                    {"from": acct, "gas_limit": 12487782, "gas_price": 1000000000})
    if diffs['XDAI'] > 1.0:
        # swap wxDai for xDai
        amountWei = backtoWack(diffs['XDAI'], 18)
        print(amountWei)
        tx_hash = wxdai_contract.withdraw(amountWei,
                                          {"from": acct})
        print(tx_hash)
