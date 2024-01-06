# Write a program to create Class with name and account number and implement get and set, with property decorator and making account number and name private.  
class BankAccount:
    def __init__(self, name, account_number):
        self._name = name  
        self._account_number = account_number  

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
            self._name = new_name
       
    @property
    def account_number(self):
        return self._account_number

    @account_number.setter
    def account_number(self, new_account_number):
            self._account_number = new_account_number
       
customer = BankAccount(name="Delin", account_number=0000000)


print("Customer Name:", customer.name)
print("Account Number:", customer.account_number)


customer.name = input("enter new name")
customer.account_number = int(input("enter account no"))


print("Updated Customer Name:", customer.name)
print("Updated Account Number:", customer.account_number)
