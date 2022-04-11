class BankAccount:
    def __init__ (self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    def request (self):
        print(f"{self.balance} miktarda paranız bulunmaktadır.")

    def deposit (self,amount):
        self.balance += amount
        print(f"İşlem başarıyla tamamlandı. Hesabınıza {amount} tutarında para aktarılmıştır." )

    def withdraw (self,amount):
        if((self.balance - amount >=0)):
            self.balance -=amount
            print(f"Hesabınızından {amount} tutarında para çektiniz.")
            return self.balance
        else:
            print("Hesapta yeterli miktarda paranız bulunmamaktadır.")
            return self.balance

account1 = BankAccount("Erdal", 10000)
account2 = BankAccount("Semih", 12000)
account3 = BankAccount("Tunahan", 7500)

account1.request()
account2.deposit(500)
account3.withdraw(7500)
account3.request()