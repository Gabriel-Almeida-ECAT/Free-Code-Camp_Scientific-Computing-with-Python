# https://replit.com/@GabrielAlmeid57/boilerplate-budget-app-8#main.py

class Category:
  ledger = []
  
  def __init__(self, name_category):
    self.__name_Category = name_category
    self.__ledger = []

  def deposit(self, in_amount, in_description = False):
    dic = {}
    dic['amount'] = in_amount
    if in_description:
      dic['description'] = in_description
    else:
      dic['description'] = ''
    self.__ledger.append(dic)

  def withdraw(self, in_amount, in_description = ''):
    if not self.check_funds(in_amount):
      return False
    else:
      self.__ledger.append( dict([ ('amount', (-1*in_amount)), ('description', in_description)]))
      return True  

  def get_balance(self):
    ACM = 0
    for i, itens in enumerate(self.__ledger):
      ACM += itens['amount']
    return ACM

  def check_funds(self, in_amount):
    if self.get_balance() < in_amount:
      return False 
    else:
      return True


  def transfer(self, in_amount, reciver):
    if not self.check_funds(in_amount):
      return False 
    else:
      string1 = f"Transfer to {reciver.__name_Category}"
      self.withdraw(in_amount, string1)
      string2 = f"Transfer from {self.__name_Category}"
      reciver.deposit(in_amount, string2)
      return True

  def get_ledger(self):
    for i in self.__ledger:
      print(i)
  
  def getLedger(self, li):
    for i in self.__ledger:
      li.append(i)

  def getName(self):
    return self.__name_Category

  def __str__(self):
    printstr = ""
    len_title = len(self.__name_Category)
    in_stars = 15 - (int(len_title/2) + (len_title % 2 > 0))
    ed_stars = 15 - int(len_title/2)
    printstr += '*'*in_stars
    printstr += self.__name_Category
    printstr += '*'*ed_stars
    printstr += '\n'
    for iten in self.__ledger:
      if(len(iten['description'])>29):
        for i in range(23):
            printstr += iten['description'][i]
        printstr += "%7.2f"%(float(iten['amount']))
      else:
        printstr += iten['description']
        printstr += " "*(23-len(iten['description']))
        printstr += "%7.2f"%(float(iten['amount']))
      printstr += '\n'
    printstr += "Total: " + "%.2f"%(self.get_balance())
    return printstr


def create_spend_chart(cat1):
  graph_names = []
  graph_values = []

  for obj in cat1:
    graph_names.append(obj.getName())
    ACM = 0
    lis = []
    obj.getLedger(lis)
    for dici in lis:
      if(dici['amount'] < 0):
        ACM += -1*dici['amount']
    graph_values.append(ACM)

    total_value = sum(graph_values)
    graph_percentages = []
    for item in graph_values:
      graph_percentages.append(int( (item/total_value)*10 ) * 10)
    
    graph = []
    graph_row = []
    for i in range(100,-10,-10):
      for item in graph_percentages:
        if(item >= i):
          graph_row.append('o')
        else:
          graph_row.append(' ')
      graph.append(graph_row)
      graph_row = []

  graphstr = "Percentage spent by category\n"
  lis_ind = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]
  for ind_row in range(11):
    graphstr += "%3.d|"%(lis_ind[ind_row])
    for ind_col in range(len(graph[ind_row])):
      if(ind_col==0):
        graphstr += " %c"%(graph[ind_row][ind_col])
      else:
        graphstr += "  %c"%(graph[ind_row][ind_col])
    graphstr += "  \n"
  
  graphstr += "    " + "-"*((len(graph_names)*2)+3) + "\n"

  size_titles = 0
  for word in graph_names:
    if len(word) > size_titles:
      size_titles = len(word)

  for i, word in enumerate(graph_names):
    if(len(word) < size_titles):
      graph_names[i] += " "*(size_titles - len(word))

  for ind_row in range(size_titles):
    graphstr += "   "
    for ind_col in range(len(graph_names)): 
      graphstr += "  %c"%(graph_names[ind_col][ind_row])
    graphstr += "  \n"

  return graphstr



if __name__ == '__main__':
  food = Category("Food")
  food.deposit(1000, "initial deposit")
  food.withdraw(10.15, "groceries")
  food.withdraw(15.89, "restaurant and more food for dessert")
  print(food.get_balance())
  
  clothing = Category("Clothing")
  food.transfer(50, clothing)
  clothing.withdraw(25.55)
  clothing.withdraw(100)
  auto = Category("Auto")
  auto.deposit(1000, "initial deposit")
  auto.withdraw(15)

  print(food)
  print(clothing)

  print(create_spend_chart([food, clothing, auto]))