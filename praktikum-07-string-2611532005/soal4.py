# Name: Rajwa Hasna Khairiyah
# NIM: 2611532005
# Question 4

phone = "082611532005"
masked = phone[:4] + "*" * (len(phone) - 7 ) + phone[-3:]
print(masked)