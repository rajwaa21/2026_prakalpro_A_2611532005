# Name: Rajwa Hasna Khairiyah
# NIM: 2611532005
# Question 6

# Pemanasan
first_name = " muhammad"
last_name = "rafi "
full_name = first_name.strip() + " " + last_name.strip()
print(full_name)
print(full_name.title())

# Soal 6
full_name = "Rajwa Hasna Khairiyah"
nim = "2611532005"
 
# Build the username: first name in lowercase + last 3 digits of the NIM.
# Do not use split().

clean = full_name.strip().lower()
space = clean.find(" ")

if space == -1:
    first_name = clean
else:
    first_name = clean[:space]

username = first_name + nim [-3:]

print(username)