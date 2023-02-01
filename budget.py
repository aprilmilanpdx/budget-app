class Category:
  # def __init__(self) -> None:
    # pass
    def __init__(self, name):
      self.name = name
      self.ledger = []
    
    def __str__(self):
      heading = f"{self.name}".center(30,'*') + "\n"
      items = ""
      total = 0
      for item in self.ledger:
        items += f"{item['description'][:23]:23}" + f"{item['amount']:>7.2f}" + "\n"
        total += item['amount']
      output = heading + items + "Total: " + str(total)
      return output

    def deposit(self, amount, description = ""):
      """accepts an amount and description(default: empty string).  Appends object to the ledger list in the form of {"amount": amount, "description": description}"""
      self.ledger.append({"amount": amount, "description": description})

    def get_balance(self):
      """returns the current balance of the budget category based on the deposits and withdrawals that have occurred"""
      balance = 0
      for entry in self.ledger:
        balance += entry["amount"]
      return balance

    def check_funds(self, amount):
      """Accepts an amount as an argument. It returns False if the amount is greater than the balance of the budget category and returns True otherwise. This method should be used by both the withdraw method and transfer method."""
      if self.get_balance() > amount:
        return True
      return False

    def withdraw(self, amount, description = ""):
      """accepts an amount and description(default: empty string). amount stored in the ledger as negative. If there are not enough funds, nothing should be added to the ledger. This method should return True if the withdrawal took place, and False otherwise"""
      if self.check_funds(amount):
        self.ledger.append({"amount": -amount, "description": description})
        return True
      return False
    
    def transfer(self, amount, category):
      """Accepts an amount and another budget category as arguments. Adds a withdrawal with the amount and the description "Transfer to [Destination Budget Category]". The method then adds a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]". If there are not enough funds, nothing should be added to either ledgers. This method should return True if the transfer took place, and False otherwise."""
      if self.check_funds(amount):
        self.withdraw(amount, "Transfer to " + category.name)
        category.deposit(amount, "Transfer from " + self.name)
        return True
      return False

    


# def create_spend_chart(categories):