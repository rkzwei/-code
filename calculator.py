def calculator():
  def add(n1, n2):
    return n1 + n2

  def sub(n1, n2):
    return (n1) - (n2)

  def mult(n1, n2):
    return n1 * n2

  def div(n1, n2):
    return n1 / n2

  operations = {
  "+": add,
  "-": sub,
  "*": mult,
  "/": div,
  }

  go = True
  count = 0
  num1 = int(input("What is the first number? "))
  for key in operations:
    print(key)
  while go:
    symbol = input("Pick an operation: ")
    num2 = int(input("What's the next number? "))
    answer = operations[symbol](num1, num2)
    print(f"{num1} {symbol} {num2} = {answer}")
    count += 1
    if count == 5:
      clear()
      count = 0
    if input("Would you like to continue calculating? y/n\n") == "y":
      num1 = answer
      continue    
    else:
      break
calculator()