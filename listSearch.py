num_students = int(input("How many students will you be adding? "))

students = []


for _ in range(num_students):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    grade = int(input("Enter grade: "))
    email_input = input("Enter email: ")

    student = {
        'name': name,
        'age': age,
        'grade': grade,
        'email': email_input
    }

students.append(student)

print("Thank you for entering student infomation")
print("-" * 30)

for student in students:
    print("Name:", student['name'])
    print("Age:", student['age'])
    print("Grade:", student['grade'])
    print("Email:", student['email'])
    print('-' * 30)

