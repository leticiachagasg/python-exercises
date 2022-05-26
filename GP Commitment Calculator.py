print("Welcome to the GP Commitment Calculator")

LP_commitment = float(input("\nWhat is the total LP Commitment? "))

GP_commitment = float (input("\nWhat is the GP contribution percentual? \n (ex: 1%  = input 1): "))

GP_percentage = GP_commitment / 100

LP_percentage = 1 - GP_percentage 

# Get formula to round + show 2 decimals

GP_total = (LP_commitment * GP_percentage) / LP_percentage

print(f"\nThe total GP commitment is ${GP_total:.2f}")
