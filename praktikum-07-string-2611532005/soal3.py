# Name: Rajwa Hasna Khairiyah
# NIM: 2611532005
# Question 3

# Bagian A
text = "Informatika"
print(text[10])
print(text.upper())
print(text[0:20])

# Bagian B
text = "Rajwa Hasna Khairiyah"
count = 0
for char in text:
    if char.lower() in "aiueo":
        count += 1
print("Vowels:", count)