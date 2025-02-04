class Banking:
    def __init__(self):
        self.amount=0
    
    def deposit(self,amount):
        self.amount+=amount
 
    def withdraw(self,amount):
        self.amount-=amount
      
    def getAmount(self):
            return self.amount
    
# bankObj = Banking()
# print(bankObj.getAmount())