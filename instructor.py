from nssperson import NSSPerson
class Instructor(NSSPerson): 
    def __init__(self, first_name, last_name, slack_handle, cohort):
        NSSPerson.__init__(self, first_name, last_name, slack_handle, cohort)
        self.specialty = ""

    def add_specialty(self, specialty): 
        self.specialty.append(specialty)
       
    def assign_exercise(self, student, exercise):
        student.exercises.append(exercise)