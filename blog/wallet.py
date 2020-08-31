from web3 import Web3

w3 = Web3(Web3.HTTPProvider('https://kovan.infura.io/v3/ff125c70fb4c45248078eaf3125d9179'))
account = w3.eth.account.create()
privateKey = account.privateKey.hex()
address = account.address

print(f"address: {address}\nKey: {privateKey}")