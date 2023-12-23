# https://replit.com/@GabrielAlmeid57/boilerplate-arithmetic-formatter#arithmetic_arranger.py

def arithmetic_arranger(listStr, ans = False ):
  listValues = []
  listOperations = []
  listResult = []
  listSize = []
  strSup = []
  listStringNumbers = []
  listStringResults = []

  if (len(listStr) > 5):
    return print("Error: Too many problems.")

  for string in listStr:
    if (not isinstance(string, str)):
      return print("Error: invalid argument")
    strSup = string.split()
    if (len(strSup) != 3):
      return print("Error: invalid syntax")
    
    if (strSup[1] == '+'):
      listOperations.append('+') 
    elif(strSup[1] == '-'):
      listOperations.append('-')
    else: 
      return print("Error: Operator must be '+' or '-'.")

    if (not strSup[0].isdecimal() or not strSup[2].isdecimal()):
      return print("Error: Numbers must only contain digits.")

    if (len(strSup[0]) > 4 or len(strSup[2]) > 4):
      return print("Error: Numbers cannot be more than four digits.")
    else:
      listValues.append(int(strSup[0]))
      listValues.append(int(strSup[2]))
      listStringNumbers.append(strSup[0])    
      listStringNumbers.append(strSup[2])
  
  for i in range(0,(len(listStr)*2),2):
    n = 1
    x = int(i/2)
    if(listOperations[x] == '+'):
      listResult.append(listValues[i] + listValues[i+1])
      listStringResults.append(str(listValues[i] + listValues[i+1]))
    else: 
      if(listOperations[x] == '-'):
        listResult.append(listValues[i] - listValues[i+1])
        listStringResults.append(str(listValues[i] + listValues[i+1]))

    if (len(listStringNumbers[i]) > n):
      n = len(listStringNumbers[i])
    
    if (len(listStringNumbers[i+1]) > n):
      n = len(listStringNumbers[i+1])
    
    if (len(listStringResults[x]) > n):
        n = len(listStringResults[x])
    listSize.append(n)

  if ans: 
    for i in range(len(listStr)):
      print("%*d    "%(listSize[i]+2, listValues[i*2]), end='')
    
    print("")
    for i in range(len(listStr)):
      print("%c%*d    "%(listOperations[i], listSize[i]+1, listValues[(i*2)+1]), end='')
    
    print("")
    for i in range(len(listStr)):
      x = listSize[i]+2
      print("-"*x, "   ", end='')
    
    print("")
    for i in range(len(listStr)):
      print("%*d    "%(listSize[i]+2, listResult[i]), end='')
  
  else: 
    for i in range(len(listStr)):
      print("%*d    "%(listSize[i]+2, listValues[i*2]), end='')
    
    print("")
    for i in range(len(listStr)):
      print("%c%*d    "%(listOperations[i], listSize[i]+1, listValues[(i*2)+1]), end='')
    
    print("")
    for i in range(len(listStr)):
      x = listSize[i]+2
      print("-"*x, "   ", end='')

  return None


if __name__ == '__main__':
  print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))