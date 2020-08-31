from web3 import Web3

def sendTransaction(message):
    w3 = Web3(Web3.HTTPProvider('https://kovan.infura.io/v3/ff125c70fb4c45248078eaf3125d9179'))
    address = '0xBba5A74dB30ED844a7bf4e966b59eFdA2Cd75991'
    privateKey = '0xc13c2b241446f4b4a00ebc83c498022777fc27e9e5efe49531ae67fd1b3ac7bc'
    nonce = w3.eth.getTransactionCount(address)
    gasPrice = w3.eth.gasPrice
    value = w3.toWei(0, 'ether')
    signedTx = w3.eth.account.signTransaction(dict(
        nonce = nonce,
        gasPrice=gasPrice,
        gas = 100000,
        to='0x0000000000000000000000000000000000000000',
        value = value,
        data = message.encode('utf-8')
    ), privateKey)

    tx = w3.eth.sendRawTransaction(signedTx.rawTransaction)
    txId = w3.toHex(tx)
    return txId

