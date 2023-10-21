class Student:
    def _init_(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

    def _repr_(self):
        return f"Student(name='{self.name}', roll_number='{self.roll_number}', cgpa={self.cgpa})"

def sort_students(student_list):
    # Sort the student_list in descending order of CGPA
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students

# Test the function with sample data
if _name_ == "_main_":
   students = [
        Student("Alice", "101", 3.9),
        Student("Bob", "102", 3.5),
        Student("Charlie", "103", 4.0),
        Student("David", "104", 3.7),
    ]

    sorted_students = sort_students(students)

    print("Sorted Students:")
  for student in sorted_students:
        print(student)

