from cohort import Cohort
from exercise import Exercise 
from instructor import Instructor 
from student import Student
from nssperson import NSSPerson

daily_journal = Exercise("Daily Journal", "Javascript")
student_exercises = Exercise("Student Exercises", "Python")
perennial = Exercise("Capstone", "React")
nutshell = Exercise("Nutshell", "Javascript")

cohort_38 = Cohort("Cohort 38")
cohort_37 = Cohort("Cohort 37")
cohort_24 = Cohort("Cohort 24")
cohort_9 = Cohort("Evening Cohort 9")

bjork_g = NSSPerson("Bjork", "Guðmundsdóttir", "@bjorkg", cohort_9)
kate_bush = NSSPerson("Kate", "Bush", "@wutheringheights", cohort_38)
kurt_cobain = NSSPerson("Kurt", "Cobain", "@nirvana", cohort_37)
billy_holiday = NSSPerson("Billy", "Holiday", "@gloomybilly", cohort_24)

thom_yorke = NSSPerson("Thom", "Yorke", "@thomyorke", cohort_9)
elizabeth_fraiser = NSSPerson("Elizabeth", "Frasier", "@pearlydewdropsdrop", cohort_38)
billy_corgan = NSSPerson("Billy", "Corgan", "@patrick", cohort_24)
bilinda_butcher = NSSPerson("Bilinda", "Butcher", "@bilindab", cohort_37)

#How can I add special traits?

# bilinda_butcher.assign_exercise(kurt_cobain, perennial)
# billy_corgan.assign_exercise(billy_holiday, nutshell)
# elizabeth_fraiser.assign_exercise(kate_bush, student_exercises)
# thom_yorke.assign_exercise(bjork_g, daily_journal)
