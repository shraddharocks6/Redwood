

class TransactionPool():

    def __init__(self):
        self.transactions = []
    
    def addTransaction(self, transaction):
        self.transactions.append(transaction)
    
    def transactionExists(self, transaction):
        #check if this transaction exists
        for poolTransaction in self.transactions:
            if poolTransaction.equals(transaction):
                return True
        return False
