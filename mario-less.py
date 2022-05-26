# set a variable for height of the pyramid

height = int(input("Height: "))

# only accept values between 1 and 8 inclusive

while height < 1 or height > 8:

  height = int(input("Height: "))

#setting the value of height into two variables that will change with each new line

print("\n")
print("MARIO LESS")
print("\n")

h = height
i = height

while i != 0:
  
  spaces = h - 1
  s = spaces
  
  while s != 0:
    print(" ", end = "")
    s -= 1

#blocks variable need to use the original height on the formula or it will only print one block

  blocks = height - spaces
    
  while blocks != 0:
    print("#", end = "")
    blocks -= 1

  print("\n")
  
  h -=1
  i -= 1


