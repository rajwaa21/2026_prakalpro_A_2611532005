# Name: Rajwa Hasna Khairiyah
# NIM: 2611532005
# Question 7

name = "Rajwa Hasna Khairiyah"
nim = "2611532005"
intake = "20" + nim[:2]
# Username dari Soal 6
full_name = "Rajwa Hasna Khairiyah"
clean = full_name.strip().lower()
space = clean.find(" ")

if space == -1:
    first_name = clean
else:
    first_name = clean[:space]

username = first_name + nim [-3:]

print(username)

# 
print("=" * 30)
print("STUDENT CARD".center(30))
print("=" * 30)
print("Name".ljust(10) + ": " + name)
print("NIM".ljust(10) + ": " + nim)
print("Username".ljust(10) + ": " + username)
print("Intake".ljust(10) + ": " + intake)
print("=" * 30)