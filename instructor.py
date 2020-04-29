class Instructor: 
    def __init__(self):
        self.specialty = ""

    def add_specialty(self, specialty): 
        self.specialty.append(specialty)
       
    def assign_exercise(self, student, exercise):
        student.exercises.append(exercise)