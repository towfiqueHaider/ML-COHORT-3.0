#tuples - task 2

# Creates a tuple with the names of 5 cities.
city_names = ("Tokyo", "Lisbon", "Nairobi", "Rio", "Denver")

#Prints the third city in the tuple
print(city_names[2])

#Converts the tuple into a list, adds a new city, and converts it back to a tuple.
city_list = list(city_names)
city_list.append("Helsinki")
city_names2 = tuple(city_list)

#Prints the modified tuple.
print(city_names2)