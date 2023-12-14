class Student:
    def __init__(self, name, student_id,Student_Health):
        self.name = name
        self.student_id = student_id
        self.registration = self.Student_Registration()
        self.course = self.Student_Course()
        self.Student_Health = Student_Health

    class Student_Registration:
        def __init__(self):
            self.registration_date = ""
            self.registration_status = ""

        def register(self, date):
            self.registration_date = date
            self.registration_status = "Registered"

    class Student_Course:
        def __init__(self):
            self.courses = []

        def add_course(self, course):
            self.courses.append(course)

        def remove_course(self, course):
            if course in self.courses:
                self.courses.remove(course)



# Example usage:
student1 = Student("John Doe", "S001")
print(student1.name)  # Output: John Doe
print(student1.student_id)  # Output: S001

# Registration
student1.registration.register("2023-01-01")
print(student1.registration.registration_date)  # Output: 2023-01-01
print(student1.registration.registration_status)  # Output: Registered

# Courses
student1.course.add_course("Math")
student1.course.add_course("Science")
print(student1.course.courses)  # Output: ['Math', 'Science']

student1.course.remove_course("Science")
print(student1.course.courses)  # Output: ['Math']

# Health
student1.health.update_health_info(170, 65, "O+")
print(student1.health.height)  # Output: 170
print(student1.health.weight)  # Output: 65
print(student1.health.blood_type)  # Output: O+
