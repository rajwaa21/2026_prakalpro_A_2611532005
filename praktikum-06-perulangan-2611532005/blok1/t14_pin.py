attempt_2005 = 1
MAX_ATTEMPTS_2005 = 3
correct_pin_2005 = "1234"
pin_2005 = input("Enter PIN: ")

while pin_2005 != correct_pin_2005 and attempt_2005 < MAX_ATTEMPTS_2005:
    print("Incorrect PIN.")
    attempt_2005 += 1
    pin_2005 = input("Enter PIN: ")

if pin_2005 == correct_pin_2005:
    print("Access granted")
else:
    print("Account locked")