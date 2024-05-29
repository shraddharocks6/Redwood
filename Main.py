from Transaction import Transaction
from Wallet import Wallet 
from TransactionPool import TransactionPool
from Block import Block
from Blockchain import Blockchain
from BlockchainUtils import BlockchainUtils

import pprint

if __name__ == '__main__':
    sender = 'sender'
    receiver = 'receiver'
    amount = 1
    type = 'TRANSFER'

    #transaction = Transaction(sender, receiver, amount, type)
    #print(transaction.toJson())

    #wallet = Wallet()
    #signature = wallet.sign(transaction.toJson())
    #print(signature)

    #transaction.sign(signature)
    #print(transaction.toJson())

    #signatureValid = Wallet.signatureValid(transaction.payload(), signature, wallet.publicKeyString())
    #print(signatureValid)

    # wallet = Wallet()
    fraudulentWallet = Wallet()
    # transaction = wallet.createTransaction(receiver, amount, type)
    # signatureValid1 = Wallet.signatureValid(transaction.payload(), transaction.signature, wallet.publicKeyString())
    # signatureValid2 = Wallet.signatureValid(transaction.payload(), transaction.signature, fraudulentWallet.publicKeyString())

    # print(signatureValid1)
    # print(signatureValid2)

    wallet = Wallet()
    fraudulentWallet = Wallet()
    pool = TransactionPool()

    transaction = wallet.createTransaction(receiver, amount, type)

    if pool.transactionExists(transaction) == False:
        pool.addTransaction(transaction)
    
    # if pool.transactionExists(transaction) == False:
    #     pool.addTransaction(transaction)
    
    # print(pool.transactions)

    # block = Block(pool.transactions, 'lastHash', 'forger', 1)
    # print(block.toJson())

    blockchain = Blockchain()

    lastHash = BlockchainUtils.hash(blockchain.blocks[-1].payload()).hexdigest()
    blockCount = blockchain.blocks[-1].blockCount + 2
    
    block = wallet.createBlock(pool.transactions, lastHash, blockCount)

    if not blockchain.lastBlockHashValid(block):
        print('lastBlockHash is not valid')

    if not blockchain.blockCountValid(block):
        print('Blockcount is not valid')
    
    if blockchain.lastBlockHashValid(block) and blockchain.lastBlockHashValid(block):
        blockchain.addBlock(block)

    # print(block.toJson())
    # pprint.pprint(block.toJson())

    # signatureValid = Wallet.signatureValid(block.payload(), block.signature, wallet.publicKeyString())
    # print(signatureValid)

    #blockchain.addBlock(block)
    pprint.pprint(blockchain.toJson())