# xDai HoneySwap Balancer Brownie Mix

This Brownie framework comes with everything you need to start building your own automated portfolio balancer on the xDai network using honeyswap exchange. Motivation is led by decentralised balancing with low gas fees.


## Installation and Setup

1. [Install Brownie](https://eth-brownie.readthedocs.io/en/stable/install.html), if you haven't already.

2. Add xDai network to brownie

```bash
brownie networks add Ethereum xdai host=https://dai.poa.network chainid=100 explorer=https://blockscout.com/poa/xdai
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
    'XDAI': 0.01,
    'WXDAI': 0.09,
    'HNY': 0.80,
    'WETH': 0.05,
    'LINK': 0.05
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

Contracts loaded
HNY 0x71850b7E9Ee3f13Ab46d67167341E4bDc905Eef9
WXDAI 0xe91D153E0b41518A2Ce8Dd3D7944Fa863463a97d
WBTC 0x8e5bBbb09Ed1ebdE8674Cda39A0c169401db4252
WETH 0x6A023CCd1ff6F2045C3309768eAd9E68F978f6e1
LINK 0xE2e73A1c69ecF83F464EFCE6A5be353a37cA09b2
STAKE 0xb7D311E2Eb55F2f68a9440da38e7989210b9A05e
xMOON 0x1e16aa4Df73d29C029d94CeDa3e3114EC191E25A

Native balances
{'HNY': 0.4666707051023862,
 'LINK': 0.0,
 'WETH': 0.0,
 'WXDAI': 182.42428847692705,
 'XDAI': 6.116330417366895}
 
Asset prices
{'HNY': 912.8804552823431,
 'LINK': 12.866424720264057,
 'WETH': 400.73308811476124,
 'WXDAI': 1.0,
 'XDAI': 1.0}
 
USD balances
{'HNY': 426.01456574079833,
 'LINK': 0.0,
 'WETH': 0.0,
 'WXDAI': 182.42428847692705,
 'XDAI': 6.116330417366895}
 
Total USD value
614.5551846350922

Adjustments
{'HNY': 65.6295819672755,
 'LINK': 30.727759231754614,
 'WETH': 30.727759231754614,
 'WXDAI': -127.11432185976875,
 'XDAI': 0.029221428984027575}
 
Swaps 
WETH 30727759231754612736 75145289820679232 ['0xe91D153E0b41518A2Ce8Dd3D7944Fa863463a97d', '0x6A023CCd1ff6F2045C3309768eAd9E68F978f6e1'] 0x513E95Eec3bAC74802b4b2D859e802f17eAE57a9 1603576706
Transaction sent: 0x246c40be5715bc6e6ac0153c654e0d3f7f786e941527326311471c53c6488805
  Gas price: 1.0 gwei   Gas limit: 31909
Waiting for confirmation...
  WXDAI.approve confirmed - Block: 12681353   Gas used: 29009 (90.91%)

Transaction sent: 0xbd3d7f5f54bb859aafbc5865ca4b214777630175ada15a93e1afa076d40ab06b
  Gas price: 1.0 gwei   Gas limit: 12487780
Waiting for confirmation...
  Honeyswap.swapExactTokensForTokens confirmed - Block: 12681354   Gas used: 126250 (1.01%)

LINK 30727759231754612736 2340448469705227264 ['0xe91D153E0b41518A2Ce8Dd3D7944Fa863463a97d', '0xE2e73A1c69ecF83F464EFCE6A5be353a37cA09b2'] 0x513E95Eec3bAC74802b4b2D859e802f17eAE57a9 1603576719
Transaction sent: 0x3df6dca674457cacbae249056d91a14d9ad3e8c1ed8b61679bf5546648e3ae8e
  Gas price: 1.0 gwei   Gas limit: 48409
Waiting for confirmation...
  WXDAI.approve confirmed - Block: 12681356   Gas used: 44009 (90.91%)

Transaction sent: 0x0299a895101db8523c57c7e595d670f2f50ff269da9b5b1bb65c6a7ba895eb52
  Gas price: 1.0 gwei   Gas limit: 12487780
Waiting for confirmation...
  Honeyswap.swapExactTokensForTokens confirmed - Block: 12681359   Gas used: 126238 (1.01%)

HNY 65629581967275499520 70454997645926704 ['0xe91D153E0b41518A2Ce8Dd3D7944Fa863463a97d', '0x71850b7E9Ee3f13Ab46d67167341E4bDc905Eef9'] 0x513E95Eec3bAC74802b4b2D859e802f17eAE57a9 1603576744
Transaction sent: 0x5c11d5a74b3077a06de6352140b554d5b5ee48c47c93486e6c968004657c45a1
  Gas price: 1.0 gwei   Gas limit: 48409
Waiting for confirmation...
  WXDAI.approve confirmed - Block: 12681361   Gas used: 44009 (90.91%)

Transaction sent: 0x1050d021ddf83c0f40c0dd8b54e38f8cd0a1f5c6be8ada526123f7889db06ff5
  Gas price: 1.0 gwei   Gas limit: 12487780
Waiting for confirmation...
  Honeyswap.swapExactTokensForTokens confirmed - Block: 12681376   Gas used: 293387 (2.35%)
```
# Karma Jar

xDai / Eth address:  0x513E95Eec3bAC74802b4b2D859e802f17eAE57a9

# Resources

 - 1Hive [Developer Discord channel](https://discord.gg/2H3gVe)
 - Brownie [Gitter channel](https://gitter.im/eth-brownie/community)
