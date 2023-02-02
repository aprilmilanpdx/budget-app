class Category:
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
      if self.get_balance() >= amount:
        return True
      return False
    
    def transfer(self, amount, category):
      """Accepts an amount and another budget category as arguments. Adds a withdrawal with the amount and the description "Transfer to [Destination Budget Category]". The method then adds a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]". If there are not enough funds, nothing is added to either ledgers. Returns True if the transfer took place, and False otherwise."""
      if self.check_funds(amount):
        self.withdraw(amount, "Transfer to " + category.name)
        category.deposit(amount, "Transfer from " + self.name)
        return True
      return False

def create_spend_chart(categories):
  """ accepts a list of categories as an argument and returns a string that is a bar chart"""

  names_list = []
  withdraw_list = []
  for category in categories:
    names = category.name
    names_list.append(names)
    height = len(max(names_list, key=len))
    padded = [word.ljust(height) for word in names_list]

    withdraw_total = 0
    for item in category.ledger:
      if item["amount"] < 0:
          withdraw_total += item["amount"]
    withdraw_list.append(withdraw_total)
  total = int(round(sum(withdraw_list)))

  percentages = []
  for num in withdraw_list:
    percent = num * 100 / total 
    bar_percent = (percent // 10) * 10
    percentages.append(bar_percent)

  chart = "Percentage spent by category\n"
 
  for num in reversed(range(0, 110, 10)):
    chart += f"{str(num) + '|':>4}"
    for percent in percentages:
      if percent >= num:
        chart += " o "
      else:
        chart += "   "
    chart += " \n"
    
  chart += "    " + ("-" * (len(names_list) + 2) * 2) + "\n" 

  for row in zip(*padded):
    chart += "     " + "  ".join(row) + "  \n"

  return chart.rstrip("\n")
