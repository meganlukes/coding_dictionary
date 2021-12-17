programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.", 
  "Function": "A piece of code that you can easily call over and over again." 
  }

#retrieving items from dictionary
# print(programming_dictionary["Bug"])
 
#adding new items to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over."
print(programming_dictionary)
print("")
# #to wipe an existing dictionary
# programming_dictionary = {}

# #to edit an item in dictionary
# programming_dictionary["Bug"] = "An insect"
# print(programming_dictionary)


for thing in programming_dictionary:
  #to get a list of library's keys
  print(thing)
  #to get a list of values
  print(programming_dictionary[thing])