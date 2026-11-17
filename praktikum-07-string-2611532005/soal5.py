# Name: Rajwa Hasna Khairiyah
# NIM: 2611532005
# Question 5

# Bagian A
username = input("Username: ")
 
# Check the rules in a safe order and print the first rule that fails.
# Messages:
#   "Invalid: at least 5 characters"
#   "Invalid: letters and digits only"
#   "Invalid: must start with a letter"
#   "Valid"

if len(username) < 5:
    print("Invalid: at least 5 characters")
elif not username.isalnum():
    print("Invalid: letters and digits only")
elif not username[0].isalpha():
    print("Invalid: must start with a letter")
else:
    print("Valid")

# Bagian B
NIM = input("NIM: ")

if len (NIM) == 10 and NIM.isdigit():
    print("Valid, intake year 20" + NIM[:2])
else:
    print("Invalid NIM")
