class Customer:
    last_id = 0
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        Customer.last_id += 1
        self.customer_id = Customer.last_id

    def __repr__(self):
        return self.__class__.__name__ + "(" + str(self.customer_id) + "): " + self.first_name + " " + self.last_name + " (" + self.email + ")"


class Account:
    last_id = 0
    def __init__(self, customer):
        self.customer = customer
        self._balance = 0
        self.interest_rate = 0.05
        Account.last_id += 1
        self.account_id = Account.last_id

    def deposit(self, amount):
        if amount >= 0:
            self._balance += amount
            if self._balance >= amount:
             print("Deposited: " + str(amount) + ". The new balance is: " + str(self._balance))
        else:
            print("You can't withdraw money from only deposit account!")

    def charge(self, amount):
        if self._balance >= amount:
            if amount >= 1000:
                print("You can't withdraw more thaan 999 zlotych at once")
            else:
                self._balance -= amount
                print("Charged: " + str(amount) + ". The new balance is: " + str(self._balance))
        else:
            print("Sorry, you do not have that much money on your account to withdraw: " + str(amount))

    def calc_interest(self):
        self._balance += self.interest_rate*self._balance
        print("Your balance now is " + str(self._balance))
        pass

    def get_balance(self):
        print("The balance is: " + str(self._balance))
        return self._balance

    def __repr__(self):
        return "{0} ({1}): {2} belonging to: {3} {4} ".format(self.__class__.__name__, self.account_id, self._balance, self.customer.first_name, self.customer.last_name)
        #return self.__class__.__name__ + "(" +  + ")" + " belonging to: " + self.customer.first_name + " " + self.customer.last_name  + " (" + self.customer.email + ")"

class Bank:
    def __init__(self):
        self.customers = []
        self.accounts = []

    def create_customer(self, first_name, last_name, email):
        c = Customer(first_name, last_name, email)
        self.customers.append(c)
        return c

    def create_account(self, customer):
        a = Account(customer)
        self.accounts.append(a)
        return a

    def transfer(self, acc_id_from, acc_id_to, amount):
        acc_id_from.charge(amount)
        acc_id_to.deposit(amount)
        print("You transfered: " + str(amount))
        pass

    def __repr__(self):
        return 'Bank(cust: {0}, acc: {1})'.format(self.customers, self.accounts)


bank = Bank()

c1 = bank.create_customer("Jan", "Kowalski", "j.kowalski@gmail.com")
print(c1)
a1 = bank.create_account(c1)
print(a1)
a1.deposit(-200)
a1.deposit(200)
a1.deposit(10000)
a1.charge(100)
a1.charge(1000)
a1.calc_interest()
a2 = bank.create_account(c1)

bank.transfer(a1,a2,200)

print(bank)