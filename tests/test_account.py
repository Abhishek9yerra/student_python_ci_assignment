from student_account import BankAccount

import pytest

def test_BankAccount_initialization():
    account = BankAccount("Abhishek", 100)
    assert account.owner == "Abhishek"
    assert account.balance == 100
    assert account.transaction_count == 0
    pytest.raises(ValueError, BankAccount, "", 100)
    pytest.raises(ValueError, BankAccount, "Abhishek", -100)

def test_balance_property():
    account = BankAccount("Abhishek", 100)
    assert account.balance == 100

def test_transaction_count_property():
    account = BankAccount("Abhishek", 100)
    assert account.transaction_count == 0
    account.deposit(50)
    assert account.transaction_count == 1
    account.withdraw(30)
    assert account.transaction_count == 2

def test_deposit_increases_balance():
    account = BankAccount("Abhishek", 100)
    assert account.deposit(50) == 150
    account1=BankAccount("Bob", 100)
    assert account1.deposit(100) == 200

def test_withdraw_decreases_balance():
    account = BankAccount("Abhishek", 100)
    assert account.withdraw(50) == 50 
    pytest.raises(ValueError, account.withdraw, 200)
    account1=BankAccount("Bob", 200)
    assert account1.withdraw(100) == 100

def test_transfer_to():
    account1 = BankAccount("Abhishek", 100)
    account2 = BankAccount("Boss", 50)
    assert account1.transfer_to(account2, 50) == 50
    assert account2.balance == 100
def test_monthly_interest():
    account = BankAccount("Abhishek", 1200)
    interest = account.monthly_interest(0.12)
    assert interest == 12
    assert account.balance == 1212
    pytest.raises(ValueError, account.monthly_interest, -0.1)

def test_statement():
    account = BankAccount("Abhishek", 100)
    statement = account.statement()
    assert "Owner: Abhishek" in statement
    assert "Balance: 100.00" in statement
    assert "Transactions: 0" in statement
    assert "No transactions." in statement

    account.deposit(50)
    account.withdraw(30)
    statement = account.statement()
    assert "Transactions: 2" in statement
