# Donte' Brown  
# September 15th 2026
# This program stores student's exam grades as a list and student attendance as a set.

# Stored Data (lists)
grades = [83,85,72,65,76,90,79,88,93,70,67,80]
average = sum(grades)/len(grades)

# Attendance sets
day1 = {"Mary", "Jake", "Sam","Alex","Percy", "Jessica","Trent","Mahmoud"}
day2 = {"Jake","Sam", "Alex", "Percy","Mahmoud","Trent","Caleb","Zayne"}
all_stu = day1.union(day2)
both = day1.intersection(day2)
one_day = day1.symmetric_difference(day2)
# Output
print(f"{len(grades)} students took the exam.")
print(f"The highest grade was {max(grades)}")
print(f"The lowest grade was {min(grades)}")
print(f"The average grade for the exam was a {average:.1f}")
print()
print(f"{len(all_stu)} students attended the class")
print(f"{both} attended both class days.")
print(f"{one_day} attended one class day.")
print()