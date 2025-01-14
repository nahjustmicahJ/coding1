# list - a data type for collectiing and organizing data.
# - list can contain all data types, including other list
# - lists are changable, we can update the list
# - lists can contain duplicate data
# - we can get specific list items based on its index position.

# INput is a function that allows us to enter data directly into
# our program from the terminal
# data that is passed in from an input function autmoatically becomes
# a string
# name = input('Whats is your name?')
# print(name)

# list functions
skiiTripItem_ShoppingCart = ['gloves']
# Insert() - allows us to enter a new list item
# based on an index position

# insert requires 2 arguments to work.

skiiTripItem_ShoppingCart.insert(1,'Snow Boots')
skiiTripItem_ShoppingCart.insert(2,'goggles')
print(skiiTripItem_ShoppingCart)

# append() - allow us tp enter a new line into a list
# without having to provide an index location. append() will
# automatically put the new item at the end of the list

skiiTripItem_ShoppingCart.append('scarf')
print(skiiTripItem_ShoppingCart)

# remove() - allows us to remove an item from a list
# it works by specifiying what item you want to take out

skiiTripItem_ShoppingCart.remove('scarf')
print(skiiTripItem_ShoppingCart)

# pop() - allows us to remove the last item 

skiiTripItem_ShoppingCart.pop()
print(skiiTripItem_ShoppingCart)

# clear()/del() - allows us to delete/remove all items in a list
del skiiTripItem_ShoppingCart
skiiTripItem_ShoppingCart.clear()

print(skiiTripItem_ShoppingCart)