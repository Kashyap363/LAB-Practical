# Practical 2

# (A)Create a list and apply methods(append, extend, remove, reverse), arrange created
# list into the ascending and descending order

friends = ['Kirtan', 'manav', 'aayush', 'om']
friends.append('aayush')
print(friends)
friends.reverse()
print(friends)
friends.remove('om')
print(friends)
friends.extend(['ansh'])
print(friends)
print(sorted(friends))
print(friends)
friends.sort()
print(friends)
friends.sort(reverse = True)
print(friends)

# (B) List1 = [1, 2, 3, 4, ["python", "java", "c++", [10,20,30]], 5, 6, 7, ["apple", "banana","orange"]]
#From above list get word “orange” and “Python” & repeat this list five times without 
#using loops.
List1 = [1, 2, 3, 4, ['Pyton', 'Java', 'C++',[10, 20, 30]], 5, 6, 7, ['apple', 'grapes', 'banana']]

values = List1[4][0:1] + List1[8][2:3]
five_values = [values] * 5
print(five_values)

# (C) Create a list and copy it using slice function
cars = ['Rollsroys', 'Maserati', 'BMW', 'Mercedes', 'Ferrari']
duplicate_cars = cars[:]
print(duplicate_cars)

# (D) Create a tuple and apply different type of mathematical operation on it (Sum, Maximum, minimum etc.).
numbers = (3, 7, 1, 50, 20)
print("Maximum is ",max(numbers))
print("Minimum is ",min(numbers))
print("Sum is ",sum(numbers))