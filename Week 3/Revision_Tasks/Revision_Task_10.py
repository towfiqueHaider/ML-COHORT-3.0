'''
create an empty dictionary, 
allow 4 friends to enter their favourite programming language as values and keys as their name. 
and display them. 
assume the names are unique
'''
myDict ={}

for i in range(0,4):
    friendName = str(input("Enter friend name:"))
    languageName = str(input("Enter language name:"))
    myDict.update({friendName:languageName})

print(myDict)
