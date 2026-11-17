# Name: Rajwa Hasna Khairiyah
# NIM: 2611532005
# Bonus

kalimat = input("Masukkan kalimat: ")
text = kalimat.lower().replace(" ", "")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")