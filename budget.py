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
      """Accepts an amount and description(default: empty string).  Appends object to the ledger list in the form of {"amount": amount, "description": description}"""
      self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description = ""):
      """Accepts an amount and description(default: empty string). amount stored in the ledger as negative. If not enough funds, nothing is added to the ledger. Returns True if the withdrawal took place, and False otherwise."""
      if self.check_funds(amount):
        self.ledger.append({"amount": -amount, "description": description})
        return True
      return False

    def get_balance(self):
      """Returns the current balance of the budget category based on the deposits and withdrawals that have occurred."""
      balance = 0
      for entry in self.ledger:
        balance += entry["amount"]
      return balance

    def check_funds(self, amount):
      """Accepts an amount as an argument. Returns False if the amount > balance of the category.  Returns True otherwise."""
      if self.get_balance() > amount:
        return True
      return False
    
    def transfer(self, amount, category):
      """Accepts an amount and another budget category as arguments. Adds a withdrawal with the amount and the description "Transfer to [Destination Budget Category]". The method then adds a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]". If there are not enough funds, nothing is added to either ledgers. Returns True if the transfer took place, and False otherwise."""
      if self.check_funds(amount):
        self.withdraw(amount, "Transfer to " + category.name)
        category.deposit(amount, "Transfer from " + self.name)
        return True
      return False

    def get_withdrawal(self):
      total = 0
      for item in self.ledger:
        if item["amount"] < 0:
          total += item["amount"]
      return total

    def get_total(categories):
      total = 0
      category_list = []
      for category in categories:
        total += category.get_withdrawal()
        category_list.append(category.get_withdrawal())
      return category_list
      
# The chart should show the percentage spent in each category passed in to the function. The percentage spent should be calculated only with withdrawals and not with deposits. Down the left side of the chart should be labels 0 - 100. The "bars" in the bar chart should be made out of the "o" character. The height of each bar should be rounded down to the nearest 10. The horizontal line below the bars should go two spaces past the final bar. Each category name should be written vertically below the bar. There should be a title at the top that says "Percentage spent by category".

# This function will be tested with up to four categories.

def create_spend_chart(categories):
  """ accepts a list of categories as an argument and returns a string that is a bar chart"""
  chart = "Percentage spent by category\n"
  
  for num in reversed(range(0, 110, 10)):
    chart += str(num) + "\n"
  
  chart += "-" * 10 + "\n" 

  for name in zip(*categories):
    chart += "  ".join(name) + "\n"
