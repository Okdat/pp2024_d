def add_students():
    return int(input("Enter the number of students: "))

def student_info():
    student_id = input("Enter student id: ")
    student_name = input("Enter student name: ")
    student_dob = input("Enter date of Birth: ")
    return {'id': student_id, 'name': student_name, 'dob': student_dob}

def num_of_courses():
    return int(input("Enter number of courses: "))
     
def course_info():
    course_id = input("Enter course ID: ")
    course_name = input("Enter course name: ")
    return {'id': course_id, 'name': course_name}

def input_marks(student, course):
    mark = float(input(f"Enter mark for {student['name']} in {course['name']}: "))
    return mark

def main():
    students = []
    courses = []
    marks = {}

    num_students = add_students()
    for _ in range(num_students):
        student_info_data = student_info()
        students.append(student_info_data)

    num_courses = num_of_courses()
    for _ in range(num_courses):
        course_info_data = course_info()
        courses.append(course_info_data)

    for course in courses:
        for student in students:
            mark = input_marks(student, course)
            marks[(student['id'], course['id'])] = mark

    print("\nStudent Mark Management System:")
    print("-------------------------------")
    print("Students:")
    for student in students:
        print(f"ID: {student['id']}, Name: {student['name']}, DoB: {student['dob']}")

    print("\nCourses:")
    for course in courses:
        print(f"ID: {course['id']}, Name: {course['name']}")

    print("\nMarks:")
    for (student_id, course_id), mark in marks.items():
        print(f"Student ID {student_id}, Course ID {course_id}: {mark}")

if __name__ == "__main__":
    main()
