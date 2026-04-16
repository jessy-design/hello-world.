def get_gpa_point(marks):
    if marks >= 90: return 4.0
    elif marks >= 80: return 3.5
    elif marks >= 70: return 3.0
    elif marks >= 60: return 2.5
    elif marks >= 50: return 2.0
    else: return 0.0

print("--- MWC Grade to US GPA Converter ---")
num_subjects = int(input("How many subjects do you have? "))

total_points = 0

for i in range(num_subjects):
    subject_marks = float(input(f"Enter marks for subject {i+1} (out of 100): "))
    total_points += get_gpa_point(subject_marks)

final_gpa = total_points / num_subjects

print(f"\nYour estimated US GPA is: {final_gpa:.2f}")

if final_gpa >= 3.8:
    print("Result: Stanford/Ivy Tier. Keep grinding!")
elif final_gpa >= 3.5:
    print("Result: Very Strong. Competitive for Top 30 US Schools.")
else:
    print("Result: Good start. Focus on raising those core marks!")
