num_students = int(input("Enter number of students: "))
num_subjects = int(input("Enter number of subjects: "))

sum_of_student_averages = 0

for student_index in range(1, num_students + 1):
    print(f"\nStudent {student_index}")
    total_score = 0
    
    for subject_index in range(1, num_subjects + 1):
        score_input = float(input(f"Enter score {subject_index}: "))
        total_score += score_input
    
    average_score_per_student = total_score / num_subjects
    print(f"Average for Student {student_index} = {average_score_per_student:.1f}")

    sum_of_student_averages += average_score_per_student

average_class_score = sum_of_student_averages / num_students
print(f"\nClass Average = {average_class_score:.1f}")
