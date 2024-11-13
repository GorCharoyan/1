grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
a = len(grades[0])
b = sum(grades[0])
c = b/a
grades[0] = c
a = len(grades[1])
b = sum(grades[1])
c = b/a
grades[1] = c
a = len(grades[2])
b = sum(grades[2])
c = b/a
grades[2] = c
a = len(grades[3])
b = sum(grades[3])
c = b/a
grades[3] = c
a = len(grades[4])
b = sum(grades[4])
c = b/a
grades[4] = c
students = sorted(students)
gpa = dict(zip(students,grades))
print(gpa)



