#Ask how many cents the customer is owed

cents = int(input("Cents owed: "))

while cents < 0:
  cents = int(input("Cents owed: "))

#define functions to calculate the coins

def calc_quarters(cents):
  quarters = cents / 25
  return int(quarters)

def calc_dimes(cents):
  dimes = cents / 10
  return int(dimes)

def calc_nickels(cents):
  nickels = cents / 5
  return int(nickels)

def calc_pennies(cents):
  pennies = cents
  return int(pennies)

#Calculate the number of quarters
quarters = calc_quarters(cents)
cents = cents - quarters * 25

#Calculate the number of dimes
dimes = calc_dimes(cents)
cents = cents - dimes * 10

#Calculate the number of nickels
nickels = calc_nickels(cents)
cents = cents - nickels * 5

#Calculate the number of pennies
pennies = cents

#Sum of coins
coins = quarters + dimes + nickels + pennies

print(coins)
