#NID info

def nid(NAME, GENDER, NATIONALITY, BLOOD_GROUP, ADRESS, DOB):
    print(NAME, GENDER, NATIONALITY, BLOOD_GROUP, ADRESS, DOB)

NAME = str(input("Enter your name: "))
GENDER = str(input("Enter your Gender: "))
NATIONALITY = str(input("Enter your Nationality: "))
BLOOD_GROUP = str(input("Enter your Blood Group: "))
ADRESS = str(input("Enter your adress: "))
DOB = str(input("Enter your Date of birth: "))

nid(NAME, GENDER, NATIONALITY, BLOOD_GROUP, ADRESS, DOB)