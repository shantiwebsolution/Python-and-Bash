students_dict = {'EXSITING': 75}
"""Display the menu options"""
print("    STUDENT GRADE MANAGEMENT SYSTEM")
print("1. Add new student and grade")
print("2. Update existing student's grade")
print("3. Print all student grades")
action = input("Select an option (1-3): ")

if action == "1":
    students_dict['NEW'] = 85
elif action == "2":
    students_dict['jayesh'] = 90
elif action == "3":
    print(students_dict)
else:
    print("Invalid option. Please try again.")
