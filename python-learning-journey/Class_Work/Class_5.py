# Sets
# sets doesnot allow duplicate

name: str = 'Ali'
phonenumber: int = 29482093483
age: float = 12.43
colors: list = ['red', 'green']
colors2: list = ['red', 'green', 89]  # mixed types allowed without type hinting strictness

fruits_name: set = {'apple', 'apple', 'orange', 'grapes'}

print(fruits_name)  #
# print(fruits_name[0]) # Error


# Union
electronics_cust: set = {'ali', 'ahmed', 'nabeel'}
garments_cust: set = {'zargham', 'ahmed', 'ashfaq'}

merge = electronics_cust.union(garments_cust)
print(merge)


# ASSIGNMENT

# 2 set creating 1. Wow_react 2. Laugh_react #.all

wow_react: set = {'ali', 'ahmed', 'kashan'}
laugh_react: set = {'kamran', 'nabeel', 'asfand'}

all = wow_react.union(laugh_react)
# another of union is using pipe operator |
all = wow_react | laugh_react
print(all)


# Intersection 
# Common element ko ak sath likh kr da dega

summer_fruits: set = {'mango', 'apple', 'watermelon'}
winter_fruits: set = {'oranges', 'banana', 'apple'}

common_fruits: set = summer_fruits.intersection(winter_fruits)
print(common_fruits)

winter_fruits: set = {'oranges', 'apple', 'annar'}
if 'oranges' in winter_fruits:
    print('oranges')

if 'mango' not in winter_fruits:
    winter_fruits.add('mango')  # ✅ fixed: added mango

lunch = {'bhindi'}
if 'bhindi' in lunch:
    lunch.discard('bhindi')  # ✅ fixed: discarded correctly


# Assignments
# 1.laiba_frineds  2. nabia_friends 3.mutual_friends

laiba_friends: set = {'nabia', 'fatima', 'ayesha', 'laraib'}
nabia_friends: set = {'laiba', 'fatima', 'yusra', 'ayesha'}

mutual_friends: set = laiba_friends.intersection(nabia_friends)
# another method of  intersection
mutual_friends: set = laiba_friends & nabia_friends
print(mutual_friends)


winter_fruits: set = {'apple', 'mango'}
if 'oranges' in winter_fruits:
    print('oranges')


# Assignment
# Create a set named fruits containing "apple", "banana", "cherry".
# Add "orange" to the fruits set.
# remove "banana" from the set.
# check if apple is in the set.
# clear all the items from the set

fruits_name: set = {"apple", "banana", "cherry"}
# add orange in list
fruits_name.add("orange")
print(fruits_name)
# remove banana
if "banana" in fruits_name:
    fruits_name.remove("banana")
print(fruits_name)
# check apple is in the list
if "apple" in fruits_name:
    print("APPLE IS HERE")
    print(fruits_name)
# clear all the list
fruits_name.clear()
print("The list is empty")
print(fruits_name)


# For Loops (when you know the ending point)
# The following example is add to cart feature.
# Think yourself as a superstore customer.
# After shopping you will be charged the amount of the products you have purchased.
# Price of each product is added to the total

cart: list = [
    {'product': 'shoes', 'price': 39},
    {'product': 'Tshirt', 'price': 99},
    {'product': 'hat', 'price': 59},
    {'product': 'socks', 'price': 11},
]

total: int = 0
for kharcha in cart:
    total = total + kharcha['price']

print(total)


# While loop (executed till the certain condition is True)
# Think of yourself as a men who is doing the activity of scanning the price of the Product
# The duty of the men is to scan the price of all the products in the basket.
# When the items in the basket ends the condition becomes false and the program ends

total = 0
while True:
    price_input: str = input("Enter the price of the Product ")

    if price_input == 'done':
        break

    if price_input.isdigit():
        total += int(price_input)
        print("Current total:", total)
