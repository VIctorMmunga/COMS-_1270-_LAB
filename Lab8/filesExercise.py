def main():
    # Read students
    with open('students.txt', 'r') as f:
        students = [line.strip() for line in f]

    # Read scores
    with open('scores.txt', 'r') as f:
        scores = [float(line.strip()) for line in f]

    # Calculate grades (example: just pair student and score)
    grades = list(zip(students, scores))

    # Write output
    with open('grades.txt', 'w') as f:
        for student, score in grades:
            f.write(f"{student} {score}\n")
    print("Grades written to grades.txt")

if __name__ == "__main__":
    main()