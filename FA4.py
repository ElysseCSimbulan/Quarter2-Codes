student_num = int(input("Enter number of students: "))
subject_num = int(input("Enter number of subjects: "))
total_avg = 0

for i in range(1, student_num + 1):
    print(f"Student {i}")
    score_sum = 0

    for j in range(1, subject_num + 1):
        score = float(input(f"Enter score {j}: "))
        score_sum += score

    student_avg = score_sum / subject_num
    print(f"Average for Student {i} =", student_avg)

    total_avg += student_avg

class_avg = total_avg / student_num
print("Class Average =", class_avg)