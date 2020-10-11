# xDai HoneySwap Balancer Brownie Mix

This Brownie framework comes with everything you need to start building your own automated portfolio balancer on the xDai network using honeyswap exchange. Motivation is led by decentralised balancing with low gas fees.


## Installation and Setup

1. [Install Brownie](https://eth-brownie.readthedocs.io/en/stable/install.html), if you haven't already.

2. Add xDai network to brownie

```bash
brownie networks add Ethereum xdai host=https://dai.poa.network chainid=100
```

3. Setup your account (import by private key)

```bash
brownie accounts new <id>
```

4. Download these files. Edit scripts/Honeybalance.py
Change the following lines to include your account id and desired portfolio allocations as a ratio of 1.0. 
```pyhton
acct = accounts.load(<id>)

portfolio = {
    'XDAI': 0.10,
    'WXDAI': 0.20,
    'HNY': 0.70
}
```
Note that you must include XDAI for transaction costs and WXDAI for the base of trading. Note also that liquidity tokens are excluded.

## Basic Use

Make sure you have a balance of xDai and have set your account id and portfolio correctly in scripts/Honeybalance.py:

```bash
$ brownie run Honeybalance.py
```

Output should look something like this.

```python
Brownie v1.11.1 - Python development framework for Ethereum

BalancerProject is the active project.
Enter the password to unlock this account:
0x513E95Eec3bAC74802b4b2D859e802f17eAE57a9

Running '\xDai\balancer\scripts\Honeybalance.py::main'...
Native balances
{'HNY': 0.010103709894396873,
 'WXDAI': 7.248460291475703,
 'XDAI': 1.7707885005242983}
 
Asset prices
HNY
885.9722898914424
{'HNY': 885.9722898914424, 'WXDAI': 1.0, 'XDAI': 1.0}

USD balances
{'HNY': 8.951606991537622,
 'WXDAI': 7.248460291475703,
 'XDAI': 1.7707885005242983}

Total USD value
17.970855783537623

Adjustments
{'HNY': 3.627992056938714,
 'WXDAI': -3.6542891347681783,
 'XDAI': 0.026297077829464}

Swap Info
HNY 3627992056938714112 4053977959975946 ['0xe91D153E0b41518A2Ce8Dd3D7944Fa863463a97d', '0x71850b7E9Ee3f13Ab46d67167341E4bDc905Eef9'] 0x513E95Eec3bAC74802b4b2D859e802f17eAE57a9 1602448971

Transaction sent: 0x6eb2bfb37de1d873f48f9b980628b48064e82f3016386d3e3b87611dc0154b72
  Gas price: 1.0 gwei   Gas limit: 12487782
Waiting for confirmation...
  Honeyswap.swapExactTokensForTokens confirmed - Block: 12464677   Gas used: 336054 (2.69%)
```
# Karma Jar

xDai / Eth address:  0x513E95Eec3bAC74802b4b2D859e802f17eAE57a9

# Resources

 - 1Hive [Developer Discord channel](https://discord.gg/2H3gVe)
 - Brownie [Gitter channel](https://gitter.im/eth-brownie/community)
