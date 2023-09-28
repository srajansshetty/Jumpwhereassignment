classes_held = int(input("Enter the number of classes held: "))
classes_attended = int(input("Enter the number of classes attended: "))

attendance_percentage = (classes_attended / classes_held) * 100
if attendance_percentage >= 75:
    print(f"Percentage of classes attended: {attendance_percentage}%")
    print("The student is allowed to sit in the exam.")
else:
    print(f"Percentage of classes attended: {attendance_percentage}%")
    print("The student is not allowed to sit in the exam.")