#1. Create a greeting for your program.

#2. Ask the user for the city that they grew up in.

#3. Ask the user for the name of a pet.

#4. Combine the name of their city and pet and show them their band name.

#5. Make sure the input cursor shows on a new line, see the example at:
#   https://replit.com/@appbrewery/band-name-generator-end

#YOUR CODE BELOW

print("Welcome to the Band Name Generator!!\n")

city = input("What is the name of the city you grew up in?\n")

pet = input("What is the name of your pet?\n")

band_name = city + ' ' + pet

print(f"Your band name is {band_name}")
