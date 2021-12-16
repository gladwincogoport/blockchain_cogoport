from web3 import Web3, contract
import json

ganache_url = "HTTP://127.0.0.1:8545"

web3 = Web3(Web3.HTTPProvider(ganache_url))

add_1 = "0xc7f453315CBe9b0E4E9f56851921A5E3fFd80fD9"
add_2 = "0x8DaDF1c33758Fb0Fa882C7E8851730E75DAcc90a"

add_1_p_key = "8e298b3a0237825a242f6e5357c82e4e0c446bd990b4083f97e706f127d1424c"

# Build a transaction

''' Nonce : Nonce is a history of your transactions. It prevents a transaction from being executed more than once'''
nonce = web3.eth.getTransactionCount(add_1)

tx = {
    'nonce': nonce,
    'to': add_2,
    'value': web3.toWei('1', 'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei('50', 'gwei')
}

signed_tx = web3.eth.account.sign_transaction(tx, add_1_p_key)

tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
print(tx_hash)
