from nssperson import NSSPerson
class Student(NSSPerson): 
    def __init__(self, first_name, last_name, slack_handle, cohort):
        NSSPerson.__init__(self, first_name, last_name, slack_handle, cohort)
        self.exercises = []
    def __repr__(self):
        return f'{self.first_name} {self.last_name} is in {self.cohort}!'