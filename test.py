from main import Banking
bankObj = Banking()
def test_deposit():
    bankObj.deposit(500)
    assert bankObj.getAmount() == 500

def test_withdraw():
    bankObj.withdraw(200)
    assert bankObj.getAmount() == 300