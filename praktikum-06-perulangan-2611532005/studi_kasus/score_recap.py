PASS_SCORE = 70
EXCELLENT_SCORE = 85

student = int(input("Number of students: "))
while student < 1:
    print("Invalid student count!")
    student = int(input("Number of students: "))

total = 0
passed = 0
excellent = 0

for n in range(1, student + 1):
    nilai = int(input("Enter score: "))
    while nilai < 0 or nilai > 100:
        print("Invalid score!")
        nilai = int(input("Enter score: "))
    total += nilai
    if nilai >= PASS_SCORE:
        passed += 1
    if nilai >= EXCELLENT_SCORE:
        excellent += 1

average = round(total / student, 2)

print("Total score:", total)
print("Average score:", average)
print("Passed:", passed)
print("Excellent count:", excellent)