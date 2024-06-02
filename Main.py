from Transaction import Transaction
from Wallet import Wallet 
from TransactionPool import TransactionPool
from Block import Block
from Blockchain import Blockchain
from BlockchainUtils import BlockchainUtils
from AccountModel import AccountModel

import pprint

#This file is being used for the purpose of testing all the other classes and methods

if __name__ == '__main__':
    wallet = Wallet()
    accountModel = AccountModel()

    accountModel.addAccount(wallet.publicKeyString())

    print(accountModel.balances)