#Name: Mary Clayton
#Date: 7/4/2022
#Purpose: Price counter
#Initalize the count variables to 0
count = 0
#Initalize the sum variable to 0
sum = 0
#Welcome Message
print("Welcome to your own prices program")
#Input full_name
full_name = input("Please enter your full name: ")
#Input the min_price and convert it to float
min_price = float(input("Please enter minimum price: "))
#Create a list of prices
price_list = [69.0, 71.0, 84.5, 91.0, 67.4, 81.2, 84.6, 58.8, 
79.3, 101.2]
#Add price counter to price_list
for price in price_list:
    sum += min_price
    if price > min_price:
        count += 1
#Output
print("Hello", full_name, "the minimum price is", min_price)
print("There are", count, "prices greater than the minimum price")
print("The total price is", sum)

