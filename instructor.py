from nssperson import NSSPerson
class Instructor(NSSPerson): 
    def __init__(self, first_name, last_name, slack_handle, cohort):
        NSSPerson.__init__(self, first_name, last_name, slack_handle, cohort)
        self.specialty = ""

    def add_specialty(self, specialty): 
        self.specialty.append(specialty)
       
    def assign_exercise(self, student, exercise):
        student.exercises.append(exercise)
        
    def __repr__(self):
        return f'{self.first_name} {self.last_name} is in {self.cohort}!'